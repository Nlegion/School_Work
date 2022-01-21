import os
import time
import speech_recognition as sr
from fuzzywuzzy import fuzz
import pyttsx3
import datetime

speak_engine = pyttsx3.init()
voices = speak_engine.getProperty('voices')
now = datetime.datetime.now()
hour = now.hour
minute = now.minute
speak_engine.say( f'сейчас {hour} часов,{minute} минут'.format(hour , minute))
speak_engine.runAndWait()
#print( 'Сейчас ', hour, ' часов', minute, ' минут')
