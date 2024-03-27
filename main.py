import random
import exact

class Test:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


test1 = [[10,-3,-3,4,0,0,0],[0,-5,0,0,0,0,0],[-10,0,0,0,2,8,0],[0,0,0,0,0,4,6]]
test2 = [[0,0,4,-8,0,0],[0,0,0,8,-1,0],[0,0,6,0,0,-4],[0,0,0,0,0,6],[0,3,0,0,0,0],[-9,7,0,0,0,0]]
test3 = [[0,-1,6,-7,0,0],[-6,0,0,0,-10,0],[0,0,0,0,-1,9],[8,0,-7,0,0,0],[0,0,10,0,0,0]]
test4 = [[5,-9,0,0,0,5],[0,1,0,0,3,0],[0,-8,0,0,0,0],[-10,0,0,-1,0,0],[0,0,0,9,0,0],[-3,0,0,0,0,0]]
test5 = [[0,0,0,3,0,-10],[-5,0,-8,0,0,6],[0,0,0,0,2,0],[0,0,0,0,3,4],[0,0,0,-4,0,0]]

list_a = [test1,test2, test3, test4, test5] 
tests = []
for i in range (5):
    list_b = []
    list_c = []
    for j in range (len(list_a[i])):
        b = random.randint(-10,10)
        c = random.randint(-10,10)
        list_b.append(b)
        list_c.append(c)
    tests.append(Test(list_a[i],list_b,list_c))

solutions = []
for i in range(len(tests)):
    solutions.append(exact.Problem(tests[i].a, tests[i].b, tests[i].c).solve())