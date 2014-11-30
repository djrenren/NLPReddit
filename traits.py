def comment_length(comment, parent_traits):
	return [('length', len(comment.body))]


trait_functions = [comment_length]


def get_all_traits(comment, parent_traits=[]):
	return [trait for f in trait_functions for trait in f(comment, parent_traits)]