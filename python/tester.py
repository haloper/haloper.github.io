import argparse
import tensorflow as tf
import numpy as np

import model
import data_loader


parser = argparse.ArgumentParser()

def main(argv):
    classifier = model.get_classifier()
    items = [
        [10.0,6.0697,9.0,7.2612,8.0,7.7422,5.0,2.2205,4.0,0.0001,10.0,7.1323,9.0,2.2632,8.0,8.6772,5.0,2.2205,4.0,49.2917,7.0,2.94,6.0,0.01,5.0,7.887,4.0,2.3216,3.0,19.899,7.0,2.94,6.0,6.0082,5.0,0.01,4.0,0.1111,3.0,22.0148,8.0,8.6772,6.0,2.01,5.0,0.01,4.0,0.1111,3.0,22.0148,8.0,8.254,6.0,4.7587,5.0,0.01,4.0,0.1111,3.0,18.5206,8.0,4.7372,6.0,3.7587,5.0,0.01,4.0,2.5593,3.0,36.03,6.0,3.7587,5.0,0.01,4.0,0.1111,3.0,16.03,2.0,9.0824,6.0,4.7587,5.0,0.01,4.0,0.1111,3.0,16.03,2.0,0.1144,8.0,5.2611,6.0,3.7587,5.0,23.01,4.0,2.5593,3.0,17.029,3],
        [11.0,7.1323,10.0,2.2632,9.0,8.6772,6.0,2.2205,5.0,49.2917,8.0,2.94,7.0,0.01,6.0,7.887,5.0,2.3216,4.0,19.899,8.0,2.94,7.0,6.0082,6.0,0.01,5.0,0.1111,4.0,22.0148,9.0,8.6772,7.0,2.01,6.0,0.01,5.0,0.1111,4.0,22.0148,9.0,8.254,7.0,4.7587,6.0,0.01,5.0,0.1111,4.0,18.5206,9.0,4.7372,7.0,3.7587,6.0,0.01,5.0,2.5593,4.0,36.03,7.0,3.7587,6.0,0.01,5.0,0.1111,4.0,16.03,3.0,9.0824,7.0,4.7587,6.0,0.01,5.0,0.1111,4.0,16.03,3.0,0.1144,9.0,5.2611,7.0,3.7587,6.0,23.01,5.0,2.5593,4.0,17.029,9.0,6.059,7.0,4.7587,6.0,0.01,5.0,31.0171,4.0,47.028,2],
        [11.0,2.94,10.0,0.01,9.0,7.887,8.0,2.3216,7.0,19.899,11.0,2.94,10.0,6.0082,9.0,0.01,8.0,0.1111,7.0,22.0148,12.0,8.6772,10.0,2.01,9.0,0.01,8.0,0.1111,7.0,22.0148,12.0,8.254,10.0,4.7587,9.0,0.01,8.0,0.1111,7.0,18.5206,12.0,4.7372,10.0,3.7587,9.0,0.01,8.0,2.5593,7.0,36.03,10.0,3.7587,9.0,0.01,8.0,0.1111,7.0,16.03,6.0,9.0824,10.0,4.7587,9.0,0.01,8.0,0.1111,7.0,16.03,6.0,0.1144,12.0,5.2611,10.0,3.7587,9.0,23.01,8.0,2.5593,7.0,17.029,12.0,6.059,10.0,4.7587,9.0,0.01,8.0,31.0171,7.0,47.028,9.0,1.01,8.0,3.0511,7.0,55.8852,6.0,23.0,5.0,7.2454,8],
        [8.0,15.3867,7.0,19.0507,6.0,12.6695,5.0,1.3091,4.0,31.1885,8.0,15.3867,7.0,19.0507,6.0,12.6695,5.0,1.3091,4.0,28.5953,8.0,14.3867,7.0,18.0507,6.0,12.6695,5.0,1.3091,4.0,108.7563,8.0,14.3867,7.0,18.0507,6.0,12.6695,5.0,1.3091,4.0,111.1563,6.0,12.6695,5.0,11.3091,4.0,112.1263,3.0,6.0,2.0,0.4912,7.0,18.0507,6.0,12.6695,5.0,12.3091,4.0,111.1263,3.0,6.8453,7.0,19.2228,6.0,12.6695,5.0,11.3091,4.0,97.5126,3.0,16.1369,7.0,19.2228,6.0,12.6695,5.0,11.3091,4.0,97.5126,3.0,20.5132,7.0,19.2228,6.0,12.6695,5.0,11.3091,4.0,38.4866,3.0,17.1206,7.0,19.2228,6.0,12.6695,5.0,11.3091,4.0,98.5126,3.0,34.4969,6],
        [8.0,14.3867,7.0,18.0507,6.0,12.6695,5.0,1.3091,4.0,108.7563,8.0,14.3867,7.0,18.0507,6.0,12.6695,5.0,1.3091,4.0,111.1563,6.0,12.6695,5.0,11.3091,4.0,112.1263,3.0,6.0,2.0,0.4912,7.0,18.0507,6.0,12.6695,5.0,12.3091,4.0,111.1263,3.0,6.8453,7.0,19.2228,6.0,12.6695,5.0,11.3091,4.0,97.5126,3.0,16.1369,7.0,19.2228,6.0,12.6695,5.0,11.3091,4.0,97.5126,3.0,20.5132,7.0,19.2228,6.0,12.6695,5.0,11.3091,4.0,38.4866,3.0,17.1206,7.0,19.2228,6.0,12.6695,5.0,11.3091,4.0,98.5126,3.0,34.4969,6.0,12.6695,5.0,11.3091,4.0,74.5366,3.0,32.5505,2.0,4.3995,6.0,12.6695,5.0,11.3091,4.0,43.5276,3.0,28.1742,2.0,8.2913,5],
        [9.0,12.6695,8.0,12.3091,7.0,18.5516,6.0,4.2009,5.0,39.117,9.0,15.6095,8.0,11.3091,7.0,19.5516,6.0,4.2009,5.0,39.117,9.0,12.6695,8.0,11.3091,7.0,19.5516,6.0,4.2009,5.0,17.7595,9.0,12.6695,8.0,11.3091,7.0,19.5516,6.0,4.2009,5.0,39.117,9.0,12.6695,8.0,14.2491,7.0,18.5516,6.0,5.2009,5.0,35.8819,9.0,12.6695,8.0,14.2491,7.0,18.5516,6.0,5.2009,5.0,40.7603,7.0,18.5516,6.0,7.1409,5.0,17.7603,4.0,54.5896,2.0,2.9794,7.0,18.5516,6.0,7.1409,5.0,17.7603,4.0,29.0361,2.0,1.9794,8.0,12.2855,7.0,18.5516,6.0,5.2009,5.0,22.8906,4.0,56.9964,8.0,11.3091,7.0,18.5516,6.0,5.2009,5.0,25.8306,4.0,27.1102,4],
        [10.0,15.6095,9.0,11.3091,8.0,19.5516,7.0,4.2009,6.0,39.117,10.0,12.6695,9.0,11.3091,8.0,19.5516,7.0,4.2009,6.0,17.7595,10.0,12.6695,9.0,11.3091,8.0,19.5516,7.0,4.2009,6.0,39.117,10.0,12.6695,9.0,14.2491,8.0,18.5516,7.0,5.2009,6.0,35.8819,10.0,12.6695,9.0,14.2491,8.0,18.5516,7.0,5.2009,6.0,40.7603,8.0,18.5516,7.0,7.1409,6.0,17.7603,5.0,54.5896,3.0,2.9794,8.0,18.5516,7.0,7.1409,6.0,17.7603,5.0,29.0361,3.0,1.9794,9.0,12.2855,8.0,18.5516,7.0,5.2009,6.0,22.8906,5.0,56.9964,9.0,11.3091,8.0,18.5516,7.0,5.2009,6.0,25.8306,5.0,27.1102,9.0,11.3091,8.0,18.5516,7.0,5.2009,6.0,26.1228,5.0,48.3407,4],
        [11.0,12.6695,10.0,11.3091,9.0,19.5516,8.0,4.2009,7.0,39.117,11.0,12.6695,10.0,14.2491,9.0,18.5516,8.0,5.2009,7.0,35.8819,11.0,12.6695,10.0,14.2491,9.0,18.5516,8.0,5.2009,7.0,40.7603,9.0,18.5516,8.0,7.1409,7.0,17.7603,6.0,54.5896,4.0,2.9794,9.0,18.5516,8.0,7.1409,7.0,17.7603,6.0,29.0361,4.0,1.9794,10.0,12.2855,9.0,18.5516,8.0,5.2009,7.0,22.8906,6.0,56.9964,10.0,11.3091,9.0,18.5516,8.0,5.2009,7.0,25.8306,6.0,27.1102,10.0,11.3091,9.0,18.5516,8.0,5.2009,7.0,26.1228,6.0,48.3407,7.0,16.7185,6.0,24.1721,5.0,0.9992,4.0,19.912,1.0,1.9794,7.0,15.7185,6.0,23.9992,5.0,0.9992,4.0,25.0167,2.0,0.6473,5],
        [11.0,12.6695,10.0,14.2491,9.0,18.5516,8.0,5.2009,7.0,35.8819,11.0,12.6695,10.0,14.2491,9.0,18.5516,8.0,5.2009,7.0,40.7603,9.0,18.5516,8.0,7.1409,7.0,17.7603,6.0,54.5896,4.0,2.9794,9.0,18.5516,8.0,7.1409,7.0,17.7603,6.0,29.0361,4.0,1.9794,10.0,12.2855,9.0,18.5516,8.0,5.2009,7.0,22.8906,6.0,56.9964,10.0,11.3091,9.0,18.5516,8.0,5.2009,7.0,25.8306,6.0,27.1102,10.0,11.3091,9.0,18.5516,8.0,5.2009,7.0,26.1228,6.0,48.3407,7.0,16.7185,6.0,24.1721,5.0,0.9992,4.0,19.912,1.0,1.9794,7.0,15.7185,6.0,23.9992,5.0,0.9992,4.0,25.0167,2.0,0.6473,7.0,16.7185,6.0,23.0,4.0,10.5739,3.0,1.8192,2.0,14.7744,5],
        [9.0,18.5516,8.0,7.1409,7.0,17.7603,6.0,54.5896,4.0,2.9794,9.0,18.5516,8.0,7.1409,7.0,17.7603,6.0,29.0361,4.0,1.9794,10.0,12.2855,9.0,18.5516,8.0,5.2009,7.0,22.8906,6.0,56.9964,10.0,11.3091,9.0,18.5516,8.0,5.2009,7.0,25.8306,6.0,27.1102,10.0,11.3091,9.0,18.5516,8.0,5.2009,7.0,26.1228,6.0,48.3407,7.0,16.7185,6.0,24.1721,5.0,0.9992,4.0,19.912,1.0,1.9794,7.0,15.7185,6.0,23.9992,5.0,0.9992,4.0,25.0167,2.0,0.6473,7.0,16.7185,6.0,23.0,4.0,10.5739,3.0,1.8192,2.0,14.7744,7.0,16.7185,6.0,23.0,5.0,1.9984,4.0,4.1696,2.0,13.2682,6.0,23.0,5.0,1.9984,4.0,1.1721,3.0,2.94,2.0,13.6642,5],
        [10.0,11.3091,9.0,18.5516,8.0,5.2009,7.0,25.8306,6.0,27.1102,10.0,11.3091,9.0,18.5516,8.0,5.2009,7.0,26.1228,6.0,48.3407,7.0,16.7185,6.0,24.1721,5.0,0.9992,4.0,19.912,1.0,1.9794,7.0,15.7185,6.0,23.9992,5.0,0.9992,4.0,25.0167,2.0,0.6473,7.0,16.7185,6.0,23.0,4.0,10.5739,3.0,1.8192,2.0,14.7744,7.0,16.7185,6.0,23.0,5.0,1.9984,4.0,4.1696,2.0,13.2682,6.0,23.0,5.0,1.9984,4.0,1.1721,3.0,2.94,2.0,13.6642,6.0,25.0,5.0,1.9984,4.0,1.1721,3.0,2.94,2.0,9.4761,7.0,18.3889,6.0,25.0,5.0,1.9984,4.0,2.7073,2.0,3.3213,7.0,18.4888,6.0,25.0,5.0,4.9384,4.0,1.1721,2.0,10.2014,4],
        [4.0,12.7913,3.0,24.176,2.0,24.8763,1.0,39.784,0.0,0.5186,4.0,12.7913,3.0,24.176,2.0,24.8763,1.0,39.784,0.0,1.3572,5.0,79.8693,4.0,12.7913,3.0,24.176,2.0,24.8763,1.0,38.9246,5.0,80.6527,4.0,12.7913,3.0,34.0915,2.0,24.8763,1.0,31.1363,4.0,12.7913,3.0,34.0915,2.0,24.8763,1.0,22.9711,0.0,2.2498,5.0,80.6527,4.0,12.7913,3.0,34.0915,2.0,24.8763,1.0,20.458,5.0,79.6527,4.0,12.7913,3.0,34.0915,2.0,11.3429,1.0,30.3812,5.0,79.6527,4.0,12.7913,3.0,34.0915,2.0,19.3869,1.0,32.1054,5.0,80.6527,4.0,22.7068,3.0,24.176,2.0,11.3429,1.0,19.0936,6.0,28.7059,5.0,80.1527,4.0,22.7068,3.0,24.176,2.0,10.3429,7],
        [3.0,12.7913,2.0,24.176,1.0,24.8763,0.0,39.784,-1.0,1.3572,4.0,79.8693,3.0,12.7913,2.0,24.176,1.0,24.8763,0.0,38.9246,4.0,80.6527,3.0,12.7913,2.0,34.0915,1.0,24.8763,0.0,31.1363,3.0,12.7913,2.0,34.0915,1.0,24.8763,0.0,22.9711,-1.0,2.2498,4.0,80.6527,3.0,12.7913,2.0,34.0915,1.0,24.8763,0.0,20.458,4.0,79.6527,3.0,12.7913,2.0,34.0915,1.0,11.3429,0.0,30.3812,4.0,79.6527,3.0,12.7913,2.0,34.0915,1.0,19.3869,0.0,32.1054,4.0,80.6527,3.0,22.7068,2.0,24.176,1.0,11.3429,0.0,19.0936,5.0,28.7059,4.0,80.1527,3.0,22.7068,2.0,24.176,1.0,10.3429,5.0,28.7059,4.0,80.1527,3.0,22.7068,2.0,23.976,1.0,10.3429,5],
        [4.0,79.8693,3.0,12.7913,2.0,24.176,1.0,24.8763,0.0,38.9246,4.0,80.6527,3.0,12.7913,2.0,34.0915,1.0,24.8763,0.0,31.1363,3.0,12.7913,2.0,34.0915,1.0,24.8763,0.0,22.9711,-1.0,2.2498,4.0,80.6527,3.0,12.7913,2.0,34.0915,1.0,24.8763,0.0,20.458,4.0,79.6527,3.0,12.7913,2.0,34.0915,1.0,11.3429,0.0,30.3812,4.0,79.6527,3.0,12.7913,2.0,34.0915,1.0,19.3869,0.0,32.1054,4.0,80.6527,3.0,22.7068,2.0,24.176,1.0,11.3429,0.0,19.0936,5.0,28.7059,4.0,80.1527,3.0,22.7068,2.0,24.176,1.0,10.3429,5.0,28.7059,4.0,80.1527,3.0,22.7068,2.0,23.976,1.0,10.3429,5.0,28.7059,4.0,80.1527,3.0,22.7068,2.0,23.976,1.0,17.6352,7]
    ]

    predict_x = {}
    expected = []

    for i in range(len(model.COLUMN_NAMES)):
        predict_x[model.COLUMN_NAMES[i]] = []
        for item in items:
            predict_x[model.COLUMN_NAMES[i]].append(item[i])

    for item in items:
        expected.append(item[len(item) - 1])



    predictions = classifier.predict(
        input_fn=lambda:data_loader.eval_input_fn(predict_x,
                                                labels=None,
                                                batch_size=100))

    for pred_dict, expec in zip(predictions, expected):
        template = ('predict: {},{:.10f}, expected: {}')

        class_id = pred_dict['class_ids'][0]
        probability = pred_dict['probabilities'][class_id]

        print(template.format(model.LABELS[class_id],
                              100 * probability,
                              model.LABELS[expec]))





if __name__ == '__main__':
    tf.logging.set_verbosity(tf.logging.INFO)
    tf.app.run(main)
