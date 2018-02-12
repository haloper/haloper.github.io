from queue import Queue


def read_data(filename):
    file = open(filename, "r")

    q = Queue(maxsize=5)

    for line in file:
        item = parse_line(line)
        print(item)

    file.close()


def parse_line(line):
    item = []
    for val in line.split(","):
        item.append(float(val))
    return item


read_data("../server/data/20180207")
