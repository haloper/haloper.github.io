import numpy as np

FEATURE_SIZE = 5
LABEL_PAD = 1

result = []


def read_data(filename):
    file = open(filename, "r")

    q = []

    for line in file:
        item = parse_line(line)
        q.append(item)
        if len(q) == FEATURE_SIZE + LABEL_PAD:
            cal_que(q)
            q.pop(0)

    file.close()


def parse_line(line):
    item = []
    for val in line.split(","):
        item.append(float(val))
    return item


def cal_que(q):
    que = np.array(q)
    print(que)
    print("=====")
    print(que[:,0])
    print("=====")


read_data("../server/data/20180207")
