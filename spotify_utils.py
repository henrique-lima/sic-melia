import pprint
import sys
import spotipy
import spotipy.util as util
from track import Track
from artist import Artist

class Spotify_Utils:

    def __init__(self):

        self._username = ""
        self._scope= "user-top-read"
        self.token = util.prompt_for_user_token(self._username, self._scope,client_id='142e222ba0344943951ef655795a5018',client_secret='a5202e52b9e54a9880224356d146bc2b',redirect_uri='http://localhost/')
    
    def get_playlist(self):

        if self.token:
            sp = spotipy.Spotify(auth=self.token)
            results = sp._get('me/top/tracks', limit=100)
            tracks = []
            for res in results['items']:
                name = res['name']
                artist = res[u'artists'][0]['name']
                uri = res["external_urls"]["spotify"]
                artist_uri = res[u'artists'][0]['id']
                artist_data = sp._get('artists/'+artist_uri, limit=100)
                genre = artist_data['genres']
                
                tracks.append(Track(name, artist, uri, artist_uri, artist_data, genre))

            return tracks

        else:
            return None

    def search_artist(self, search_str):
        
        if self.token:
            sp = spotipy.Spotify(auth=self.token)
            results = sp.search(search_str, type='artist')

            if len(results['artists']['items']) > 0:
                name = results['artists']['items'][0]['name']
                uri = results['artists']['items'][0]['external_urls']['spotify']  
                genres = results['artists']['items'][0]['genres']
                return Artist(name, uri, genres)
            else:
                return None
        else:
            return null