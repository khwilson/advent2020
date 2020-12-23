#include<cstdlib>
#include<iostream>


int main() {
    const size_t NUM_VALS = 1000000;
    const uint64_t NUM_ROUNDS = 10000000;

    uint64_t *next = (uint64_t*) malloc(NUM_VALS * sizeof(uint64_t));
    next[2 - 1] = 1 - 1;
    next[1 - 1] = 5 - 1;
    next[5 - 1] = 6 - 1;
    next[6 - 1] = 9 - 1;
    next[9 - 1] = 4 - 1;
    next[4 - 1] = 7 - 1;
    next[7 - 1] = 8 - 1;
    next[8 - 1] = 3 - 1;
    next[3 - 1] = 9;

    for (size_t i = 9; i < NUM_VALS; ++i) {
        next[i] = i + 1;
    }
    next[NUM_VALS - 1] = 2 - 1;

    uint64_t cur_cup = 2 - 1;
    for (u_int64_t round_num = 0; round_num < NUM_ROUNDS; ++round_num) {

        const uint64_t first = next[cur_cup],
                       second = next[first],
                       third = next[second];

        uint64_t next_cup = (cur_cup > 0) ? ((cur_cup - 1) % NUM_VALS) : (NUM_VALS - 1);
        while (next_cup == first || next_cup == second || next_cup == third) {
            next_cup = (next_cup > 0) ? ((next_cup - 1) % NUM_VALS) : (NUM_VALS - 1);
        }

        next[cur_cup] = next[third];
        uint64_t tmp = next[next_cup];
        next[next_cup] = first;
        next[third] = tmp;

        cur_cup = next[cur_cup];
    }

    std::cout << ((next[0] + 1) * (next[next[0]] + 1)) << std::endl;
}