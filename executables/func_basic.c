int add(int a, int b)
{
    return a + b;
}

int main()
{
    int *p(int, int);
    p = &add;
    printf("%d", p);
}