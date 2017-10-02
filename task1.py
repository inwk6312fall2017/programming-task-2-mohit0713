import csv
x = open("Crime.csv", 'r') # opens the file read-only

crime_type, no_of_times = [], [] # creating 2 list



def extract_info(w): # function to get the desired info from file
#	if  row[8] in w:
#		crime_type.append(row[8])
#	c = 0
#	for i in len(crime_type): #loop that goes for the len of the list created
	for i in w: # loop that check the value in the list in the file
		c+=1 # couter that increament the value
		no_of_times.append(c) # appends the list with number of times the 
#	print (crime_type)
	print (no_of_times)

extract_info(x) # call the function




