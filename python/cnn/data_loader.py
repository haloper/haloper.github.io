import pandas as pd
import tensorflow as tf
import glob


REFINED_TRAIN_PATH = "../server/data/refined/train/"
REFINED_TEST_PATH = "../server/data/refined/test/"


def load_data(y_name='label'):

    train_x = [] # 10,10,10 * 10,10 -> 10,2 * 5
    train_y = []

    for file in glob.glob(REFINED_TRAIN_PATH + "*"):
        if len(train_y) == 0:
            train = pd.read_csv(file, names=csv_column_names, header=0)
        else :
            train.append(pd.read_csv(file, names=csv_column_names, header=0))

    train_x, train_y = train, train.pop(y_name)


load_data()