from io import StringIO
import csv


def task(csv_str):
    f = StringIO(csv_str)
    reader = csv.reader(f, delimiter=',')
    input = []
    result = [[] for _ in range(5)]
    for line in reader:
        input.append([int(line[0]), int(line[1])])

    def direct(ind, arr):
        for line in input:
            if line[ind] not in arr:
                arr.append(line[ind])

    def indirect(first_ind, second_ind, arr):
        for line in input:
            for next_line in input:
                if line[first_ind] not in arr and next_line[first_ind] == line[second_ind]:
                    arr.append(line[first_ind])

    direct(0, result[0])
    direct(1, result[1])
    indirect(0, 1, result[2])
    indirect(1, 0, result[3])

    for line in input:
        for next_line in input:
            if line[1] not in result[4] and next_line[0] == line[0] and next_line != line:
                result[4].append(line[1])

    return result
