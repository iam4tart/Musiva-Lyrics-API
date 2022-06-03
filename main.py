import requests
from bs4 import BeautifulSoup
from flask import Flask, request, jsonify

# instantiating a Flask app
app = Flask(__name__)

# web scraping lyrics from 'songlyrics.com'

def get_lyrics(artist_name, song_name):

  URL = f"http://www.songlyrics.com/{artist_name}/{song_name}-lyrics/"

  res = requests.get(URL)

  soup = BeautifulSoup(res.content,'html5lib')
  data = soup.find('p',attrs={'id':'songLyricsDiv'}).getText()
  print(data)
  return data

# routing URLs

@app.route('/lyrics/', methods=['GET'])
def respond():
  # retrieve Artist Name from URL parameter
  # /lyrics/?artist=
  artist = request.args.get("artist", 'rihanna')
  song = request.args.get("song", 'diamonds')
  lyrics = get_lyrics(artist, song)
                            
  # for debugging
  print(f'received artist_name: {artist}')
  print(f'received song_name: {song}')
  # response var
  response = {}

  # verifying the response variable
  if not artist:
    response['ERROR'] = f"No artist found with name: {artist}"
  elif str(artist).isdigit():
    response['ERROR'] = "Atleast a million dollar artist"
  elif not song:
    response['ERROR'] = f"No song found with name: {song}"
  elif str(song).isdigit():
    response['ERROR'] = "Atleast a decent song"
  else:
    response['lyrics'] = f"{lyrics}"
  # return json response
  return jsonify(response)

@app.route('/')
def homepage():
    return '''
    <h1>Musiva Lyrics API</h1>
    '''

#--
if __name__ == '__main__':
  # multiple user access
  app.run(threaded=True, port=5000, debug=True, use_reloader=True)
