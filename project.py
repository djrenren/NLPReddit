import json
from comment import Comment
from itertools import chain


def comment_length(comment, parent_traits):
	return [('length', len(comment.body))]

trait_functions = [comment_length]


def get_traits(comments, parent_traits=[]):
	for comment in comments:
		comment.traits = list(chain.from_iterable([f(comment, parent_traits) for f in trait_functions]))
		get_traits(comment.children, comment.traits)


def main():
	a = json.loads(open('data/portugal.json').read())

	comments = [Comment(c) for c in a[1]['data']['children'] if 'body' in c['data']]

	get_traits(comments)




if __name__ == '__main__':
	main()