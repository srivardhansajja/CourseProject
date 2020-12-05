import numpy as np
from collections import Counter
import re
import math 


def train(train_set, train_labels):

    arr = np.zeros(train_labels.count(1))
    postive_words = Counter()

    index = 0 

    for url, label in zip(train_set, train_labels):

        if (label == 1):
            arr[index] = len(url)
            index += 1

        url = "/".join(url.split("/")[3:])
        words = re.split("/|-|:|\.|=|\?", url)
        
        for word in words:
            if (word == ''):
                continue
            if (label == 1):
                temp = word.lower()
                postive_words.update([temp])
                

    mean_len = np.mean(arr)
    std_dev = np.std(arr)
            
    return postive_words, mean_len, std_dev


def test(postive_words, dev_set, mean_len, std_dev):

    predicted_labels = np.zeros(len(dev_set))

    trim = {'/', '?', '.php','.html','.shtml'}

    for i in range(len(dev_set)):

        for elem in trim:
            if dev_set[i].endswith(elem):
                dev_set[i] = dev_set[i][:-len(elem)]
     
        for j in range(6):
            if (dev_set[i].endswith(postive_words.most_common(6)[j][0])):
                predicted_labels[i] = 1

        for j in range(7, 10):
            if ((postive_words.most_common(11)[j][0]) in dev_set[i]):
                predicted_labels[i] = 1

        if (np.absolute(len(dev_set[i]) - mean_len) <  std_dev/25):
            predicted_labels[i] = 1
    

    return predicted_labels 
   