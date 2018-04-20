myString = input("Input a string: ")
binFile = open("Binary Message.txt", 'w')
for letter in myString:
	ordNum = ord(letter)
	binNum = bin(ordNum)
	binNum = str(binNum)
	binNum = binNum.replace("b", "")
	binFile.write(binNum)
	
binFile.close()
