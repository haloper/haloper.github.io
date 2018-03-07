import argparse
import tensorflow as tf
import datetime
import data_filter
import cnn_model
import data_loader
import constant
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument('--date', default=None, help='predict date')


def predict(date, time):
    classifier = cnn_model.get_classifier()
    file = open("../../server/data/" + date, "r")
    lines = file.readlines()
    file.close()

    line_size = constant.FEATURE_SIZE + constant.LABEL_PAD
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


    predict_x = data_loader.parse_tokens(list(map(np.float32, item)));


    pred_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": predict_x},
        y=None,
        num_epochs=1,
        shuffle=False)
    predictions = classifier.predict(input_fn=pred_input_fn)

    for predict in predictions:
        pass

    template = ('"time":{}, "label":{}, "probability":{:.10f}')

    class_id = predictions['classes'][0]
    probability = predictions['probabilities'][class_id]

    return "{" + template.format(last_time,
                                 cnn_model.LABELS[class_id],
                                 100 * probability) + "}"




def main(argv):
    args = parser.parse_args(argv[1:])

    if args.date == None:
        today = datetime.datetime.now().strftime("%Y%m%d")
    else:
        today = args.date

    today = "20180220"
    time = "25317692"

    # print("Target file : " , today)
    print(predict(today, time))





if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.FATAL)
    tf.app.run(main)
