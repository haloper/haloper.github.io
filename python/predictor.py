import argparse
import tensorflow as tf
import numpy as np
import datetime
import data_filter

import model
import data_loader


parser = argparse.ArgumentParser()
parser.add_argument('--date', default=None, help='predict date')

ROOT_DIR = "/Users/hoon/Documents/github/haloper.github.io/"

def main(argv):
    args = parser.parse_args(argv[1:])

    classifier = model.get_classifier()

    if args.date == None:
        today = datetime.datetime.now().strftime("%Y%m%d")
    else:
        today = args.date

    today = "20180213"

    # print("Target file : " , today)

    file = open(ROOT_DIR + "server/data/" + today, "r")
    lines = file.readlines()
    file.close()

    line_size = data_filter.FEATURE_SIZE
    last_lines = lines[line_size * -1:]

    q = []

    for line in last_lines:
        origin_item = data_filter.parse_line(line)
        q.append(origin_item)

    add_item = origin_item[:]
    add_item[0] = q[-1:][0][0] + 1
    q.append(add_item)

    item = data_filter.cal_que(q)

    if item is None:
        print("Data is bad")
        return

    item.pop()

    last_time = origin_item[0]

    predict_x = {}

    for i in range(len(model.COLUMN_NAMES)):
        predict_x[model.COLUMN_NAMES[i]] = []
        predict_x[model.COLUMN_NAMES[i]].append(item[i])



    predictions = classifier.predict(
        input_fn=lambda:data_loader.eval_input_fn(predict_x,
                                                  labels=None,
                                                  batch_size=100))

    for pred_dict in predictions:
        template = ('{}, {}, {:.10f}')

        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(last_time,
                              model.LABELS[class_id],
                              100 * probability))





if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.FATAL)
    tf.app.run(main)
