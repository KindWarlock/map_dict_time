import matplotlib.pyplot as plt
import os
import numpy as np

def read_file(file_name):
    measures = [0, ]
    with open(f'measures/{file_name}', 'r') as file:
        _, num = file.readline().split(': ')
        num = int(num)
        if file_name == 'dict_time.txt':
            for i in range(num):
                measures.append(float(file.readline()))
        else:
            for i in range(num):
                measures.append(int(file.readline()))
    type, _ = file_name.split('_')
    if type == 'dict':
        items = np.arange(0, 100001, 100000 / num)
    else:
        items = np.arange(0, 100000001, 100000000 / num)
    return measures, items


def main():
    files = list(os.walk('measures'))
    for file in files[0][2]:
        measures, items = read_file(file)
        plt.title(file)
        plt.xlabel('Elements')
        if file == 'dict_mem.txt' or file == 'map_mem.txt':
            plt.ylabel('Bytes')
        else:
            plt.ylabel('Seconds')
        plt.plot(items, measures)
        name_no_ext, _ = file.split('.')
        plt.savefig(f'./graphs/{name_no_ext}.png')
        # plt.show()

main()
