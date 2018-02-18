import pandas as pd
import tensorflow as tf
import glob
import model


REFINED_TRAIN_PATH = "../server/data/refined/train/"
REFINED_TEST_PATH = "../server/data/refined/test/"


def load_data(y_name='label'):

    csv_column_names = model.COLUMN_NAMES[:]
    csv_column_names.append("label")

    train = None
    for file in glob.glob(REFINED_TRAIN_PATH + "*"):
        if train is None:
            train = pd.read_csv(file, names=csv_column_names, header=0)
        else :
            train.append(pd.read_csv(file, names=csv_column_names, header=0))

    train_x, train_y = train, train.pop(y_name)

    test = None
    for file in glob.glob(REFINED_TEST_PATH + "*"):
        if test is None:
            test = pd.read_csv(file, names=csv_column_names, header=0)
        else :
            test.append(pd.read_csv(file, names=csv_column_names, header=0))

    test_x, test_y = test, test.pop(y_name)

    return (train_x, train_y), (test_x, test_y)


def train_input_fn(features, labels, batch_size):
    """An input function for training"""
    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices((dict(features), labels))

    # Shuffle, repeat, and batch the examples.
    dataset = dataset.batch(batch_size)

    # Return the dataset.
    return dataset


def eval_input_fn(features, labels, batch_size):
    """An input function for evaluation or prediction"""
    features=dict(features)
    if labels is None:
        # No labels, use only features.
        inputs = features
    else:
        inputs = (features, labels)

    # Convert the inputs to a Dataset.
    dataset = tf.data.Dataset.from_tensor_slices(inputs)

    # Batch the examples
    assert batch_size is not None, "batch_size must not be None"
    dataset = dataset.batch(batch_size)

    # Return the dataset.
    return dataset
