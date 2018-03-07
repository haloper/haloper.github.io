import data_loader
import tensorflow as tf


tf.logging.set_verbosity(tf.logging.INFO)




def cnn_model_fn(features, labels, mode):

    input_layer = tf.reshape(features["x"], [-1, 30, 10, 1])

    # Input Tensor Shape: [batch_size, 30, 10, 1]
    # Output Tensor Shape: [batch_size, 30, 5, 32]
    conv1 = tf.layers.conv2d(
        inputs=input_layer,
        filters=32,
        kernel_size=[1, 2],
        strides=(1, 2),
        padding="valid",
        activation=tf.nn.relu)

    # Input Tensor Shape: [batch_size, 30, 5, 32]
    # Output Tensor Shape: [batch_size, 6, 5, 32]
    pool1 = tf.layers.max_pooling2d(inputs=conv1, pool_size=[5, 1], strides=(5,1))

    # Input Tensor Shape: [batch_size, 6, 5, 32]
    # Output Tensor Shape: [batch_size, 6, 5, 64]
    conv2 = tf.layers.conv2d(
        inputs=pool1,
        filters=64,
        kernel_size=[1, 1],
        strides=(1, 1),
        padding="same",
        activation=tf.nn.relu)

    # Input Tensor Shape: [batch_size, 6, 5, 64]
    # Output Tensor Shape: [batch_size, 3, 5, 64]
    pool2 = tf.layers.max_pooling2d(inputs=conv2, pool_size=[2, 1], strides=(2,1))

    pool2_flat = tf.reshape(pool2, [-1, 3 * 5 * 64])

    dense = tf.layers.dense(inputs=pool2_flat, units=1024, activation=tf.nn.relu)

    dropout = tf.layers.dropout(
        inputs=dense, rate=0.4, training=mode == tf.estimator.ModeKeys.TRAIN)

    dense2 = tf.layers.dense(inputs=dropout, units=1024, activation=tf.nn.relu)

    dropout2 = tf.layers.dropout(
        inputs=dense2, rate=0.4, training=mode == tf.estimator.ModeKeys.TRAIN)

    dense3 = tf.layers.dense(inputs=dropout2, units=1024, activation=tf.nn.relu)

    dropout3 = tf.layers.dropout(
        inputs=dense3, rate=0.4, training=mode == tf.estimator.ModeKeys.TRAIN)

    logits = tf.layers.dense(inputs=dropout3, units=11)

    predictions = {
        # Generate predictions (for PREDICT and EVAL mode)
        "classes": tf.argmax(input=logits, axis=1),
        # Add `softmax_tensor` to the graph. It is used for PREDICT and by the
        # `logging_hook`.
        "probabilities": tf.nn.softmax(logits, name="softmax_tensor")
    }
    if mode == tf.estimator.ModeKeys.PREDICT:
        return tf.estimator.EstimatorSpec(mode=mode, predictions=predictions)

    # Calculate Loss (for both TRAIN and EVAL modes)
    loss = tf.losses.sparse_softmax_cross_entropy(labels=labels, logits=logits)

    # Configure the Training Op (for TRAIN mode)
    if mode == tf.estimator.ModeKeys.TRAIN:
        optimizer = tf.train.GradientDescentOptimizer(learning_rate=0.001)
        train_op = optimizer.minimize(
            loss=loss,
            global_step=tf.train.get_global_step())
        return tf.estimator.EstimatorSpec(mode=mode, loss=loss, train_op=train_op)

    # Add evaluation metrics (for EVAL mode)
    eval_metric_ops = {
        "accuracy": tf.metrics.accuracy(
            labels=labels, predictions=predictions["classes"])}
    return tf.estimator.EstimatorSpec(
        mode=mode, loss=loss, eval_metric_ops=eval_metric_ops)


def get_classifier():
    return tf.estimator.Estimator(
        model_fn=cnn_model_fn, model_dir="../models/rnn_v_1_0_0")


def main(unused_argv):
    # Load training and eval data
    (train_data, train_labels), (eval_data, eval_labels) = data_loader.load_data()

    # Create the Estimator
    mnist_classifier = get_classifier()

    # Set up logging for predictions
    # Log the values in the "Softmax" tensor with label "probabilities"
    tensors_to_log = {"probabilities": "softmax_tensor"}
    logging_hook = tf.train.LoggingTensorHook(
        tensors=tensors_to_log, every_n_iter=500)

    # Train the model
    train_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": train_data},
        y=train_labels,
        batch_size=100,
        num_epochs=None,
        shuffle=False)
    mnist_classifier.train(
        input_fn=train_input_fn,
        steps=10000,
        hooks=[logging_hook])

    # Evaluate the model and print results
    eval_input_fn = tf.estimator.inputs.numpy_input_fn(
        x={"x": eval_data},
        y=eval_labels,
        num_epochs=1,
        shuffle=False)
    eval_results = mnist_classifier.evaluate(input_fn=eval_input_fn)
    print('\nTest set accuracy: {accuracy:0.3f}\n'.format(**eval_results))


if __name__ == "__main__":
    tf.app.run()
