import csv
x = open("Crime.csv", 'r') # opens the file read-only

crime_type, no_of_times = [], [] # creating 2 lis

a = "ASSAULT"

def new_func (): #creates a list of unique crimes
	# something

def extract_info(w): # function to get the desired info from file
#	if  row[8] in w:
#		crime_type.append(row[8])y
	c = 0
#	for i in len(crime_type): #loop that goes for the len of the list created
	for a in w: # loop that check the value in the list in the file
		c+=1 # couter that increament the value
		 # appends the list with number of times the 
#	print (crime_type)
	print (c)

extract_info(x) # call the function




