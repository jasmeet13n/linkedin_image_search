"""
===================================================
Faces recognition example using eigenfaces and SVMs
===================================================

The dataset used in this example is a preprocessed excerpt of the
"Labeled Faces in the Wild", aka LFW_:

  http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz (233MB)

.. _LFW: http://vis-www.cs.umass.edu/lfw/

Expected results for the top 5 most represented people in the dataset::

                   precision    recall  f1-score   support

     Ariel Sharon       0.67      0.92      0.77        13
     Colin Powell       0.75      0.78      0.76        60
  Donald Rumsfeld       0.78      0.67      0.72        27
    George W Bush       0.86      0.86      0.86       146
Gerhard Schroeder       0.76      0.76      0.76        25
      Hugo Chavez       0.67      0.67      0.67        15
       Tony Blair       0.81      0.69      0.75        36

      avg / total       0.80      0.80      0.80       322

"""
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

pca = joblib.load('my_pca.pkl')
clf = joblib.load('my_model.pkl')
target_names = joblib.load('target_names.pkl')

X=load_one_image(["/home/jasmeet/scikit_learn_data/lfw_home/lfw_funneled/Colin_Powell/pic1.jpg"], slice_=None, color=False, resize=0.4)

X_pca = pca.transform(X)
y_pred = clf.predict(X_pca)

print(str(y_pred))
print(target_names[y_pred[0]])

#print(classification_report(y, y_pred, target_names=target_names))
#print(confusion_matrix(y, y_pred, labels=range(n_classes)))
