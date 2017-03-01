from flask import Flask
import pandas
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pickle

import urllib.request


app = Flask(__name__)

@app.route('/')
def hello():
	
	#Get the dataset
	features = urllib.request.urlopen("https://rikyupl.000webhostapp.com/features.txt")
	dataset= pandas.read_csv(features)

	#Split the features from the label
	X = np.array(dataset.drop(['label'], 1))
	y = np.array(dataset['label'])
	
	response = urllib.request.urlopen("https://rikyupl.000webhostapp.com/clf.pickle")
	data = response.read()
	clf = pickle.loads(data)

	accuracy = clf.score(X, y)
	return str(accuracy)

if __name__ == '__main__':
    app.run()