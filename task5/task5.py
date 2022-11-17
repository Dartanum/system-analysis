import json

import numpy as np


def task(arg1: str, arg2: str) -> str:
    conflicts = []
    ranking1 = json.loads(arg1)
    ranking2 = json.loads(arg2)

    Ya = get_relationship_mat(ranking1)
    Ya_transposed = Ya.transpose()
    Yb = get_relationship_mat(ranking2)
    Yb_transposed = Yb.transpose()
    Yab = np.multiply(Ya, Yb)
    Yab_transposed = np.multiply(Ya_transposed, Yb_transposed)

    for i in range(Yab.shape[0]):
        for j in range(Yab[i].shape[1]):
            if int(Yab[i, j]) == 0 and int(Yab_transposed[i, j]) == 0:
                if (str(j + 1), str(i + 1)) not in conflicts:
                    conflicts.append((str(i + 1), str(j + 1)))

    return json.dumps(conflicts)


def get_relationship_mat(ranking):
    ranks = dict()
    rank_len = get_ranking_len(ranking)

    for i, rank in enumerate(ranking):
        if type(rank) is str:
            ranks[int(rank)] = i
        else:
            for r in rank:
                ranks[int(r)] = i

    return np.matrix([[1 if ranks[i + 1] <= ranks[j + 1] else 0 for j in range(rank_len)] for i in range(rank_len)])


def get_ranking_len(ranking) -> int:
    length = 0
    for i in ranking:
        if type(i) is str:
            length += 1
        else:
            length += len(i)
    return length


def main():
    print(task('["1", ["2","3"],"4", ["5","6","7"],"8","9","10"]', '[["1","2"],["3","4","5"],"6","7","9",["8","10"]]'))


if __name__ == "__main__":
    main()
