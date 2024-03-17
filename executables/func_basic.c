#include <stdio.h>
int add(int a, int b)
{
    return a + b;
}

int main()
{
    int (*p)(int, int);
    p = &add;
    printf("%d\n", p);
    printf("%d\n", (*p)(2, 3));
}