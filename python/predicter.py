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
parser.add_argument('--train_steps', default=1000, type=int,
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
    item = [4000.0,11.1665,3000.0,13.0123,2000.0,17.7486,1000.0,21.367,0.0,0.9289,5000.0,17.6749,4000.0,11.1665,3000.0,12.0123,2000.0,17.7486,1000.0,17.9538,5000.0,17.6749,4000.0,11.1665,3000.0,12.0123,2000.0,17.7486,1000.0,10.7233,5000.0,17.6749,4000.0,12.1665,3000.0,12.0123,2000.0,33.9724,1000.0,13.7336,5000.0,17.6749,4000.0,12.1665,3000.0,12.0123,2000.0,17.7486,1000.0,24.6088,5000.0,17.6749,4000.0,11.1665,3000.0,12.0123,2000.0,17.7486,1000.0,22.6247,5000.0,17.6749,4000.0,11.1665,3000.0,13.0123,2000.0,31.4786,1000.0,2.6679,5000.0,14.7349,4000.0,11.1665,3000.0,13.0123,2000.0,33.0652,1000.0,2.6679,5000.0,14.7349,4000.0,17.859,3000.0,13.0123,2000.0,33.0652,1000.0,23.3083,5000.0,14.7349,4000.0,10.3665,3000.0,12.0123,2000.0,17.7486,1000.0,9.255,0]

    predict_x = {}

    for i in range(len(model.COLUMN_NAMES)):
        predict_x[model.COLUMN_NAMES[i]] = []
        predict_x[model.COLUMN_NAMES[i]].append(item[i])

    predictions = classifier.predict(
        input_fn=lambda:data_loader.eval_input_fn(predict_x,
                                                labels=None,
                                                batch_size=100))

    for pred_dict in predictions:
        template = ('{},{},{:.1f}')

        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(0,
                              model.LABELS[class_id],
                              100 * probability))





if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
