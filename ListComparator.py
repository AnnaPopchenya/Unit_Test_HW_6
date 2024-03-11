class ListComparator:
    def __init__(self, list1, list2):
        self.list1 = list1
        self.list2 = list2

    def calculate_average(self, lst):
        return sum(lst) / len(lst) if len(lst) > 0 else 0

    def compare_lists(self):
        avg_list1 = self.calculate_average(self.list1)
        avg_list2 = self.calculate_average(self.list2)

        if avg_list1 > avg_list2:
            return "Первый список имеет большее среднее значение"
        elif avg_list2 > avg_list1:
            return "Второй список имеет большее среднее значение"
        else:
            return "Средние значения равны"


# Пример использования
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

comparator = ListComparator(list1, list2)
result = comparator.compare_lists()
print(result)