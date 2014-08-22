import nltk
import os
from os import listdir
import codecs

stemmer = nltk.stem.RSLPStemmer()

for category in listdir('articles'):
	in_path = 'swf_articles/'+ category
	out_path = 'stmd_articles/'+ category

	if not os.path.exists(out_path):
		os.makedirs(out_path)

	for article in listdir(in_path):
		f_in = codecs.open(in_path+'/'+article, encoding='utf-8')
		f_out = codecs.open(out_path+'/'+article, 'wt', encoding='utf-8')

		for line in f_in.readlines():
			f_out.write(" ".join(map(stemmer.stem, line.split())))

		f_out.close()
		print(article+" printed!")

