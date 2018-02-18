import argparse
import tensorflow as tf
import numpy as np

import model
import datetime
import data_filter
import data_loader


parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--date', default=None, help='predict date')


def main(argv):
    args = parser.parse_args(argv[1:])
    classifier = model.get_classifier()

    if args.date == None:
        today = datetime.datetime.now().strftime("%Y%m%d")

    today = "20180214"

    print("Target file : " , today)

    file = open("../server/data/" + today, "r")
    lines = file.readlines()
    file.close()

    line_size = data_filter.FEATURE_SIZE
    last_lines = lines[line_size * -1:]

    q = []

    for line in last_lines:
        item = data_filter.parse_line(line)
        q.append(item)

    add_item = item[:]
    add_item[0] = q[-1:][0][0] + 1
    q.append(add_item)

    item = data_filter.cal_que(q)

    item.pop()

    print(item)

    predict_x = {}
    expected = model.LABELS[:]

    for i in range(len(model.COLUMN_NAMES)):
        predict_x[model.COLUMN_NAMES[i]] = item[i]


    predictions = classifier.predict(
        input_fn=lambda:data_loader.eval_input_fn(predict_x,
                                                labels=None,
                                                batch_size=1))


    for pred_dict, expec in zip(predictions, expected):
        template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')

        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(model.LABELS[class_id],
                              100 * probability, expec))





if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)