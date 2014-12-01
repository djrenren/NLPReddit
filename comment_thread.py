from comment import Comment
from traits import get_all_traits
from json import loads as load_json
from random import shuffle
from math import ceil
from nltk import NaiveBayesClassifier
from nltk.classify import accuracy

class Thread:

	def __init__(self, fname):
		data = load_json(open(fname).read())

		topic = Comment(data[0]['data']['children'][0])

		comments = [Comment(c) for c in data[1]['data']['children'] if 'body' in c['data']]

		topic.children = comments

		self.comment_tree = topic
		self.comment_list = flatten_comment_tree(self.comment_tree)


	def tag_traits(self, comment=None, parent_traits={}):

		if comment == None:
			comment = self.comment_tree

		comment.traits = get_all_traits(comment, parent_traits)
		for child in comment.children:
			self.tag_traits(child, comment.traits)


	def train_and_test(self, num_folds=10):
		shuffle(self.comment_list)

		fold_size = int(ceil(len(self.comment_list) / float(num_folds)))

		folds = []
		for i in range(num_folds):
			start = i * fold_size
			end = (i+1) * fold_size

			if end > len(self.comment_list):
				end = len(self.comment_list)

			train_comments = self.comment_list[:start] + self.comment_list[end:]
			test_comments = self.comment_list[start:end]

			train_set = data_set(train_comments)
			test_set = data_set(test_comments)

			classifier = NaiveBayesClassifier.train(train_set)

			print accuracy(classifier, test_set)




def data_set(comment_list):
	return [(c.traits, 1 if c.score > 0 else 0) for c in comment_list]

def flatten_comment_tree(comment, comment_list=[]):
	comment_list.append(comment)
	for child in comment.children:
		comment_list = flatten_comment_tree(child, comment_list)
	return comment_list