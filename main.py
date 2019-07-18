import pprint
import sys
import spotipy
import spotipy.util as util
import mel

from track import Track
from spotify_utils import Spotify_Utils
from predict_utils import Predict_Utils

spot_utils = Spotify_Utils()

#get events
predict_utils = Predict_Utils()
events = predict_utils.get_concerts('10km@41.3948976,2.0787279,12', '2019-07-19T00:00:00+0200', '2019-07-21T00:00:00+0200')

# event_artists = []

# for event in events:

# 	#print(event.title)

# 	event_artist = spot_utils.search_artist(event.title)

# 	if event_artist is None:
# 		event_title = event.title
# 		mel_artists = mel.get_artists(event_title)
# 		for event_title in mel_artists:
# 			event_artist = spot_utils.search_artist(event_title)

# 			if event_artist is not None:
# 				event_artists.append(event_artist)
# 				#print('-' + event_artist.name)
# 				event.artist = event_artist	
# 				break

# for event in events:
# 	print(event.title)
# 	if event.artist is not None:
# 		print("-" + event.artist.name)

# tracks = spot_utils.get_playlist()

# rec_events = []

# for env in events:
# 	if env.artist is not None:
# 		for genre_art in env.artist.genres:
# 			#print('art-' + genre_art)
# 			for track in tracks:
# 				for genre_track in track.genre:
# 					#print('track-' + genre_track)
# 					if genre_art == genre_track:
# 						print('MATCH:' + env.title + " - " + track.artist)
# 						rec_events.append(env)
# 						break

# for rec_ev in rec_events:
# 	print(rec_ev.name)

