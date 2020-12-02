from types import ClassMethodDescriptorType


def read_physical_model():
    f = open("model", "r")
    pass


def classify(model, dev_set):
    pass


def model_deploy(unfiltered_urls):

    # model = read_physical_model()

    # labels = classify(model, unfiltered_urls)

    # filtered_list = list()
    # for i in range(len(unfiltered_urls)):
    #     if labels[i] == 1:
    #         filtered_list.append(unfiltered_urls[i])

    # apply model, and filter out unwanted urls
    filtered_list = unfiltered_urls  # comment out line

    return filtered_list