import requests
from bs4 import BeautifulSoup
import json

def get_lyrics():
  artist_name = "Rihanna" #input("Artist Name: ")
  song_name = "Diamonds" #input("Song Name: ")

  URL = f"http://www.songlyrics.com/{artist_name}/{song_name}-lyrics/"

  response = requests.get(URL)

  soup = BeautifulSoup(response.content,'html5lib')
  data = soup.find('p',attrs={'id':'songLyricsDiv'}).getText()
  print(data)
  #format = '{"lyrics":"'+f'{data}'+'"}'

  #format = "{"+f'"lyrics": \"{data}\"'+"}"
  #jsonobj = json.loads(format)
  #print(jsonobj)
get_lyrics()




