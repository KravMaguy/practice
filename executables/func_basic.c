#include <stdio.h>
int add(int a, int b)
{
    return a + b;
}
// int (*Func)(int, int);

int main()
{
    int c;
    int (*p)(int, int);
    p = &add;
    printf("%d\n", p);
    // dereference and execute
    printf("%d\n", (*p)(2, 3));
    c = (*p)(2, 3);
    printf("%d\n", c);

    int added = p(4, 5);
    printf("%d\n", added);

    // review
    // int *P(int, int);
}