#include <iostream>
#include <time.h>
#include <map>
#include <fstream>

const int DIVISIONS_NUM = 100;
const int MAX_NUM = 100000000;

int main() {
    int part_num = MAX_NUM / DIVISIONS_NUM;
    time_t start, stop;
    double times[DIVISIONS_NUM];
    unsigned long mems[DIVISIONS_NUM];
    int cnt = 0;
    for (int i = 1; i <= MAX_NUM; i += part_num) {
        std::cout << "Counting for n=" << i << " ...\n";
        std::map <int, int> mp;
        time(&start);
        for (int k = 0; k < i; k++) {
            mp[k] = k;
        }
        time(&stop);

        times[cnt] = difftime(stop, start);
        
        mems[cnt++] = sizeof(mp) + 8 * i;

        mp.clear();
        if (i == 1) {
            i = 0;
        }
    }
    std::ofstream file_t("measures/map_time.txt");
    std::ofstream file_m("measures/map_mem.txt");
    file_t << "measures number: " << DIVISIONS_NUM << '\n';
    file_m << "measures number: " << DIVISIONS_NUM << '\n';
    for (int i = 0; i < DIVISIONS_NUM; i++) {
        file_t << times[i] << '\n';
        file_m << mems[i] << '\n';
    }
    file_t.close();
    file_m.close();
    return 0;
}