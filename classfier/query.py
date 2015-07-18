# -*- coding: UTF-8 -*-

from __future__ import print_function

from time import time
import logging
import matplotlib.pyplot as plt

from sklearn.cross_validation import train_test_split
from sklearn.datasets import fetch_lfw_people
from sklearn.grid_search import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.decomposition import RandomizedPCA
from sklearn.svm import SVC
from sklearn.externals import joblib
from fetch_data import load_one_image

# Display progress logs on stdout
logging.basicConfig(level=logging.INFO, format='%(asctime)s %(message)s')

pca = ''
clf = ''
target_names = ''

def loadModel():
  pca = joblib.load('my_pca.pkl')
  clf = joblib.load('my_model.pkl')
  target_names = joblib.load('target_names.pkl')
  #return pca, clf, target_names

def queryModel(img_path=None):
  #pca, clf, target_names = loadModel()
  if img_path == None:
    img_path = "/home/jasmeet/test.jpg"
  X=load_one_image([img_path], slice_=None, color=False, resize=0.4)
  X_pca = pca.transform(X)
  y_pred = clf.predict(X_pca)

  print(str(y_pred))
  print(target_names[y_pred[0]])

loadModel()
queryModel()
