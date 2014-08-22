import nltk
import os
from os import listdir

stopwords = nltk.corpus.stopwords.words('portuguese')

for category in listdir('articles'):
	in_path = 'articles/'+ category
	out_path = 'swf_articles/'+ category

	if not os.path.exists(out_path):
		os.makedirs(out_path)

	for article in listdir(in_path):
		f_in = file(in_path+'/'+article, 'r')
		f_out = file(out_path+'/'+article, 'wt')

		for line in f_in.readlines():
			#print(" ".join(filter(lambda word: len(word) <= 1, line.split())))
			f_out.write(" ".join(filter(lambda word: word not in stopwords and len(word) > 1, line.split())))

		f_out.close()
		print(article+" printed!")
		break
	break

