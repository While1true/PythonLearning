#encoding:utf_8

import re
import datetime as tt
from itertools import *
# m = re.subn("output_(\d{4})", "122","aoutput_1986output_1986.txt")
#
# for i in m:
#    print(i)

# 有一个文件，文件名为output_1981.10.21.txt 。
# 下面使用Python： 读取文件名中的日期时间信息，并找出这一天是周几。
# 将文件改名为output_YYYY-MM-DD-W.txt
# (YYYY:四位的年，MM：两位的月份，DD：两位的日，W：一位的周几，并假设周一为一周第一天)
data="output_2017.12.29.txt"
m=re.search("^(?P<start>output_)(?P<year>\d{4})\.(?P<month>\d{2})\.(?P<day>\d{2})\.(?P<end>txt$)",data)
print(m.group(0), m.group("start"), m.group("year"), m.group("month"), m.group('day'), m.group('end'))

week=tt.date(int(m.group("year")),int(m.group("month")),int(m.group('day'))).weekday()
print(week)
a=data.replace(".","-",2).replace(".","-%d." % week)
print(a)

def height_class(h):
    if h > 180:
        return "tall"
    elif h < 160:
        return "short"
    else:
        return "middle"

friends = [191, 158, 159, 165, 170, 177, 181, 182, 190]

friends = sorted(friends, key = height_class)
print(friends)
for m, n in groupby(friends, key = height_class):
    print(m)
    print(list(n))