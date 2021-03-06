import numpy as np
from trainer import train, test
import json


def load_data():
    train_set = list()
    train_labels = list()
    dev_set = list()
    dev_labels = list()
    
    train_data = open('train_data.txt').readlines()
    for line in train_data:
        label, url = line[:-1].split(" ")
        train_set.append(url)
        train_labels.append(int(label))

    dev_data = open('dev_data.txt').readlines()
    for line in dev_data:
        label, url = line[:-1].split(" ")
        dev_set.append(url)
        dev_labels.append(int(label))

    return train_set, train_labels, dev_set, dev_labels


"""
print_statistics - Citation: Taken from UofI ECE448/CS440 MP3: Naive Bayes' starter 
                    code for calculation of accuracy, precision, f1_score and recall
"""
def print_statistics(predicted_labels, dev_labels):

    yhats = np.array(predicted_labels)
    dev_labels = np.array(dev_labels)
    accuracy = np.mean(yhats == dev_labels)
    #accuracy = np.mean([yhats[i] == dev_labels[i] for i in range(len(yhats))])
    tp = np.sum([yhats[i] == dev_labels[i] and yhats[i] == 1 for i in range(len(yhats))])
    precision = tp / np.sum([yhats[i] == 1 for i in range(len(yhats))])
    recall = tp / (np.sum([yhats[i] != dev_labels[i] and yhats[i] == 0 for i in range(len(yhats))]) + tp)
    f1 = 2 * (precision * recall) / (precision + recall)

    print("Accuracy:",accuracy)
    print("F1-Score:",f1)
    print("Precision:",precision)
    print("Recall:",recall)


def create_physical_model(model, mean_len, std_dev):
    jsondata = {"positives":model, "mean_len":mean_len, "std_dev": std_dev}
    with open("../model_deploy/model_testing.json", "w") as fp:
        json.dump(jsondata, fp)
    


def main():

    train_set, train_labels, dev_set, dev_labels = load_data()

    model, mean_len, std_dev = train(train_set, train_labels)

    prediction = test(model, dev_set, mean_len, std_dev)
    
    print_statistics(prediction, dev_labels)

    create_physical_model(model, mean_len, std_dev)


if __name__ == "__main__":
    main()
