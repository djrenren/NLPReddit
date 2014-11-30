from re import compile as regex

non_alpha = regex("[^-a-z0-9']")
spaces = regex("\s+")

class Comment:

	def __init__(self, json):
		data = json['data']
		self.raw_body = data['body'] if 'body' in data else data['selftext']
		if 'children' in data:
			self.children = [Comment(child) for child in data['children'] if 'data' in child and 'body' in child['data']]
		else:
			self.children = []
		self.score = data['score']
		self._normalize()

	def _normalize(self):	
		self.body = spaces.sub(' ', non_alpha.sub(' ', self.raw_body.lower())).split() or []	