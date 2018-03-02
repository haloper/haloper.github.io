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
before_value = 0
before_money = 0
success_cnt = 0
fail_cnt = 0


def buy(value):
    global money, stock, count, fee
    print("buy : ", value)
    money = money - int(value)
    stock = stock + int(value)
    count += 1
    fee += float(value) * 0.001


def sell(value):
    global money, stock, count, fee
    print("sell : ", value)
    money = money + int(value)
    stock = 0
    count += 1
    fee += float(value) * 0.001


def get_state(pred):
    label = pred['label']
    if float(label) >= 0.3:
        return 1
    elif float(label) >= -0.1:
        return 0
    return -1
    # if label == 0:
    #     return 0
    # elif label == "-0" or label < 0:
    #     return -1
    # else:
    #     return 1


def process_result(tokens, time, result):
    global success_cnt, fail_cnt, before_money, before_value
    if not result.startswith("{"):
        return
    pred = json.loads(result)
    price = tokens[11]
    state = get_state(pred)
    print(time, " ", price, " ", state)

    # if money > before_money and before_value > 0:
    #     success_cnt += 1
    # elif money < before_money and before_value < 0:
    #     success_cnt += 1
    # elif money == before_money and before_value == 0:
    #     success_cnt += 1
    # else:
    #     fail_cnt += 1

    if state > 0 and stock == 0:
        buy(price)
    elif state < 0 and stock > 0:
        sell(price)

    before_value = state
    before_money = money

    print("money : ", money, ", count : ", count, ", fee : ", fee, ", success_cnt : ", success_cnt, ", fail_cnt : ", fail_cnt, ", label : ", pred['label'])


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
