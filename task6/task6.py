import json
import numpy as np


def create_comparison_mat(column):
    c = len(column)
    res = np.zeros((c, c))

    for i in range(c):
        for j in range(c):
            res[i][j] = 0.5 if column[i] == column[j] else 1 if column[i] > column[j] else 0
    return res


def task(input_mat: str):
    mat = np.array(json.loads(input_mat)).T
    comparisons = []

    for col in range(mat.shape[1]):
        comparisons.append(create_comparison_mat(mat[:, col]).T)

    X = np.mean(comparisons, axis=0)
    kt = [1 / mat.shape[0] for _ in range(mat.shape[1])]
    y = np.dot(X, kt)
    l = np.dot(np.ones(len(y)), y)
    kt_1 = np.dot(1 / l, y)
    e = 0.001

    while max(abs(kt_1 - kt)) >= e:
        kt = kt_1
        y = np.dot(X, kt)
        l = np.dot(np.ones(len(y)), y)
        kt_1 = np.dot(1 / l, y)

    return json.dumps([round(res, 3) for res in kt_1])


def main():
    print(task("[[1,3,2],[2,2,2],[1.5,3,1.5]]"))


if __name__ == "__main__":
    main()
