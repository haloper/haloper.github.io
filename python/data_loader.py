import pandas as pd
import tensorflow as tf
import glob

CSV_COLUMN_NAMES = [
    'ask_1_5_val', 'ask_1_5_cnt',
    'ask_1_4_val', 'ask_1_4_cnt',
    'ask_1_3_val', 'ask_1_3_cnt',
    'ask_1_2_val', 'ask_1_2_cnt',
    'ask_1_1_val', 'ask_1_1_cnt',
    'bid_1_1_val', 'bid_1_1_cnt',
    'bid_1_2_val', 'bid_1_2_cnt',
    'bid_1_3_val', 'bid_1_3_cnt',
    'bid_1_4_val', 'bid_1_4_cnt',
    'bid_1_5_val', 'bid_1_5_cnt',
    'ask_2_5_val', 'ask_2_5_cnt',
    'ask_2_4_val', 'ask_2_4_cnt',
    'ask_2_3_val', 'ask_2_3_cnt',
    'ask_2_2_val', 'ask_2_2_cnt',
    'ask_2_1_val', 'ask_2_1_cnt',
    'bid_2_1_val', 'bid_2_1_cnt',
    'bid_2_2_val', 'bid_2_2_cnt',
    'bid_2_3_val', 'bid_2_3_cnt',
    'bid_2_4_val', 'bid_2_4_cnt',
    'bid_2_5_val', 'bid_2_5_cnt',
    'ask_3_5_val', 'ask_3_5_cnt',
    'ask_3_4_val', 'ask_3_4_cnt',
    'ask_3_3_val', 'ask_3_3_cnt',
    'ask_3_2_val', 'ask_3_2_cnt',
    'ask_3_1_val', 'ask_3_1_cnt',
    'bid_3_1_val', 'bid_3_1_cnt',
    'bid_3_2_val', 'bid_3_2_cnt',
    'bid_3_3_val', 'bid_3_3_cnt',
    'bid_3_4_val', 'bid_3_4_cnt',
    'bid_3_5_val', 'bid_3_5_cnt',
    'ask_4_5_val', 'ask_4_5_cnt',
    'ask_4_4_val', 'ask_4_4_cnt',
    'ask_4_3_val', 'ask_4_3_cnt',
    'ask_4_2_val', 'ask_4_2_cnt',
    'ask_4_1_val', 'ask_4_1_cnt',
    'bid_4_1_val', 'bid_4_1_cnt',
    'bid_4_2_val', 'bid_4_2_cnt',
    'bid_4_3_val', 'bid_4_3_cnt',
    'bid_4_4_val', 'bid_4_4_cnt',
    'bid_4_5_val', 'bid_4_5_cnt',
    'ask_5_5_val', 'ask_5_5_cnt',
    'ask_5_4_val', 'ask_5_4_cnt',
    'ask_5_3_val', 'ask_5_3_cnt',
    'ask_5_2_val', 'ask_5_2_cnt',
    'ask_5_1_val', 'ask_5_1_cnt',
    'bid_5_1_val', 'bid_5_1_cnt',
    'bid_5_2_val', 'bid_5_2_cnt',
    'bid_5_3_val', 'bid_5_3_cnt',
    'bid_5_4_val', 'bid_5_4_cnt',
    'bid_5_5_val', 'bid_5_5_cnt',
    'label'
]

LABELS = ['UP', 'DOWN']

REFINED_TRAIN_PATH = "../server/data/refined/train/"
REFINED_TEST_PATH = "../server/data/refined/test/"


def load_data(y_name='label'):

    train = None
    for file in glob.glob(REFINED_TRAIN_PATH + "*"):
        if train is None:
            train = pd.read_csv(file, names=CSV_COLUMN_NAMES, header=0)
        else :
            train.append(pd.read_csv(file, names=CSV_COLUMN_NAMES, header=0))

    train_x, train_y = train, train.pop(y_name)

    test = None
    for file in glob.glob(REFINED_TEST_PATH + "*"):
        if test is None:
            test = pd.read_csv(file, names=CSV_COLUMN_NAMES, header=0)
        else :
            test.append(pd.read_csv(file, names=CSV_COLUMN_NAMES, header=0))

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
