import csv
x = open("Crime.csv", 'r') # opens the file read-only

crime_type, no_of_times = [], [] # creating 2 list
def extract_info(w): # function to get the desired info from file
	if  row[8] in w:
		crime_type.append(row[8])
	c = 0
	a = "ASSAULT"
	for a in w:
		c+=1
	print(c)

extract_info(x) # call the function




