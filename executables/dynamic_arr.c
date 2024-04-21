#include <stdio.h>
#include <stdlib.h>

/*
 * This stores the total number of books in each shelf.
 */
int *shelfSizes;

/*
 * This stores the total number of pages in each book of each shelf.
 * The rows represent the shelves and the columns represent the books.
 */
int **pagesPerBook;

int main()
{

    int total_number_of_shelves;
    scanf("%d", &total_number_of_shelves);

    int total_number_of_queries;
    scanf("%d", &total_number_of_queries);
    // memory shelfSizes store the number of books on each shelf.
    // pagesPerBook multidimentional arr the number of pages in each book for each shelf.
    // in loop set the initial values in shelfSizes to zero/no books.

    // e.g. if three shelves space for 3 pointer to int (how many books on a given shelf)
    shelfSizes = (int *)malloc(total_number_of_shelves * sizeof(int));
    // type pointer to pointer to int (variable type adress that points to an adress that contains the adress
    // of the size of the book)
    pagesPerBook = (int **)malloc(total_number_of_shelves * sizeof(int *));

    for (int i = 0; i < total_number_of_shelves; i++)
    {
        shelfSizes[i] = 0;
        pagesPerBook[i] = (int *)malloc(1100 * sizeof(int));
    }

    while (total_number_of_queries--)
    {
        int type_of_query;
        scanf("%d", &type_of_query);

        if (type_of_query == 1)
        {
            /*
             * Process the query of first type here.
             */
            int x, y;
            scanf("%d %d", &x, &y);
            // 1 x y : Insert a book with y pages at the end of the xth shelf.
            shelfSizes[x] = shelfSizes[x] + 1;
            pagesPerBook[x][shelfSizes[x] - 1] = y;
        }
        else if (type_of_query == 2)
        {
            int x, y;
            scanf("%d %d", &x, &y);
            printf("%d\n", *(*(pagesPerBook + x) + y));
        }
        else
        {
            int x;
            scanf("%d", &x);
            printf("%d\n", *(shelfSizes + x));
        }
    }

    if (shelfSizes)
    {
        free(shelfSizes);
    }

    for (int i = 0; i < total_number_of_shelves; i++)
    {
        if (*(pagesPerBook + i))
        {
            free(*(pagesPerBook + i));
        }
    }

    if (pagesPerBook)
    {
        free(pagesPerBook);
    }

    return 0;
}