import csv 
import sys
import re

sex_datafile_name = 'name_gender.csv' 
#data file must be a csv file
target_file_name = 'test.csv' 
#target file must be a csv file


#######create a dictionary of name and sex###########################
def getfirstname(s):
	firstname = s.split()[0]
	return firstname

def getlastname(s):
	lastname= s.split()[-1]
	return lastname

def getname(s):
	a = getfirstname(s)
	b = getlastname(s)
	return a + " " + b

def getsex(name):
	if name in namedict:
		return namedict[name]
	else:
		return 2

namedict = {}
f = open(sex_datafile_name, 'rt')
reader = csv.reader(f)
for row in reader:
	name = getname(row[0])
	sex = row[1]
	namedict[name] = sex
f.close()

######import new names from .txt file#################################
f = open(target_file_name, 'rt')
g = open('result.csv','w')
reader = csv.reader(f)
for row in reader:
	name = getname(row[0])
	sex = str(getsex(name))
	g.write(name + " " + sex + '\n')
f.close()
g.close()