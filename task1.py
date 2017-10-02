import csv
x = open("Crime.csv", 'r') # opens the file read-only mode


def extract_info(w): # function to get the desired info from file
	c = 0
	a = "ASSAULT"
	for a in w:
		c+=1
	print(c)

extract_info(x) # call the function




