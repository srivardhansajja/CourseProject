from types import ClassMethodDescriptorType
import numpy as np
import json
from collections import Counter


def read_physical_model():
    with open("model_deploy/model.json", "r") as fp:
        data = json.load(fp)
    positive_words = Counter(data["positives"])
    mean_len = data["mean_len"]
    std_dev = data["std_dev"]
    return positive_words, mean_len, std_dev


def classify(postive_words, dev_set, mean_len, std_dev):

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


def model_deploy(unfiltered_urls):

    model, mean_len, std_dev = read_physical_model()

    labels = classify(model, unfiltered_urls, mean_len, std_dev)

    filtered_list = list()
    for i in range(len(unfiltered_urls)):
        if labels[i] == 1:
            filtered_list.append(unfiltered_urls[i])

    # apply model, and filter out unwanted urls
    #filtered_list = unfiltered_urls  # comment out line

    return filtered_list
