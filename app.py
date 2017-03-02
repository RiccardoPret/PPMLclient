from flask import Flask, request, jsonify
import pandas
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
import pickle

import urllib.request


app = Flask(__name__)

def permListify(s_perms):
	#multiple apps list permissions
	ps=[]
	for p in s_perms.split(','):
		tmp=[]
		for sp in p:
			#permissions of single app
			tmp.append(sp)
		ps.append(tmp)
	return ps

@app.route('/')
def hello():
	all_args = request.args.to_dict()
	try:
		perm=all_args['perm']
	except:
		return "Incorrect URL"

	permlist = permListify(perm)
	for app_perm in permlist:
		if len(app_perm) != 20:
			return "Incorrect permission"

	# Get the classifier
	response = urllib.request.urlopen("https://rikyupl.000webhostapp.com/clf.pickle")
	data = response.read()
	clf = pickle.loads(data)

	# Predict the result
	prediction=clf.predict(permlist)
	result=""
	for r in prediction:
		result = result + str(r) + ','
	return str(result[:-1])

if __name__ == '__main__':
	app.run()