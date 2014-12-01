from nltk.util import ngrams

def comment_length(comment, parent_traits):
	return {'length': len(comment.body)}

def trigrams(comment, parent_traits):
	traits = {}
	for t in ngrams(comment.body, 3):
		if t in parent_traits:
			if 'shared_grams' in traits:
				traits['shared_grams'] += 1
			else:
				traits['shared_grams'] = 0
		traits[t] = True
	return traits



trait_functions = [comment_length, trigrams]



def get_all_traits(comment, parent_traits):
	traits = {}
	for f in trait_functions:
		traits.update(f(comment, parent_traits))
	return traits
