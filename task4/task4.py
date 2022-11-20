from io import StringIO
from math import log
import csv


def complex_relation(params, arr):
    new_arr = []
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i != j and arr[i][params[0]] == arr[j][params[1]]:
                new_arr.append(arr[i][params[2]])
    return new_arr


def entropy(p):
    return -(p * log(p, 2))


def task(csv_str):
    f = StringIO(csv_str)
    graph = list(csv.reader(f, delimiter=','))
    graph = list(map(lambda x: [int(element) for element in x], graph))

    py = [x[0] for x in graph]
    pp = [x[1] for x in graph]
    ky = complex_relation((1, 0, 0), graph)
    kp = complex_relation((0, 1, 1), graph)
    cp = complex_relation((0, 0, 1), graph)

    vertex = set()
    for x in graph:
        vertex.update(x)
    vertex = list(vertex)
    res = [[] for _ in vertex]

    for v in vertex:
        res[int(v) - 1].append(py.count(v))
        res[int(v) - 1].append(pp.count(v))
        res[int(v) - 1].append(ky.count(v))
        res[int(v) - 1].append(kp.count(v))
        res[int(v) - 1].append(cp.count(v))

    h = 0
    for i in range(len(vertex)):
        for j in range(len(vertex)):
            if res[i][j] != 0:
                h += entropy(res[i][j] / (len(vertex) - 1))

    return h


if __name__ == '__main__':
    data = '''1,2
              1,3
              3,4
              3,5'''

    print(task(data) == 6.5)
