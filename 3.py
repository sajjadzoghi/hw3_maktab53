# مقایسه دو لیست بسته به type مقادیر هر لیست میتونه متفاوت باشه. بطور مثال اگر تایپ مقادیر تنها از نوع int باشه،
# مقایسه دو لیست میتونه براساس:
# "تعداد مقادیر هریک از آنها" یا "مجموع مقادیر هریک از آنها" و یا انواع دیگر مقایسه ها باشه.
from functools import total_ordering


@total_ordering
class Mylist:
    def __init__(self, list):
        self.list = list

    def __repr__(self):
        return f'{self.list}'

    def __lt__(self, other):
        return (sum(self.list) / len(self.list)) < (sum(other.list) / len(other.list))


class Mylist2(Mylist):
    def __init__(self, list):
        super().__init__(list)

    def __eq__(self, other):
        return (sum(self.list) / len(self.list)) == (sum(other.list) / len(other.list))


li = [[0, 100, 100], [1, 2], [2.1, 5.4, 3], [1, 4], [100, 100, 100], [90, 90, 90, 90, 90]]
li = [Mylist(item) for item in li]
print(sorted(li))
print(Mylist([0, 100, 100]) > Mylist([1, 2]))
print(Mylist([0, 100, 100]) < Mylist([1, 2]))
print(Mylist([0, 100, 100]) <= Mylist([1,2]))
print(Mylist([0, 100, 100]) >= Mylist([1,2]))
print(Mylist([0, 100, 100]) == Mylist([1,2]))
print(Mylist([0, 100, 100]) != Mylist([1,2]))
