from pattern.en import parse

def tag_sentence(sentence):
	return parse(sentence,relations=True,lemmata=True)

print tag_sentence("The boy goes to school everyday")