#include <stdio.h>
#include <string.h>

int main()
{

    char c[] = "John";
    printf("bytes : %d", sizeof(c));
    printf("length : %d", strlen(c));
    printf("%s\n", c);
    for (int i = 0; i < strlen(c); i++)
    {
        printf("%c\n", c[i]);
        printf("%c\n", *(c + i));
        printf("%p\n", c + i);
    }
    return 0;
}