import pandas as pd
import tensorflow as tf
import glob

CSV_COLUMN_NAMES = [
    'ask5_val', 'ask5_cnt',
    'ask4_val', 'ask4_cnt',
    'ask3_val', 'ask3_cnt',
    'ask2_val', 'ask2_cnt',
    'ask1_val', 'ask1_cnt',
    'bid1_val', 'bid1_cnt',
    'bid2_val', 'bid2_cnt',
    'bid3_val', 'bid3_cnt',
    'bid4_val', 'bid4_cnt',
    'bid5_val', 'bid5_cnt',
]

LABELS = ['UP', 'DOWN', 'KEEP']

REFINED_PATH = "../server/data/refined/"


def load_data(y_name='Label'):

    for log_file in glob.glob(REFINED_PATH + "*"):
        train = pd.read_csv(log_file, names=CSV_COLUMN_NAMES, header=0)

    train_x, train_y = train, train.pop(y_name)

    test = pd.read_csv(test_path, names=CSV_COLUMN_NAMES, header=0)
    test_x, test_y = test, test.pop(y_name)

    return (train_x, train_y), (test_x, test_y)
