
class Matrix:

    def __init__(self, lists):
        self.lists = lists

    def __str__(self):
        for item in self.lists:
            itog = ""
            for i in item:
                itog = itog + str(i) + ' '
            print(itog)

    def __add__(self, other):
        itog_list = other.lists.copy()
        for i in range(len(self.lists)):
            for j in range(len(self.lists[i])):
                try:
                    itog_list[i][j] += self.lists[i][j]
                except IndexError:
                    pass
        return itog_list


a = Matrix([[1, 2, 3], [2, 5, 4]])
a.__str__()
b = Matrix([[1, 2, 3], [4, 5, 6]])
print(a + b)
