import argparse
import tensorflow as tf
import numpy as np
import datetime
import predictor
import json

def get_state(pred):
    label = pred['label']
    if label == 0:
        return 0
    elif label == "-0" or label < 0:
        return -1
    else:
        return 1


def main(argv):

    date = "20180226"

    file = open("../server/data/" + date, "r")
    lines = file.readlines()
    file.close()

    for i in range(len(lines)):
        line = lines[i]
        tokens =  line.split(",")
        time = tokens[0]
        result = predictor.predict(date, time)
        if result.startswith("{"):
            pred = json.loads(result)
            price = tokens[11]
            state = get_state(pred)
            print(time, " ", price, " ", state)

    # print("Target file : " , today)
    # print(predict(date, time))




if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.FATAL)
    tf.app.run(main)
