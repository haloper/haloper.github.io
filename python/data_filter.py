import numpy as np
import random

FEATURE_SIZE = 5
LABEL_PAD = 1


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
    label = next_money - current_money
    item = []
    for i in range(FEATURE_SIZE):
        for j in range(1,11):
            if j % 2 == 1:
                item.append(que[i,j] - current_money)
            else:
                item.append(que[i,j])
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
    data_folder = "../server/data/"
    refined_foler = "../server/data/refined/"
    result = read_data(data_folder + filename)
    write_result(result, refined_foler + filename, refined_foler + '/test/' + filename, 30)


filter("20180212")


