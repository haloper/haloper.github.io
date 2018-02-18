import tensorflow as tf


LABELS = ['UP', 'DOWN']
COLUMN_NAMES = [
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
    'bid_5_5_val', 'bid_5_5_cnt'
]


def get_classifier():
    my_feature_columns = []
    for column in COLUMN_NAMES:
        my_feature_columns.append(tf.feature_column.numeric_column(key=column))

    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # Two hidden layers of 10 nodes each.
        hidden_units=[80, 120, 150, 200, 170, 120, 80, 50, 20, 5],
        # The model must choose between 3 classes.
        n_classes=2,
        model_dir="models/ver_1_0_0",
        dropout=0.1)

    return classifier

