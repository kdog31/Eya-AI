#imports
import re
import time
import sys
import os
import datetime
import vlc
import pyttsx
import json

#database stuff
def database_load()
	db = open("eyadb", "r")
	data = json.loads(db.read())
	b.close()
	#print data
	return data
	
def database_save()
	b_file = open("eyadb", "w")
	data = json.dumps(db, separators=(',', ':'))
	db_file.write(data)
	db_file.close()
	
def say(saystr):
	os.system("say " + str(saystr))

def input(db)
	say("shat should i call you?")
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