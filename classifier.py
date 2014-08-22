import numpy as np
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.feature_selection import SelectPercentile, chi2
from sklearn.multiclass import OneVsRestClassifier
from sklearn.datasets import load_files
from sklearn.pipeline import Pipeline
from sklearn.svm import LinearSVC
from sklearn import cross_validation
import codecs
import nltk
import os

stopwords = nltk.corpus.stopwords.words('portuguese')
fs = load_files('articles/')

f = file("articles/Transito/111574710")

X_train, X_test, y_train, y_test = cross_validation.train_test_split(fs.data, fs.target, test_size=0.4, random_state=0)

classifier = Pipeline([('vect', CountVectorizer(stop_words=stopwords)),
						('tfidf', TfidfTransformer()),
						('fs', SelectPercentile(chi2, percentile=50)),
						('clf', SVC(kernel="linear", probability=True, )),
])

#ovr = OneVsRestClassifier(classifier).fit(X_train, y_train)
#r = ovr.decision_function([f.readlines()[0]])
#print(r)

classifier.fit(X_train, y_train)

directory = "articles"

while True:

	command = raw_input(">> ")
	if command == 'exit':
		break
	elif command in ('ls'):
		print(os.listdir(directory))
	elif command in ('dir'):
		print(directory)
	elif command == '..':
		directory = "/".join(directory.split("/")[:-1])
	else:
		aux = directory +'/'+ command
		if os.path.isdir(aux):
			directory = aux
		elif os.path.isfile(aux):
			f = codecs.open(aux, encoding='utf-8')
			print(classifier.predict_proba(" ".join(f.readlines())))
		else:
			print("invalid command line")


#scores = classifier.predict_proba(X_test)

#print("done!")

#r = classifier.predict_proba([f.readlines()[0]])
#print(r)

#import pdb; pdb.set_trace()

#classifier.fit(X_train, y_train)
#print(classifier.get_params())

#scores = cross_validation.cross_val_score(classifier, fs.data, fs.target, cv=4, scoring='f1')

#print(scores)
#print("Accuracy: %0.2f (+/- %0.2f)" % (scores.mean(), scores.std() * 2))


#print("Train: "+X_train.shape+" "+y_train.shape)
#print("Test: "+X_test.shape+" "+y_test.shape)

#print(len(X_train))
#print(len(y_train))
#print(len(X_test))
#print(len(y_test))

#classifier.fit(X_train, y_train)
#print(classifier.score(X_test, y_test))

#predicted = classifier.predict(X_test, y_test)
#np.mean(predicted == )

#vec = CountVectorizer(stop_words=stopwords)

#f = file("articles/Transito/111574710")


#print(fs)
#print(dir(fs))

#counts = vec.fit_transform(fs.data)
#print(counts.shape)

