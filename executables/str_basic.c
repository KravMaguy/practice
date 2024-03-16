#include <stdio.h>

int main()
{
    // can fix by implicitly or explicit adding of null
    // re c[20] || c[x]='\0'
    char c[4];
    c[0] = 'J';
    c[1] = 'O';
    c[2] = 'N';
    c[3] = '!';
    printf("%s", c);
    return 0;
}