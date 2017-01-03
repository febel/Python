message="Bienvenue en CDAISI"
LETTERS="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key=13
translated=""

message=message.upper()
for symbol in message:
	if symbol in LETTERS:
		num=LETTERS.find(symbol)
		num=num+key
		if num >=  len(LETTERS):
			num = num - len(LETTERS)
		elif num < 0 :
			num = num + len(LETTERS)
		translated = translated + LETTERS[num]
	else:
		translated = translated + symbol
print translated
