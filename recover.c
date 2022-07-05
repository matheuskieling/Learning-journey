#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

int main(int argc, char *argv[])
{
    //check if correct args
    if (argc != 2)
    {
        printf("Usage: ./recover IMAGE\n");
        return 1;
    }
    //open file
    FILE *input_file = fopen(argv[1], "r");

    //check if file is valid
    if (input_file == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    //create pointer for output
    FILE *output_file = NULL;

    //create space for file
    char *filename = malloc(8 * sizeof(char)); //if it needs more, then write more

    //create buffer
    unsigned char buffer[512];

    //create image counter to print later
    int count = 0;

    //read file loop
    while (fread(buffer, sizeof(char), 512, input_file))
    {
        //1- jpg validation
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff &&
            (buffer[3] & 0xf0) == 0xe0)
        {
            //write the jpg file name
            sprintf(filename, "%03i.jpg", count);

            //open output file
            output_file = fopen(filename, "w");

            //increase counter for next image
            count++;
        }
        if (output_file != NULL)
        {
            //write to output
            fwrite(buffer, sizeof(char), 512, output_file);
        }
    }
    //free memory
    free(filename);

    //close files
    fclose(output_file);
    fclose(input_file);

    return 0;
}