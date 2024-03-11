import pytest
from ListComparator import ListComparator



def test_compare_lists():
    list1 = [1, 2, 3, 4, 5]
    list2 = [6, 7, 8, 9, 10]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_lists() == "Второй список имеет большее среднее значение"

def test_compare_lists_equal():
    list1 = [1, 2, 3, 4, 5]
    list2 = [1, 2, 3, 4, 5]
    comparator = ListComparator(list1, list2)
    assert comparator.compare_lists() == "Средние значения равны"