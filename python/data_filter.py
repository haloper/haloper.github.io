import numpy as np
import random

FEATURE_SIZE = 10
LABEL_PAD = 1
DATA_FOLDER = "../server/data/"
REFINED_TRAIN_FOLDER = "../server/data/refined/train/"
REFINED_TEST_FOLDER = "../server/data/refined/test/"
TEST_PERCENT = 30


def read_data(filename):
    file = open(filename, "r")

    q = []
    result = []
    total_data_count = 0

    for line in file:
        item = parse_line(line)
        q.append(item)
        if len(q) == FEATURE_SIZE + LABEL_PAD:
            total_data_count += 1
            item = cal_que(q)
            if item:
                result.append(item)
            q.pop(0)

    print("total count : ", total_data_count, ", success data : ", len(result), ", bad data : ", total_data_count - len(result))
    file.close()

    return result


def parse_line(line):
    item = []
    for val in line.split(","):
        item.append(float(val))
    return item


def cal_que(q):
    que = np.array(q)

    times = que[:,0]
    before_time = times[0]
    for i in range(1, FEATURE_SIZE):
        if before_time + 1 != times[i]:
            # print("Bad data", times)
            return
        before_time = times[i]
    if times[FEATURE_SIZE-1] + LABEL_PAD != times[FEATURE_SIZE]:
        # print("Bad data", times)
        return

    current_money = que[FEATURE_SIZE - 1][11]
    next_money = que[FEATURE_SIZE][11]
    diff = next_money - current_money
    item = []
    for i in range(FEATURE_SIZE):
        for j in range(1,11):
            if j % 2 == 1:
                item.append(que[i,j] - current_money)
            else:
                item.append(que[i,j])
    if diff < 0:
        label = 1
    else:
        label = 0

    item.append(label)
    return item


def write_result(result, filename, test_filename, test_rate):
    f = open(filename, 'w')
    f_test = open(test_filename, "w")
    for row in result:
        data = ",".join(map(str, row)) + "\n"
        ran = random.randrange(0,100)
        if ran < test_rate:
            f_test.write(data)
        else:
            f.write(data)
    f_test.close()
    f.close()


def filter(filename):
    result = read_data(DATA_FOLDER + filename)
    write_result(result, REFINED_TRAIN_FOLDER + filename, REFINED_TEST_FOLDER + filename, TEST_PERCENT)


def main():
    filter("20180207")
    filter("20180208")
    filter("20180209")
    filter("20180210")
    filter("20180211")
    filter("20180212")
    filter("20180213")
    filter("20180214")


if __name__ == '__main__':
    main()