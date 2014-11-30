from comment import Comment
from traits import get_all_traits
from json import loads as load_json

class Thread:

	def __init__(self, fname):
		data = load_json(open(fname).read())

		topic = Comment(data[0]['data']['children'][0])

		comments = [Comment(c) for c in data[1]['data']['children'] if 'body' in c['data']]

		topic.children = comments

		self.comment_tree = topic
		self.comment_list = flatten_comment_tree(self.comment_tree)


	def tag_traits(self, comment=None, parent_traits=[]):

		if comment == None:
			comment = self.comment_tree

		comment.traits = get_all_traits(comment, parent_traits)
		for child in comment.children:
			self.tag_traits(child, comment.traits)


	def train(self):
		pass

	def predict(self):
		pass	

def flatten_comment_tree(comment, comment_list=[]):
	comment_list.append(comment)
	for child in comment.children:
		comment_list = flatten_comment_tree(child, comment_list)
	return comment_list