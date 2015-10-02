#imports
import os
import json

#database stuff
db = open("eyadb", "w")	
	
def say(saystr):
	os.system("say " + str(saystr))

def input(db):
	say("What should i call you?")
	name = raw_input("what should i cal you?")
	print("ok so your name is " + name + ", nice to meet you")
	say("ok so your name is " + name + ", nice to meet you")
	say("when were you born?")
	DOB_DAY = raw_input("Day: ")
	DOB_MONTH = raw_input("Month, in numbers: ")
	DOB_YEAR = raw_input("Year: ")
	say("ok now i know how old you are")
	say("what is your favorite food?")
	Food = raw_input("favorite food: ")
	say("ok thank you, i have everything i need")
	DOB = DOB_DAY + "/" + DOB_MONTH + "/" + DOB_YEAR
	db.write("hello world")
	db.write(name + "\n")
	db.write(DOB + "\n")
	db.write(Food)	
input(1)