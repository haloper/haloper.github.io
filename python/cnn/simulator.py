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
buy_money = 0

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
    global success_cnt, fail_cnt, before_money, before_value, buy_money
    if not result.startswith("{"):
        return
    predict = json.loads(result)
    current_price = tokens[11]
    state = get_state(predict)
    print("time : ", time, " current_price : ", current_price)

    label = float(predict['label'])
    # check buy
    if label >= 0.3 and stock == 0:
        buy_money = current_price
        buy(current_price)

    # check sell
    if stock > 0:
        if current_price < buy_money or label < -0.3:
            sell(current_price)


    before_value = state
    before_money = money

    print("money : ", money, ", count : ", count, ", fee : ", fee, ", success_cnt : ", success_cnt, ", fail_cnt : ", fail_cnt, ", label : ", predict['label'])


def main(argv):

    date = "20180302"

    file = open("../../server/data/" + date, "r")
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
