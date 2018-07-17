#!/Users/dianaha/anaconda3/bin/python

# coding: utf-8

# In[ ]:


import numpy as np
import pandas as pd
import math
from sklearn.model_selection import train_test_split

from keras.models import load_model
from keras import backend as K
from keras import optimizers
from keras import losses
from keras.models import Sequential
from keras.layers import Dense, Activation, Flatten
from keras.utils import to_categorical
from keras.layers import Dropout
from keras.layers import Convolution2D, MaxPooling2D

import tensorflow as tf

import os
from PIL import Image
import cv2
import h5py
import glob


# In[ ]:


# get file paths for each png image in the folder
waffs_imgs = sorted(glob.glob("./WAFFLES/*.png", recursive=True))


# In[ ]:


# create empty df and list for labels
waffs_df = pd.DataFrame()


# In[ ]:


# add images as arrays to waffs_df
start = 0

for i in waffs_imgs:  
    img = cv2.imread(i, 0)
    re = cv2.resize(img, (28, 28))
    arr = np.asarray(re).ravel()
    waffs_df = waffs_df.append([arr], ignore_index=True)


# In[ ]:


# format the data in order to load into the model
waffs_df = waffs_df.values.reshape(waffs_df.shape[0], 28, 28, 1)
waffs_df = waffs_df.astype('float32')
waffs_df /= 255


# In[ ]:


# load keras model
model1 = load_model("model1.h5")


# In[ ]:


# make predictions; ouput is a number
waffs_preds = model1.predict_classes(waffs_df)


# In[ ]:


# dictionary used to convert numerical values to English alphabet
letter_dict = {0:"A", 1:"B", 2:"C", 3:"D", 4:"E", 5:"F", 
               6:"G", 7:"H", 8:"I", 10:"K", 11:"L", 12:"M", 
               13:"N", 14:"O", 15:"P", 16:"Q", 17:"R", 18:"S",
               19:"T", 20:"U", 21:"V", 22:"W", 23:"X", 24:"Y"}


# In[ ]:

# change output from numbers to a single string of alphabets
translation = "".join(list(map(lambda key: letter_dict[key], waffs_preds)))
print(translation)


# # create function to change output from numbers to a single string of alphabets
# def translate_num2let(waffs_preds):
#     translation = "".join(list(map(lambda key: letter_dict[key], waffs_preds)))
#     return translation


# # In[ ]:


# translate_num2let(waffs_preds)

