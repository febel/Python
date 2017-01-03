def main():
	monMessage= 'Bienvenue en CDAISI'
	maCle=8
	ciphertext = encryptMessage(maCle,monMessage)
	print ciphertext + '|'
	
def encryptMessage(key, message):	
	ciphertext = ['']*key
	for col in range(key):
		pointer = col
		while pointer < len(message):
			ciphertext[col] += message[pointer]
			pointer += key
	return ''.join(ciphertext)

if __name__ == '__main__':
	main()

