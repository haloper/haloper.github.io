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
parser.add_argument('--train_steps', default=20000, type=int,
                    help='number of training steps')


def main(argv):
    args = parser.parse_args(argv[1:])

    (train_x, train_y), (test_x, test_y) = data_loader.load_data()

    classifier = model.get_classifier()

    # Train the Model.
    classifier.train(
        input_fn=lambda:data_loader.train_input_fn(train_x, train_y,
                                                   args.batch_size),
        steps=args.train_steps)

    # Evaluate the model.
    eval_result = classifier.evaluate(
        input_fn=lambda:data_loader.eval_input_fn(test_x, test_y,
                                                  args.batch_size))

    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_result))



    # today = None
    # if args.date == None:
    #     today = datetime.datetime.now().strftime("%Y%m%d")
    # else:
    #     today = args.date
    #
    # today = "20180211"
    #
    # # print("Target file : " , today)
    #
    # file = open("../server/data/" + today, "r")
    # lines = file.readlines()
    # file.close()
    #
    # line_size = data_filter.FEATURE_SIZE
    # last_lines = lines[line_size * -1:]
    #
    # q = []
    #
    # for line in last_lines:
    #     item = data_filter.parse_line(line)
    #     q.append(item)
    #
    # add_item = item[:]
    # add_item[0] = q[-1:][0][0] + 1
    # q.append(add_item)
    #
    # item = data_filter.cal_que(q)
    #
    # if item is None:
    #     print("Data is bad")
    #     return
    #
    # item.pop()

    # print(item)
    item = [10.0,6.0697,9.0,7.2612,8.0,7.7422,5.0,2.2205,4.0,0.0001,10.0,7.1323,9.0,2.2632,8.0,8.6772,5.0,2.2205,4.0,49.2917,7.0,2.94,6.0,0.01,5.0,7.887,4.0,2.3216,3.0,19.899,7.0,2.94,6.0,6.0082,5.0,0.01,4.0,0.1111,3.0,22.0148,8.0,8.6772,6.0,2.01,5.0,0.01,4.0,0.1111,3.0,22.0148,8.0,8.254,6.0,4.7587,5.0,0.01,4.0,0.1111,3.0,18.5206,8.0,4.7372,6.0,3.7587,5.0,0.01,4.0,2.5593,3.0,36.03,6.0,3.7587,5.0,0.01,4.0,0.1111,3.0,16.03,2.0,9.0824,6.0,4.7587,5.0,0.01,4.0,0.1111,3.0,16.03,2.0,0.1144,8.0,5.2611,6.0,3.7587,5.0,23.01,4.0,2.5593,3.0,17.029,3]
    item2 = [11.0,7.1323,10.0,2.2632,9.0,8.6772,6.0,2.2205,5.0,49.2917,8.0,2.94,7.0,0.01,6.0,7.887,5.0,2.3216,4.0,19.899,8.0,2.94,7.0,6.0082,6.0,0.01,5.0,0.1111,4.0,22.0148,9.0,8.6772,7.0,2.01,6.0,0.01,5.0,0.1111,4.0,22.0148,9.0,8.254,7.0,4.7587,6.0,0.01,5.0,0.1111,4.0,18.5206,9.0,4.7372,7.0,3.7587,6.0,0.01,5.0,2.5593,4.0,36.03,7.0,3.7587,6.0,0.01,5.0,0.1111,4.0,16.03,3.0,9.0824,7.0,4.7587,6.0,0.01,5.0,0.1111,4.0,16.03,3.0,0.1144,9.0,5.2611,7.0,3.7587,6.0,23.01,5.0,2.5593,4.0,17.029,9.0,6.059,7.0,4.7587,6.0,0.01,5.0,31.0171,4.0,47.028,2]
    item3 = [11.0,2.94,10.0,0.01,9.0,7.887,8.0,2.3216,7.0,19.899,11.0,2.94,10.0,6.0082,9.0,0.01,8.0,0.1111,7.0,22.0148,12.0,8.6772,10.0,2.01,9.0,0.01,8.0,0.1111,7.0,22.0148,12.0,8.254,10.0,4.7587,9.0,0.01,8.0,0.1111,7.0,18.5206,12.0,4.7372,10.0,3.7587,9.0,0.01,8.0,2.5593,7.0,36.03,10.0,3.7587,9.0,0.01,8.0,0.1111,7.0,16.03,6.0,9.0824,10.0,4.7587,9.0,0.01,8.0,0.1111,7.0,16.03,6.0,0.1144,12.0,5.2611,10.0,3.7587,9.0,23.01,8.0,2.5593,7.0,17.029,12.0,6.059,10.0,4.7587,9.0,0.01,8.0,31.0171,7.0,47.028,9.0,1.01,8.0,3.0511,7.0,55.8852,6.0,23.0,5.0,7.2454,8]
    item4 = [7.0,2.94,6.0,6.0082,5.0,0.01,4.0,0.1111,3.0,22.0148,8.0,8.6772,6.0,2.01,5.0,0.01,4.0,0.1111,3.0,22.0148,8.0,8.254,6.0,4.7587,5.0,0.01,4.0,0.1111,3.0,18.5206,8.0,4.7372,6.0,3.7587,5.0,0.01,4.0,2.5593,3.0,36.03,6.0,3.7587,5.0,0.01,4.0,0.1111,3.0,16.03,2.0,9.0824,6.0,4.7587,5.0,0.01,4.0,0.1111,3.0,16.03,2.0,0.1144,8.0,5.2611,6.0,3.7587,5.0,23.01,4.0,2.5593,3.0,17.029,8.0,6.059,6.0,4.7587,5.0,0.01,4.0,31.0171,3.0,47.028,5.0,1.01,4.0,3.0511,3.0,55.8852,2.0,23.0,1.0,7.2454,6.0,6.6987,5.0,0.01,4.0,0.1111,3.0,56.8852,1.0,24.3937,2]
    item5 = [11.0,8.6772,9.0,2.01,8.0,0.01,7.0,0.1111,6.0,22.0148,11.0,8.254,9.0,4.7587,8.0,0.01,7.0,0.1111,6.0,18.5206,11.0,4.7372,9.0,3.7587,8.0,0.01,7.0,2.5593,6.0,36.03,9.0,3.7587,8.0,0.01,7.0,0.1111,6.0,16.03,5.0,9.0824,9.0,4.7587,8.0,0.01,7.0,0.1111,6.0,16.03,5.0,0.1144,11.0,5.2611,9.0,3.7587,8.0,23.01,7.0,2.5593,6.0,17.029,11.0,6.059,9.0,4.7587,8.0,0.01,7.0,31.0171,6.0,47.028,8.0,1.01,7.0,3.0511,6.0,55.8852,5.0,23.0,4.0,7.2454,9.0,6.6987,8.0,0.01,7.0,0.1111,6.0,56.8852,4.0,24.3937,8.0,0.01,7.0,0.1111,6.0,55.8862,4.0,28.2383,3.0,3.1484,8]
    item6 = [8.0,8.254,6.0,4.7587,5.0,0.01,4.0,0.1111,3.0,18.5206,8.0,4.7372,6.0,3.7587,5.0,0.01,4.0,2.5593,3.0,36.03,6.0,3.7587,5.0,0.01,4.0,0.1111,3.0,16.03,2.0,9.0824,6.0,4.7587,5.0,0.01,4.0,0.1111,3.0,16.03,2.0,0.1144,8.0,5.2611,6.0,3.7587,5.0,23.01,4.0,2.5593,3.0,17.029,8.0,6.059,6.0,4.7587,5.0,0.01,4.0,31.0171,3.0,47.028,5.0,1.01,4.0,3.0511,3.0,55.8852,2.0,23.0,1.0,7.2454,6.0,6.6987,5.0,0.01,4.0,0.1111,3.0,56.8852,1.0,24.3937,5.0,0.01,4.0,0.1111,3.0,55.8862,1.0,28.2383,0.0,3.1484,5.0,0.01,4.0,0.1111,3.0,55.8862,2.0,2.94,1.0,26.0413,3]

    predict_x = {}

    for i in range(len(model.COLUMN_NAMES)):
        predict_x[model.COLUMN_NAMES[i]] = []
        predict_x[model.COLUMN_NAMES[i]].append(item[i])
        predict_x[model.COLUMN_NAMES[i]].append(item2[i])
        predict_x[model.COLUMN_NAMES[i]].append(item3[i])
        predict_x[model.COLUMN_NAMES[i]].append(item4[i])
        predict_x[model.COLUMN_NAMES[i]].append(item5[i])
        predict_x[model.COLUMN_NAMES[i]].append(item6[i])

    predictions = classifier.predict(
        input_fn=lambda:data_loader.eval_input_fn(predict_x,
                                                labels=None,
                                                batch_size=100))

    for pred_dict in predictions:
        template = ('{},{},{:.10f}')

        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(0,
                              model.LABELS[class_id],
                              100 * probability))
        print(pred_dict['probabilities'])





if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
