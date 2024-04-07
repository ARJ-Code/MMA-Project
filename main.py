import random
import numpy as np
import pulp


def generator_context_free(n: int, m: int):
    q = [(0, m)]

    matrix = np.zeros((n, m), dtype=int)

    for i in range(n):
        if len(q) == 0:
            break
        ind = random.randint(0, len(q)-1)

        a, b = q[ind]
        q.remove(q[ind])

        k = random.randint(0, b-a)
        samples = random.sample(range(a, b), k)

        samples.sort()

        for j in range(len(samples)-1):
            l = samples[j]+1
            r = samples[j+1]

            if r-l > 0:
                q.append((l, r))

        for j in samples:
            matrix[j][i] = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                continue
            matrix[i][j] = random.randint(-100, 100)

    return matrix


def generator_row2(n: int):
    return np.random.randint(-1000, 1000, size=(2, n))


def generator_positive_vector(n: int):
    return np.random.randint(0, 1000, size=n)


def generator_vector(n: int):
    return np.random.randint(-100000, 100000, size=n)


def solve_problem(matrix, c, b, n, m, row2=False):
    prob = pulp.LpProblem('problem', pulp.LpMaximize)

    x = pulp.LpVariable.dicts('x', range(n), cat='Binary')

    prob += pulp.lpSum([v * x[i] for i, v in enumerate(c)])

    for i in range(m):
        prob += pulp.lpSum([matrix[i, j] * x[j] for j in range(n)]) >= b[i]

    prob.solve()

    return pulp.LpStatus[prob.status] == 'Optimal'


m1 = np.array([[10, -3, -3, 4, 0, 0, 0],
              [0, -5, 0, 0, 0, 0, 0],
               [-10, 0, 0, 0, 2, 8, 0],
               [0, 0, 0, 0, 0, 4, 6]])
b1 = [3, -2, 5, 3]
c1 = [7, 69, 8, 0, -44, 35, -23]

m2 = np.array([[0, 0, 4, -8, 0, 0],
               [0, 0, 0, 8, -1, 0],
               [0, 0, 6, 0, 0, -4],
               [0, 0, 0, 0, 0, 6],
               [0, 3, 0, 0, 0, 0],
               [-9, 7, 0, 0, 0, 0]])

b2 = [2, -2, 2, 3, 0, -2]
c2 = [72, -169, -8, -120, -44, 35]


m3 = np.array([[0, -1, 6, -7, 0, 0],
               [-6, 0, 0, 0, -10, 0],
               [0, 0, 0, 0, -1, 9],
               [8, 0, -7, 0, 0, 0],
               [0, 0, 10, 0, 0, 0]])

b3 = [5, -6, 6, 1, 0]
c3 = [-1372, 2169, -228, -120, -44, 122]

solve_problem(m1, c1, b1, 7, 4)
solve_problem(m2, c2, b2, 6, 6)
solve_problem(m3, c3, b3, 6, 5)

c = 0
for _ in range(1000):
    c += solve_problem(generator_row2(1000), generator_vector(
        1000), generator_vector(2), 1000, 2)
print(c)
