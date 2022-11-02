class P():
    def function1(self):
        print("Creating class P")

class Q(P):
    def function2(self):
        print('class Q')

class R(Q):
    def function3(self):
        print("class R")

class S(Q):
    def function4(self):
        print('class S')

class T(R,S):
    def function5(self):
        print("class T")

# creating object of class T
Z=T()

# calling functions
Z.function5()
Z.function4()
Z.function3()
Z.function2()
Z.function1()
