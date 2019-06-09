"""В первой строке дано три числа, соответствующие некоторой дате date -- год, месяц и день.
Во второй строке дано одно число days -- число дней.

Вычислите и выведите год, месяц и день даты, которая наступит, когда с момента исходной даты date пройдет число дней,
равное days.

Примечание:
Для решения этой задачи используйте стандартный модуль datetime.
Вам будут полезны класс datetime.date для хранения даты и класс datetime.timedelta﻿ для прибавления дней к дате."""

import datetime

x,y,z = input().split()
d = int(input())
date = datetime.date(int(x), int(y), int(z))
delta = datetime.timedelta(days=d)
a = date+delta
print (a.year, a.month, a.day)