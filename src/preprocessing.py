from pattern.en import parse
from pattern.en import parsetree

def tag_sentence(sentence):
	return parse(sentence,relations=True,lemmata=True)

def get_parse_tree(sentence):
	tree=[]
	Tree=[]
	for sentence in parsetree(sentence):
		for chunk in sentence.chunks:
			for word in chunk.words:
				tree.append(word)
			Tree.append(tree)
			tree=[]
	return Tree

print get_parse_tree("The boy is a very good artist")