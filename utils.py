import json

class Utils:

	def serialize_list(self, dictList):
		listOfDicts = "["

		for i in range(len(dictList)):
			listOfDicts += json.dumps(dictList[i].serialize())
			if i < (len(dictList) - 1):
				listOfDicts += ","

		listOfDicts += "]"

		return listOfDicts
