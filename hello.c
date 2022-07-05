#include <stdio.h>
#include <cs50.h>

int main(void)
{

    // This code was wrote at week 1 CS50 course with the intent to test what I could figure out without searching online.
    // Got a few errors, but it worked like a charm at the end.
    // would like to add a bit of pause between input and output, so it feels more organic.
    // Hope you like it! Hugs from Brazil!

    // get user input for name
    string name = get_string("\nHey there! Been waiting for you. First, what's your name?\n\n");

    //output
    printf("Hello, %s", name);
    printf("\n");
}