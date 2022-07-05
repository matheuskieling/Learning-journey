// Modifies the volume of an audio file

#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

// Number of bytes in .wav header
const int HEADER_SIZE = 44;

int main(int argc, char *argv[])
{
    // Check command-line arguments
    if (argc != 4)
    {
        printf("Usage: ./volume input.wav output.wav factor\n");
        return 1;
    }

    // Open files and determine scaling factor
    FILE *input = fopen(argv[1], "r");
    if (input == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    FILE *output = fopen(argv[2], "w");
    if (output == NULL)
    {
        printf("Could not open file.\n");
        return 1;
    }

    float factor = atof(argv[3]);

    //declaration of header array
    uint8_t header[HEADER_SIZE];

    //read 44 bytes from file imput.wav
    fread(&header, sizeof(header), 1, input);
    //write 44 bytes to output.wav
    fwrite(&header, sizeof(header), 1, output);

    //declaration of buffer(temp) var to store 2 bytes
    int16_t buffer;
    //loop in input.wav
    //read 2 bytes from input
    while (fread(&buffer, sizeof(buffer), 1, input))
    {
        //multiply 2 bytes with factor
        buffer *= factor;
        //write to output.wav
        fwrite(&buffer, sizeof(buffer), 1, output);
    }
    // Close files
    fclose(input);
    fclose(output);
}
