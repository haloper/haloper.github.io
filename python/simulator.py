import argparse
import tensorflow as tf
import numpy as np
import datetime
import predictor
import json


money = 1000000
stock = 0
count = 0
fee = 0


def buy(value):
    global money, stock, count, fee
    money = money - int(value)
    stock = stock + int(value)
    count += 1
    fee += float(value) * 0.001


def sell(value):
    global money, stock, count, fee
    money = money + int(value)
    stock = 0
    count += 1
    fee += float(value) * 0.001


def get_state(pred):
    label = pred['label']
    if label == 0:
        return 0
    elif label == "-0" or label < 0:
        return -1
    else:
        return 1


def process_result(tokens, time, result):
    if not result.startswith("{"):
        return
    pred = json.loads(result)
    price = tokens[11]
    state = get_state(pred)
    print(time, " ", price, " ", state)

    if state >= 0 and stock == 0:
        buy(price)
    elif state < 0 and stock > 0:
        sell(price)

    print("money : ", money, ", count : ", count, ", fee : ", fee)


def main(argv):

    date = "20180227"

    file = open("../server/data/" + date, "r")
    lines = file.readlines()
    file.close()

    for i in range(len(lines)):
        line = lines[i]
        tokens =  line.split(",")
        time = tokens[0]
        result = predictor.predict(date, time)
        process_result(tokens, time, result)



    # print("Target file : " , today)
    # print(predict(date, time))




if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.FATAL)
    tf.app.run(main)
