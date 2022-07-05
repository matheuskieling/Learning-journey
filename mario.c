#include <cs50.h>
#include <stdio.h>

void spaces();
void blocks();

int main(void)
{
    int height;

    do
    {
        height = get_int("Type a height: ");
    }
    while (height < 0);

    int block_count = height - (height -1);
    int space_count = height - 1;

    for (int i = 0; i < height; i++)
    {
        spaces(space_count);
        blocks(block_count);
        printf("  ");
        blocks(block_count);
        spaces(space_count);
        printf("\n");
        block_count ++;
        space_count --;
    }
}

void spaces(int space_count)
{
    for (int i = 0; i < space_count; i++)
    {
        printf(" ");
    }
}
void blocks(int block_count)
{
    for (int i = 0; i < block_count; i++)
    {
        printf("#");
    }
}
