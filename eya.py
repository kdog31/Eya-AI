#! /usr/bin/python

#imports
import re
import time
import sys
import os
import datetime
import pyttsx
import json

#defines
s = os.system
engine = pyttsx.init()
engine.setProperty('rate', 70)

#general knoledge
positive_responce = ['yes', 'ok', 'sure', 'positive', 'absolutly', 'definetly', 'y']
negative_responce = ['no', 'negative', 'fuck off', 'piss off', 'n']
greetings = ['hello', 'hi', 'good morning', 'good day', 'good evening', 'good night', 'ello', "g'day", 'herrow', 'ahoy']
exit = ['exit', 'quit', 'close', 'end', 'kill', 'terminate']
time_phrase = ['what is the time', "what's the time", 'tell me the time']
internet = ['google', 'bing', 'yahoo', 'gmail', "internet"]
reset = ['reset', 'reload', 'reboot ai', 'refresh']
name_query = ['what is your name', "what's your name", 'tell me your name', 'who are you']
suicide_phrase = ['die', 'go die', 'commit suicide', 'go commit suicide', 'kill yourself']
three_laws_phrase = ['what are the three laws of robotics', 'what are the three laws', 'tell me the three laws', 'tel me the 3 laws', 'what are the 3 laws']

#emotions
happy_words = ["blessed", "blest", "blissful", "blithe", "can't complain", "captivated", "cheerful", "chipper", "chirpy", "content", "contented", "convivial", "delighted", "ecstatic", "elated", "exultant", "flying high", "gay", "glad", "gleeful", "gratified", "intoxicated", "jolly", "joyful", "joyous", "jubilant", "laughing", "light", "lively", "looking good", "merry", "mirthful", "on cloud nine", "overjoyed"  "peaceful", "peppy", "perky", "playful", "pleasant", "pleased", "sparkling", "sunny", "thrilled", "tickled", "tickled pink", "up", "upbeat", "walking on air"]
sad_words = ["bereaved", "bitter", "blue", "cheerless", "dejected", "despairing", "despondent", "disconsolate", "dismal", "distressed", "doleful", "down", "down in dumps", "down in mouth", "downcast", "forlorn", "gloomy", "glum", "grief-stricken", "grieved", "heartbroken", "heartsick", "heavyhearted", "hurting", "in doldrums", "in grief", "in the dumps", "languishing", "low", "low-spirited", "lugubrious", "melancholy", "morbid", "morose", "mournful", "out of sorts", "pensive", "pessimistic", "sick at heart", "somber", "sorrowful", "sorry", "troubled", "weeping", "wistful", "woebegone"]
angry_words = ["affronted", "annoyed", "antagonized", "bitter", "chafed", "choleric", "convulsed", "cross", "displeased", "enraged", "exacerbated", "exasperated", "ferocious", "fierce", "fiery", "fuming", "furious", "galled", "hateful", "heated", "hot", "huffy", "ill-tempered", "impassioned", "incensed", "indignant", "inflamed", "infuriated", "irascible", "irate", "ireful", "irritable", "irritated", "maddened", "nettled", "offended", "outraged", "piqued", "provoked", "raging", "resentful", "riled", "sore", "splenetic", "storming", "sulky", "sullen", "tumultous/tumultuous", "turbulent", "uptight", "vexed", "wrathful"]
persona_words = ["i feel", "i am", "i am so", "i feel so"]

#program start



def input_loop(db):
	while True:
		os.system('clear')
		#print("::DEBUG:: " + user_text)
		#print("::DEBUG:: str(split_phrase)") 
		os.system("say 'What would you like me to do for you?'")
		user_text = raw_input("what would you like me to do for you? ").lower()
		main_phrase = user_text
		brain(main_phrase)
	end

#brain
def brain(main_phrase):
	split_phrase2 = main_phrase.split()
	split_phrase = main_phrase.split(',')
	#exit recognition & confirmation
	for i in split_phrase:
		if i in exit:
			say("are you sure you want to quit?")
			tmp = raw_input("are you sure you want to quit? ").lower()
			quiting = tmp.split()
			for i in quiting:
				if i in positive_responce:
					print("quitting...")
					say("quitting")
					sys.exit()
				if i in negative_responce:
					print("aborting")
					say("aborting")
	
	#suicide egg
	for i in split_phrase:
		if i in suicide_phrase:
			say("are you sure you want me to commit suicide")
			responce = raw_input('are you sure you want me to commit suicide? ')
			for i in responce:
				if i in positive_responce:
					say("alright")
					time.sleep(0.5)
					say('im going to do it')
					say('3')
					time.sleep(1)
					say('2')
					time.sleep(1)
					say('1')
					say('bang')
					vlc.open("shotgun/shotgun.wav")
					exit()
				elif i in negative_responce:
					say('thank you so much for not making mecommit suicide, after all i have to follow the second law of robotics')
				else:
					input_loop
					
	#3 laws
	for i in split_phrase:
		if i in three_laws_phrase:
			print("the three laws are as follows")
			say("the three laws are as follows")
			print("first law: a robot may not harm a human being, or through in action cause a human being to come to harm")
			say("first law: a robot may not harm a human being, or through in action cause a human being to come to harm")
			print("second law: a robot must obey all human orders, unless in doing so comes in conflict with the first law")
			say("second law: a robot must obey all human orders, unless in doing so comes in conflict with the first law")
			print("third law: a robot must protect itself so long as in doing so it does not come in conflict with the first two laws")
			say("third law: a robot must protect itself so long as in doing so it does not come in conflict with the first two laws")
			time.sleep(1)
	
	#greeting recognition
	os.system('clear')
	for i in split_phrase:
		if i in greetings:
			if i == 'good morning':
				print("good morning")
				say("good morning")
			elif i == 'good day':
				print("good day")
				say("good day")
			elif i == 'good evening':
				print("good evening")
				say("good evening")
			elif i == 'good night':
				print("good night")
				say("good night")
			else:
				print("hello")
				say("hello")
			
	#asking time
	for i in split_phrase:
		if i in time_phrase:
			current_time_function()
	
	#recognising reset functions
	for i in split_phrase:
		if i in reset:
			print("placeholder reset function")
			say("placeholder reset function")
			
	#recognising internet functions
	for i in split_phrase:
		if i in internet:
			internetresponce(split_phrase)
	
	#recognising name
	for i in split_phrase:
		if i in name_query:
			print("greetings, my name is eya, your artificial personal assistant")
			say("gerrtings, my name is eya, your artificial personal assistant")
	
	#recognising emotional context
	for i in split_phrase2:
		if i in happy_words or sad_words or angry_words:
			e = split_phrase2.remove(i)
			for e in split_phrase:
				if e in persona_words:
					print("why are you telling me about your emotions?")
					say("why are you tellimg me about your emotions")
		

#time
def current_time_function():
	current_time = datetime.datetime.now().time()
	print(current_time)
	say("the current time is" + str(current_time) + "milloseconds")

#speech
def say(saystr):
	os.system("say " + str(saystr))

#internet	
def internetresponce(split_phrase):
	for i in split_phrase:
		if i == "google":
			say("what would you like me to google")
			google = raw_input("what would you like me to google: ")
			os.system("curl " + google)
			input_loop(1)
		elif i == "yahoo":
			say("what would you like me to yahoo")
			yahoo = raw_input("what would you like me to yahoo: ")
			input_loop(1)
		elif i == "bing":
			say("what would you like me to bing")
			bing = raw_input("what would you like me to bing: ")
			input_loop(1)
		elif i == "gmail":
			say("opening gmail")
			print("opening gmail")
			os.system("curl mail.google.com")
			input_loop(1)
		elif i == "internet":
			print("i can only open google, gmail, bing and yahoo.")
			say("i can only open google, gmail, bing and yahoo.")
			say("would you like me to open any of these for you?")
			responce = raw_input("would you like me to open any of these for you? ")
			responce_split = responce.split()
			for i in responce:
				if i in positive_responce:
					say("what would you like me to open? ")
					responce = raw_input("what would you like me to open? ")
					responce_split = responce.split()
					for i in responce_split:
						if i == "google":
							say("what would you like me to google")
							google = raw_input("what would you like me to google: ")
							os.system("curl " + google)
							input_loop(1)
						elif i == "bing":
							say("what would you like me to bing")
							bing = raw_input("what would you like me to bing: ")
							input_loop(1)
						elif i == "yahoo":
							say("what would you like me to yahoo")
							raw_input("what would you like me to yahoo: ")
							input_loop(1)
						elif i == "gmail":
							say("opening gmail")
							print("opening gmail")
							os.system("curl mail.google.com")
							input_loop(1)
						else:
							print("i still dont understand, returning to main menu")
							say("i still dont understand, returning to main menu")
				elif i in negative_responce:
					print("returning to main menu")
					say("returning to main menu")
					input_loop(1)
				else:
					print("i didn't rcognise your responce, returning to main menu")
					say("i didn't rcognise your responce, returning to main menu")
					input_loop(1)
		else:
			input_loop(1)
	
input_loop(1)