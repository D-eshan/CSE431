#include <iostream>
#include <ctime>
#include <map>
#include <unordered_set>

using namespace std;

const int N = 10000;

void ClockBinaryTree()
{
    multimap<int, int> m;

    std::clock_t start_time = std::clock();
    for (int i = 0; i < N; ++i)
    {
        m.insert({ i, i });
    }
    std::clock_t tot_time = std::clock() - start_time;
    std::cout << "Time: "
        << ((double)tot_time) / (double)CLOCKS_PER_SEC
        << " seconds" << std::endl;
}


void ClockHashTable()
{
    unordered_multiset<int> m;
    std::clock_t start_time = std::clock();

    for (int i = 0; i < N; ++i)
    {
        m.insert(i);
    }

    std::clock_t tot_time = std::clock() - start_time;
    std::cout << "Time: "
        << ((double)tot_time) / (double)CLOCKS_PER_SEC
        << " seconds" << std::endl;
}

int main()
{
    ClockBinaryTree();
    ClockHashTable();
}
