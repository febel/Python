#navigation automatique sur un site web authentifié ( environnement de travail) avec recuperation d'emploi du temps d'une semaine
#precise et screenshot
# Fonction qui renvoie le mois en lettres
def trad_mois(mois) :
	mois_traduit = 0
	if int(mois) == 1 :
		mois_traduit = "Janvier"
	elif int(mois) == 2 :
		mois_traduit = "Février"
	elif int(mois) == 3 :
		mois_traduit = "Mars"
	elif int(mois) == 4 :
		mois_traduit = "Avril"
	elif int(mois) == 5 :
		mois_traduit = "Mai"
	elif int(mois) == 6 :
		mois_traduit = "Juin"
	elif int(mois) == 7 :
		mois_traduit = "Juillet"
	elif int(mois) == 8 :
		mois_traduit = "Aout"
	elif int(mois) == 9 :
		mois_traduit = "Septembre"
	elif int(mois) == 10 :
		mois_traduit = "Octobre"
	elif int(mois) == 11 :
		mois_traduit = "Novembre";
	elif int(mois) == 12 : 
		mois_traduit = "Décembre"
	return mois_traduit

# Fonction qui calcule le premier et le dernier jour de la semaine ISO (lundi et dimanche)
def weekbegend(year, week):
    d = date(year, 1, 1)
    delta_days = d.isoweekday() - 1
    delta_weeks = week
    if year == d.isocalendar()[0]:
        delta_weeks -= 1
    # delta pour le debut de la semaine
    delta = timedelta(days=-delta_days, weeks=delta_weeks)
    weekbeg = d + delta
    # delta2 pour la fin de la semaine
    delta2 = timedelta(days=6-delta_days, weeks=delta_weeks)
    weekend = d + delta2
    return weekbeg, weekend


# *** CODE ***
semaine_a_recup = 0
# Gestion des options (paramètres) :
usage = "\n\tpython %prog [options]"
parser = OptionParser(usage = usage)
parser.add_option("-s", "--semaine", help="No de semaine par rapport a la semaine actuelle.", dest="semaine_a_recup")
(options, args) = parser.parse_args()

# Mauvaise longueur d'argument  
if len(sys.argv) != 0 and len(sys.argv) != 3 :
	parser.print_usage()
	sys.exit(1)

if options.semaine_a_recup :
	try :
		semaine_a_recup = int(options.semaine_a_recup)
	except ValueError, e :
		print "Erreur, la valeur de semaine saisie n'est pas un entier !"
		print "ARRET."
		sys.exit(1)


# Récupération de la semaine actuelle :
aujourdhui = date.today()
semaine_actuelle = aujourdhui.isocalendar()[1]
annee_actuelle = aujourdhui.isocalendar()[0]

# On récupère le lundi et le dimanche de la semaine à récupérer
if int(semaine_actuelle + semaine_a_recup) >= 52 :
	lundi, dimanche = weekbegend(annee_actuelle+1, (semaine_actuelle+semaine_a_recup)-52)
else :
	lundi, dimanche = weekbegend(annee_actuelle, (semaine_actuelle+semaine_a_recup))

a_trouver = "Lundi "+str(lundi.day)+" "+trad_mois(lundi.month)+" "+str(lundi.year)+" - "+"Dimanche "+str(dimanche.day)+" "+trad_mois(dimanche.month)+" "+str(dimanche.year)

print "Semaine à récupérer :"+a_trouver


# Pour l'ouverture du fichier PDF en automatique
#    on modifie le profile du navigateur
# Dans l'entete de la page de télechargement, le type de fichier est 'application/force-download'
profile = webdriver.FirefoxProfile()
profile.set_preference("browser.helperApps.neverAsk.openFile", "application/force-download")
driver = webdriver.Firefox(firefox_profile=profile)


# Donc on commence par l'université directement
driver.get("http://www.univ-valenciennes.fr")
assert "de Valenciennes" in driver.title

driver.find_element_by_link_text("Accès à mon ENT").click()

driver.find_element_by_link_text("Identifiez-vous").click()
assert "authentification" in driver.title

# A REMPLACER
username = driver.find_element_by_id("username")
username.send_keys("login_name")

# A REMPLACER
password = driver.find_element_by_id("password")
password.send_keys("password")

driver.find_element_by_name("submit").click()
assert "Vie universitaire" in driver.page_source

# On se déplace dans le menu déroulant 'Mon bureau'
# pour selectionner 'Emploi du temps'
move_mouse = driver.find_element_by_link_text("Mon bureau")
action = ActionChains(driver)
action.move_to_element(move_mouse)
action.perform()
driver.find_element_by_link_text("Emploi du temps").click()

# On switche de frame pour accéder aux éléments qui s'y trouvent
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))

# Si la semaine à récupérer est inférieure à la date actuelle
#	-> on clique sur before
cpt = 0
if semaine_a_recup < 0 :
	while cpt > semaine_a_recup :
		driver.find_element_by_id("form_week:btn_before").click()
		cpt -= 1
# Si la semaine à récupérer est supérieure à la date actuelle
#	-> on clique sur next
elif semaine_a_recup > 0 :
	while cpt < semaine_a_recup :
		driver.find_element_by_id("form_week:btn_next").click()
		cpt += 1
# Sinon, on ne fait rien

# On vérifie si le lundi et le dimanche calculés au début correspondent à la semaine du calendrier
calendrier = driver.find_element_by_id('form_week').text

if a_trouver in calendrier.encode("utf-8") :
# On récupère le fichier avec l'icone 'télecharger la fiche PDF' :
	to_download = driver.find_element_by_css_selector("img[alt='export pdf']")
	to_download.click()
else :
	print "Un problème est survenu, la semaine du calendrier de l'ENT ne correspond pas à la semaine prévue."

# On ne ferme pas le navigateur, l'utilisateur le fera
# après avoir enregistré ou visualisé le fichier.
