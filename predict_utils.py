import predicthq
from predicthq.endpoints.schemas import DateTimeRange

from predicthq import Client
from event import Event

class Predict_Utils:

	def __init__(self):
		self.phq = Client(access_token = "NHcF5B9PiMCeCrhWENWuRB9SDtSxSB")

	def get_concerts(self, gps_coords, start_date, end_date):

		dt = DateTimeRange()
		dt.gte = start_date
		dt.lte = end_date 

		events = []

		for res in self.phq.events.search(category="concerts", within=gps_coords, limit=50, start=dt):
			id = res['id']	
			title = res['title']
			category = res['category']
			labels = res['labels']
			rank = res['rank']
			start = res['start']
			end = res['end']
			location = res['location']
			state = res['state']
			events.append(Event(id, title, category, labels, rank, start, end, location, state))

		return events

class HqDate:
	def __init__(self, gte, lte):
		self.name = name
		self.uri = uri
		self.genres = genres