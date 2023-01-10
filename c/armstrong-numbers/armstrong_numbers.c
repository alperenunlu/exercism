#include "armstrong_numbers.h"

bool is_armstrong_number(int candidate)
{
    int sum = 0;
    int n = candidate;
    int digits = 0;
    while (n > 0)
    {
        n /= 10;
        digits++;
    }
    n = candidate;
    while (n > 0)
    {
        int digit = n % 10;
        int power = 1;
        for (int i = 0; i < digits; i++)
        {
            power *= digit;
        }
        sum += power;
        n /= 10;
    }
    return sum == candidate;
}
