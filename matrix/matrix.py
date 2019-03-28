class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        matrix_list = self.__split()
        __row = []
        for element in matrix_list[index-1].split():
            __row.append(int(element))
        return __row

    def column(self, index):
        self.index = index
        matrix_list = self.__split()
        __column = []
        for each_row in matrix_list:
            row_items = each_row.split()
            __column.append(int(row_items[self.index - 1]))
        return __column

    def __split(self):
        return self.matrix_string.splitlines()
