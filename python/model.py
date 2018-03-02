import tensorflow as tf


LABELS = ['-1', '-0.6', '-0.3', '-0.1', '-0', '0', '0+', '0.1', '0.3', '0.6', '1']

FEATURE_SIZE = 30
LABEL_PAD = 5


def get_column_names():
    column_names = []
    for i in range(FEATURE_SIZE * 10):
        column_names.append("C" + str(i))
    return column_names


def get_classifier():
    my_feature_columns = []
    for key in get_column_names():
        my_feature_columns.append(tf.feature_column.numeric_column(key=key))

    classifier = tf.estimator.DNNClassifier(
        feature_columns=my_feature_columns,
        # Two hidden layers of 10 nodes each.
        hidden_units=[400] * 3,
        # The model must choose between 3 classes.
        n_classes=11,
        model_dir="models/ver_1_0_0",
        dropout=0.1)

    return classifier

