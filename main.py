# main.py
import numpy as np
from sklearn.linear_model import LogisticRegressionCV
import matplotlib.pyplot as plt
from sklearn.linear_model import LogisticRegressionCV as LogReg
from sklearn.metrics import roc_curve
from sklearn.metrics import confusion_matrix, classification_report, precision_score
import pandas as pd

# Load the data

labelled_data = pd.read_csv('AllBooks_baseline_DTM_Labelled.csv')
unlabelled_data = pd.read_csv('AllBooks_baseline_DTM_Unlabelled.csv')

