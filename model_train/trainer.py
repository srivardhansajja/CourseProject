import numpy as np
from collections import Counter
import re
import math 

word1  = Counter()
word0 = Counter()


def train(train_set : list, train_labels : list) :

    arr = [len(train_set[i]) for i in range(len(train_set)) if train_labels[i] == 1]
    arr = np.array(arr)

    mean_len = np.mean(arr)
    std_dev = np.std(arr)

    print(mean_len)
    print(std_dev)

    num_word0 = 0
    num_word1 = 0

    for url, label in zip(train_set, train_labels):
        url = "/".join(url.split("/")[3:])
        #print(url)
        words = re.split("/|-|:|\.|=|\?", url)
        #print(words)
        
        for word in words:
            if (word == ''):
                continue
            if (label == 1):
                temp = word.lower()
                word1.update([temp])
                num_word1 += 1
            elif (label == 0):
                temp = word.lower()
                word0.update([temp])
                num_word0 += 1

    
           

    return None, num_word0, num_word1

    
   

def test(model : None, dev_set : list, num_word0 : int, num_word1 : int ) -> list:
    # import random
    # return [random.randint(0,1) for _ in dev_set]


    toret = np.ones(len(dev_set))

    word0_prob = []
    word1_prob = []

    for i in range(len(dev_set)):
        
        url = dev_set[i]
        url = "/".join(url.split("/")[3:])
        words = re.split("/|-|:|\.|=|\?", url)
        for word in words:
            if (word == ''):
                continue
            param = 65
            word0_prob.append((word0[word]+ param)/(num_word1+ param * (len(word0) + len(word1))))
            word1_prob.append((word1[word]+ param)/(num_word0+ param * (len(word0) + len(word1))))

        prob1 = 0
        prob0 = 0

        for prob in word1_prob:
            prob1 += math.log10(prob)

        for prob in word0_prob:
            prob0 += math.log10(prob)

        #print(prob0, " ", prob1)
        if (prob0 > prob1):
            toret[i] = 0
   
    #print(toret)

    return toret 
# ==========================================================================================================================
# import numpy as np

# mean_len = 0
# std_dev = 0

# def train(train_set : list, train_labels : list) :

#     arr = [len(train_set[i]) for i in range(len(train_set)) if train_labels[i] == 1]
#     arr = np.array(arr)

#     mean_len = np.mean(arr)
#     std_dev = np.std(arr)

#     print(mean_len)
#     print(std_dev)

#     # for i in range(len(train_set)):
#     #     if (train_labels[i] == 1):
#     #         train_labels.split

#     return None, mean_len, std_dev

    
   

# def test(model : None, dev_set : list, mean_len : float, std_dev : float ) -> list:
#     # import random
#     # return [random.randint(0,1) for _ in dev_set]

#     toret = np.zeros(len(dev_set))

#     for i in range(len(dev_set)):
#         if (dev_set[i].endswith('/')):
#             dev_set[i] = dev_set[i][:-1]
#         if (dev_set[i].endswith('.html')):
#             dev_set[i] = dev_set[i][:-5]
#         if (dev_set[i].endswith('.shtml')):
#             dev_set[i] = dev_set[i][:-6]
#         if (dev_set[i].endswith('.php')):
#             dev_set[i] = dev_set[i][:-4]
#         if (dev_set[i].endswith('?')):
#             dev_set[i] = dev_set[i][:-1]
        
#         if (dev_set[i].endswith("faculty")):
#             toret[i] = 1
#         if (dev_set[i].endswith("directory")):
#             toret[i] = 1
#         if (dev_set[i].endswith("staff")):
#             toret[i] = 1
#         if (dev_set[i].endswith("people")):
#             toret[i] = 1
#         if (dev_set[i].endswith("lecturers")):
#             toret[i] = 1


#         if ("department" in dev_set[i] != -1):
#             toret[i] = 1

#         if (np.absolute(len(dev_set[i]) - mean_len) <  std_dev/25):
#             toret[i] = 1
    

#     return toret 
   