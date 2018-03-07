import glob
import numpy as np
import constant


REFINED_TRAIN_PATH = "../../server/data/refined/train/"
REFINED_TEST_PATH = "../../server/data/refined/test/"


def load_data():

    train_x = [] # 10,10,10 * 10,10 -> 10,2 * 5
    train_y = []

    for filename in glob.glob(REFINED_TRAIN_PATH + "*"):
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            tokens = line.split(",")
            tokens = list(map(np.float32, tokens))
            train_y.append(int(tokens.pop()))
            item = parse_tokens(tokens)
            train_x.append(item)

    test_x = []
    test_y = []
    for filename in glob.glob(REFINED_TEST_PATH + "*"):
        file = open(filename, "r")
        lines = file.readlines()
        file.close()
        for line in lines:
            tokens = line.split(",")
            tokens = list(map(np.float32, tokens))
            test_y.append(int(tokens.pop()))
            item = parse_tokens(tokens)
            test_x.append(item)

    return (np.asarray(train_x), np.asarray(train_y)), (np.asarray(test_x), np.asarray(test_y))


def parse_tokens(tokens):
    tokens = np.array(tokens)
    tokens = np.reshape(tokens, (int(constant.FEATURE_SIZE * 10 / 2), 2))

    index = 10
    first = tokens[0:10, :]
    for i in range(4):
        target = tokens[index:index+10, :]
        first = np.concatenate((first, target), axis=1)
        index += 10
    second = tokens[index:index+10, :]
    for i in range(4):
        target = tokens[index:index+10, :]
        second = np.concatenate((second, target), axis=1)
        index += 10
    thrid = tokens[index:index+10, :]
    for i in range(4):
        target = tokens[index:index+10, :]
        thrid = np.concatenate((thrid, target), axis=1)
        index += 10

    result = np.concatenate((first,second), axis=0)
    result = np.concatenate((result,thrid), axis=0)
    return result.flatten()

