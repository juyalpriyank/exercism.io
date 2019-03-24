class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        matrix_list = self.__split()
        return matrix_list[index]

    def column(self, index):
        self.index = index
        matrix_list = self.__split()
        print(matrix_list)
        if self.index % 2:
            self.index += 1
        print(self.index)
        return [n[self.index] for m in matrix_list for n in m.split()]

    def __split(self):
        return self.matrix_string.splitlines()
