class Event:

	artist = None

	def __init__(self, id, title, category, labels, rank, start, end, location, address, state):
		self.id = id
		self.title = title
		self.category = category
		self.labels = labels
		self.rank = rank
		self.start = start
		self.end = end
		self.location = location
		self.address = address
		self.state = state

	def serialize(self):
		return {'id': self.id,
        	'title': self.title,
        	'category': self.category,
        	'labels': self.labels,
        	'rank': self.rank,
        	'start': str(self.start.year) + '/' + str(self.start.month) + '/' + str(self.start.day) + " " + str(self.start.hour) + ":" + str(self.start.minute),
        	'end': str(self.end.year) + '/' + str(self.end.month) + '/' + str(self.end.day) + " " + str(self.end.hour) + ":" + str(self.end.minute),
        	'location': self.location,
        	'address': self.address,
        	'state': self.state
        }