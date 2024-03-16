#include <stdio.h>
#include <string.h>

int main()
{

    char c[20];
    c[0] = 'J';
    c[1] = 'O';
    c[2] = 'N';
    c[3] = '!';
    c[4] = '\0';
    printf("length of c: %d", strlen(c));
    printf("%s", c);
    return 0;
}