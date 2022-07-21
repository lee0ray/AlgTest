class A:
    def __init__(self):
        print("class ---- A ----")


class B(A):
    def __init__(self):
        print("class ---- B ----")
        super(B, self).__init__()


class C(A):
    def __init__(self):
        print("class ---- C ----")
        super(C, self).__init__()


class D(B, C):
    def __init__(self):
        print(D.__mro__)
        print("class ---- D ----")
        super(C, self).__init__()


if __name__ == '__main__':
    d = D()
