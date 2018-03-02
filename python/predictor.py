import argparse
import tensorflow as tf
import numpy as np
import datetime
import data_filter

import model
import data_loader


parser = argparse.ArgumentParser()
parser.add_argument('--date', default=None, help='predict date')


def predict(date, time):
    classifier = model.get_classifier()
    file = open("../server/data/" + date, "r")
    lines = file.readlines()
    file.close()

    line_size = data_filter.FEATURE_SIZE
    if time == None:
        last_lines = lines[line_size * -1:]
    else:
        for i in range(len(lines)):
            if lines[i].startswith(time) and i >= line_size:
                last_lines = lines[i-line_size:i]
                break;
        else:
            return "Time is not valued"

    q = []

    for line in last_lines:
        origin_item = data_filter.parse_line(line)
        q.append(origin_item)

    add_item = origin_item[:]
    add_item[0] = q[-1:][0][0] + 1
    q.append(add_item)

    item = data_filter.cal_que(q)

    if item is None:
        return "Data is bad"

    item.pop()

    last_time = origin_item[0]

    predict_x = {}

    for i in range(model.FEATURE_SIZE):
        predict_x[i] = []
        predict_x[i].append(item[i])



    predictions = classifier.predict(
        input_fn=lambda:data_loader.eval_input_fn(predict_x,
                                                  labels=None,
                                                  batch_size=100))

    for pred_dict in predictions:
        template = ('"time":{}, "label":{}, "probability":{:.10f}')

        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        return "{" + template.format(last_time,
                               model.LABELS[class_id],
                               100 * probability) + "}"



def main(argv):
    args = parser.parse_args(argv[1:])

    if args.date == None:
        today = datetime.datetime.now().strftime("%Y%m%d")
    else:
        today = args.date

    today = "20180226"
    time = "25326197"

    # print("Target file : " , today)
    print(predict(today, time))





if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.FATAL)
    tf.app.run(main)
