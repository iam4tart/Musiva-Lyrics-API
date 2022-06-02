import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

# instantiating a Flask app
app = Flask(__name__)

# web scraping lyrics from 'songlyrics.com'

def get_lyrics():
  artist_name = "Rihanna" #input("Artist Name: ")
  song_name = "Diamonds" #input("Song Name: ")

  URL = f"http://www.songlyrics.com/{artist_name}/{song_name}-lyrics/"

  response = requests.get(URL)

  soup = BeautifulSoup(response.content,'html5lib')
  data = soup.find('p',attrs={'id':'songLyricsDiv'}).getText()

  return data

lyrics = get_lyrics()

# routing URLs

@app.route('/lyrics/', methods=['GET'])
def respond():
  # retrieve Artist Name from URL parameter
  # /lyrics/?artist=
  artist = request.args.get("artist", None)
  # for debugging
  print(f'received artist_name: {artist}')
  # response var
  response = {}

  # verifying the response variable
  if not artist:
    response['ERROR'] = f"No artist found with name: {artist}"
  elif str(artist).isdigit():
    response['ERROR'] = "Atleast a million dollar artist"
  else:
    response['MESSAGE'] = f"Welcome to Musiva Lyrics API!"

  # return json response
  return jsonify(response)

#--
#if __name__ = '__main__':
  # multiple user access
  #app.run(threaded=True, port=5000)


  if artist:
    return jsonify({
      "lyrics": f"{lyrics}",
      "METHOD": "POST"
    })
  else:
    return jsonify({
      "ERROR": f"No artist found with name: {artist}"
    })
