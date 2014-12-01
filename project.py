from comment_thread import Thread
from itertools import chain
from sys import argv

# declared globally so it can be inspected with python -i
thread = None
def main(args):
	global thread
	
	thread = Thread(args['i'])

	thread.tag_traits()

	thread.train_and_test()

	




# Turn args into a readable dictionaryxx
def process_args(args):
	while args[0][-3:] != '.py':
		args = args[1:]

	vals = {}
	key = None
	for arg in args:
		if arg[0] == '-':
			# Remove dashes from keys
			key = arg[1:]
			vals[key] = True

		else:
			vals[key] = arg
	return vals

if __name__ == '__main__':
	main(process_args(argv))