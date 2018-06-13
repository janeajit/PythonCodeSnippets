import sys
characterList = ["19", "10", "58", "1B", "A8", "2E", "18", "01", "03", "62", "28", "04", "00", "0A", "38", "F6", "43", "0D", "48", "09", "00", "AB", "B7"]
for character in characterList:
	sys.stdout.write(character.decode("hex"))
