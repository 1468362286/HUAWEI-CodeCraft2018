import copy

EPS = 1e-10


class matrix:

    def __init__(self, arg_1, arg_2=0, arg_3=0.0):
        if isinstance(arg_1, list):
            self.rows_ = len(arg_1)
            self.cols_ = len(arg_1[0])
            self.__matrix = arg_1
            self.shape = (self.rows_, self.cols_)
        else:
            if isinstance(arg_1, int) and isinstance(arg_2, int):
                self.rows_ = arg_1
                self.cols_ = arg_2
                self.__matrix = [[arg_3] * arg_2 for i in range(arg_1)]
                self.shape = (arg_1, arg_2)
            else:
                raise TypeError("parameters wrong")