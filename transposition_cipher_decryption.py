import math

def main():
	monMessage = 'BeIi SeeInnv eCnDuA'
	maCle = 8
	plaintext=decryptMessage(maCle,monMessage)
	print plaintext

def decryptMessage(cle,message):
	numOfColumns = int( math.ceil(len(message)/float(cle)) )
	print "nombre de colonnes" + str(numOfColumns)
	numOfRows = cle
	numOfShadedBoxes = ( numOfColumns * numOfRows) - len(message)
	plaintext=['']*numOfColumns
	col = 0
	row = 0
	for symbol in message:	
		plaintext[col] += symbol
		col += 1
		if ( col == numOfColumns) or (col == numOfColumns -1 and row >= numOfRows - numOfShadedBoxes):
 			col = 0
			row += 1
	return ''.join(plaintext)

if __name__=='__main__':
	main()
