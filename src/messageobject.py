from pattern.en import parse
from pattern.en import parsetree
from textblob import TextBlob
from textblob.np_extractors import ConllExtractor

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

def split_into_sentences(text):
	return TextBlob(text).sentences

def split_into_words(sentence):
	return TextBlob(sentence).words

def get_words_pos(sentence):
	words=split_into_words(sentence)
	tree=get_parse_tree(sentence)
	return words,tree

def get_nouns(sentence):
	pos=get_parse_tree(sentence)
	nouns=[]
	for chunk in pos:
		for word in chunk:
			if word.tag[0] == 'N':
				nouns.append(word)
	return nouns

def get_verbs(sentence):
	pos=get_parse_tree(sentence)
	verbs=[]
	for chunk in pos:
		for word in chunk:
			if word.tag[0] == 'V' or word.tag[0] == 'M':
				verbs.append(word)
	return verbs

def get_adjectives(sentence):
	pos=get_parse_tree(sentence)
	adjectives=[]
	for chunk in pos:
		for word in chunk:
			if word.tag[0] == 'J':
				adjectives.append(sentence)

def get_noun_phrase(sentence):
	extractor=ConllExtractor()
	blob=TextBlob(sentence,np_extractor=extractor)
	print blob.noun_phrases

