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
    return np.random.rand(n, 2)


def generator_positive_vector(n: int):
    return np.random.randint(0, 1000, size=n)


def generator_vector(n: int):
    return np.random.rand(n)


def solve_problem(matrix, c, b, n, m):
    print(matrix)
    print(c)
    print(b)
    prob = pulp.LpProblem('problem', pulp.LpMaximize)

    x = pulp.LpVariable.dicts('x', range(n), cat='Binary')

    prob += pulp.lpSum([v * x[i] for i, v in enumerate(c)])

    for i in range(m):
        prob += pulp.lpSum([matrix[i, j] * x[j] for j in range(n)]) >= b[i]

    prob.solve()

    print("Estado:", pulp.LpStatus[prob.status])
    for v in prob.variables():
        print(v.name, "=", v.varValue)


solve_problem(generator_context_free(100, 100), generator_vector(
    100), generator_positive_vector(100), 100, 100)
