import time
from pympler import asizeof


MAX_NUM = 100000
DIVISIONS_NUM = 100
part_num = int(MAX_NUM / DIVISIONS_NUM)

dct = {}
times = []
mems = []

for i in range(0, MAX_NUM + 1, part_num):
    if i == 0:
        i = 1
    print(f'Counting for {i} ...')
    start = time.time()
    for k in range(i):
        dct[k] = k
    end = time.time()
    times.append(end - start)
    mems.append(asizeof.asizeof(dct))
    dct.clear()

file_times = open('measures/dict_time.txt', 'w')
file_mems = open('measures/dict_mem.txt', 'w')
file_times.write('measures number: ' + str(DIVISIONS_NUM) + '\n')
file_mems.write('measures number: ' + str(DIVISIONS_NUM) + '\n')
for i in range(DIVISIONS_NUM):
    file_times.write(str(times[i]) + '\n')
    file_mems.write(str(mems[i]) + '\n')
