import numpy as np
import random
import constant


DATA_FOLDER = "../../server/data/"
REFINED_TRAIN_FOLDER = "../../server/data/refined/train/"
REFINED_TEST_FOLDER = "../../server/data/refined/test/"
TEST_PERCENT = 30


def read_data(filename):
    file = open(filename, "r")

    q = []
    result = []
    total_data_count = 0

    for line in file:
        item = parse_line(line)
        q.append(item)
        if len(q) == constant.FEATURE_SIZE + constant.LABEL_PAD:
            total_data_count += 1
            item = cal_que(q)
            if item:
                result.append(item)
            q.pop(0)

    print(filename, " - total count : ", total_data_count, ", success data : ", len(result), ", bad data : ", total_data_count - len(result))
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
    for i in range(1, constant.FEATURE_SIZE):
        if before_time + 1 != times[i]:
            # print("Bad data", times)
            return
        before_time = times[i]
    if times[constant.FEATURE_SIZE-1] + constant.LABEL_PAD != times[constant.FEATURE_SIZE - 1 + constant.LABEL_PAD]:
        # print("Bad data", times)
        return

    current_money = que[constant.FEATURE_SIZE - 1][11]
    next_money = que[constant.FEATURE_SIZE][11]
    diff = next_money - current_money
    item = []
    for i in range(constant.FEATURE_SIZE):
        for j in range(1,11):
            if j % 2 == 1:
                item.append((que[i,j] - current_money) / 1000)
            else:
                item.append(que[i,j])

    # label : 0 ~ 10
    rate = (diff / current_money) * 100
    if rate < -1:
        label = 0
    elif rate < -0.6:
        label = 1
    elif rate < -0.3:
        label = 2
    elif rate < -0.1:
        label = 3
    elif rate < 0:
        label = 4
    elif rate == 0:
        label = 5
    elif rate > 1:
        label = 10
    elif rate > 0.6:
        label = 9
    elif rate > 0.3:
        label = 8
    elif rate > 0.1:
        label = 7
    elif rate > 0:
        label = 6


    item.append(label)
    return item


def write_result(result, filename, test_filename, test_rate):
    f = open(filename, 'x')
    f_test = open(test_filename, "x")
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
    filter("20180215")
    filter("20180216")
    filter("20180217")
    filter("20180218")
    filter("20180219")
    filter("20180220")
    filter("20180221")
    filter("20180222")
    filter("20180223")
    filter("20180224")
    filter("20180225")
    filter("20180226")
    filter("20180227")
    filter("20180228")
    filter("20180301")


if __name__ == '__main__':
    main()
