from nltk.corpus import wordnet as wn

def allSpecialNouns():
	nounZeroHyponyms = []
	nounLems = []

	for synset in list(wn.all_synsets('n')):
		if (len(synset.hyponyms()) is 0 and
		len(wn.synsets(synset.lemmas()[0].name())) < 3):
			nounZeroHyponyms.append(synset)

	for synset in nounZeroHyponyms:
		lemma = synset.lemmas()[0]
		if '_' not in lemma.name():		# Remove this line to include phrases
			nounLems.append(lemma)

	nounOut = open("noun_lemmas_counts.tsv", 'w')
	for lemma in nounLems:
		nounOut.write(lemma.name() + "\t" + str(lemma.count()) + "\n")


def allSpecialVerbs():
	verbZeroHyponyms = []
	verbLems = []

	for synset in list(wn.all_synsets('v')):
		if (len(synset.hyponyms()) is 0 and
		len(wn.synsets(synset.lemmas()[0].name())) < 3):
			verbZeroHyponyms.append(synset)

	for synset in verbZeroHyponyms:
		lemma = synset.lemmas()[0]
		if '_' not in lemma.name():		# Remove this line to include phrases
			verbLems.append(lemma)

	verbOut = open("verb_lemmas_counts.tsv", 'w')
	for lemma in verbLems:
		verbOut.write(lemma.name() + "\t" + str(lemma.count()) + "\n")


def allSpecialAdvs():
	advZeroHyponyms = []
	advLems = []

	for synset in list(wn.all_synsets('r')):
		if (len(synset.hyponyms()) is 0 and
		len(wn.synsets(synset.lemmas()[0].name())) < 3):
			advZeroHyponyms.append(synset)

	for synset in advZeroHyponyms:
		lemma = synset.lemmas()[0]
		if '_' not in lemma.name():		# Remove this line to include phrases
			advLems.append(lemma)

	advOut = open("adv_lemmas_counts.tsv", 'w')
	for lemma in advLems:
		advOut.write(lemma.name() + "\t" + str(lemma.count()) + "\n")


def allSpecialAdjs():
	adjZeroHyponyms = []
	adjLems = []

	for synset in list(wn.all_synsets('s')):
		if (len(synset.hyponyms()) is 0 and
		len(wn.synsets(synset.lemmas()[0].name())) < 3):
			adjZeroHyponyms.append(synset)

	for synset in adjZeroHyponyms:
		lemma = synset.lemmas()[0]
		if '_' not in lemma.name():		# Remove this line to include phrases
			adjLems.append(lemma)

	adjOut = open("adj_lemmas_counts.tsv", 'w')
	for lemma in adjLems:
		adjOut.write(lemma.name() + "\t" + str(lemma.count()) + "\n")


if __name__ == '__main__':
	allSpecialNouns()
	allSpecialVerbs()
	allSpecialAdvs()
	allSpecialAdjs()
