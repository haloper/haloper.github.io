#  Copyright 2016 The TensorFlow Authors. All Rights Reserved.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
"""An Example of a DNNClassifier for the Iris dataset."""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import tensorflow as tf

import data_loader
import datetime


DATA_FOLDER = "../server/data/"


parser = argparse.ArgumentParser()
parser.add_argument('--batch_size', default=100, type=int, help='batch size')
parser.add_argument('--train_steps', default=100000, type=int,
                    help='number of training steps')
parser.add_argument('--date', default=None, help='predict date')

def main(argv):
    args = parser.parse_args(argv[1:])

    # Fetch the data
    (train_x, train_y), (test_x, test_y) = data_loader.load_data()

    # Feature columns describe how to use the input.
    my_feature_columns = []
    for key in train_x.keys():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    # Build 2 hidden layer DNN with 10, 10 units respectively.
    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # Two hidden layers of 10 nodes each.
        hidden_units=[80, 120, 150, 200, 170, 120, 80, 50, 20, 5],
        # The model must choose between 3 classes.
        n_classes=2,
        model_dir="models/ver_1_0_0",
        dropout=0.1)

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


    if args.date == None:
        today = datetime.datetime.now().strftime("%Y%m%d")

    today = "20180214"

    print(today)
    log_date = datetime.date.fromtimestamp(25303161 * 60)
    print(log_date.strftime("%Y-%m-%d %H:%M"))

    # Generate predictions from the model
    # expected = ['Setosa', 'Versicolor', 'Virginica']
    # predict_x = {
    #     'SepalLength': [5.1, 5.9, 6.9],
    #     'SepalWidth': [3.3, 3.0, 3.1],
    #     'PetalLength': [1.7, 4.2, 5.4],
    #     'PetalWidth': [0.5, 1.5, 2.1],
    # }
    #
    # predictions = classifier.predict(
    #     input_fn=lambda:data_loader.eval_input_fn(predict_x,
    #                                             labels=None,
    #                                             batch_size=args.batch_size))
    #
    # for pred_dict, expec in zip(predictions, expected):
    #     template = ('\nPrediction is "{}" ({:.1f}%), expected "{}"')
    #
    #     class_id = pred_dict['class_ids'][0]
    #     probability = pred_dict['probabilities'][class_id]
    #
    #     print(template.format(data_loader.SPECIES[class_id],
    #                           100 * probability, expec))



def get_real_data(filename):
    file = open(filename, "r")
    for line in file:
        pass

    file.close()


if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)