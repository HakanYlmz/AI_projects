
from abc import ABCMeta, abstractmethod

import random
import json
import pickle
import numpy as np
import os



import nltk
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import SGD
from tensorflow.keras.models import load_model

print("h")