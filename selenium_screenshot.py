from selenium import webdriver
from selenium.webdriver.common.keys import Keys
navigator = "firefox"
url = "http://www.serval-concept.com"
size = None
img = "prise_ecran.png"

if navigator == "firefox" : 
	browser = webdriver.Firefox()
elif navigator == "chrome": 
	browser = webdriver.Chrome()
elif navigator == "ie": 
	browser = webdriver.Ie()
else : 
	raise Exception("impossible de trouver le navigateur")

if size != None :
	browser.set_window_size(size[0],size[1])
browser.get(url)
browser.get_screenshot_as_file(img)
browser.quit()
