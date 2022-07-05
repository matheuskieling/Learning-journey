#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <math.h>

int index(string text);
float count_letters(string text);
float count_words(string text);
float count_sentences(string text);

int main(void)
{
    //get user prompt
    string text = get_string("Input text: ");
    //calculate everything
    index(text);
}
// how many letters?
float count_letters(string text)
{
    // define variable
    float num_letters = 0;
    //loop to check every letter and count + 1 if is a alphabetic character
    for (int i = 0; i < strlen(text); i++)
    {
        if (isalpha(text[i]))
        {
            num_letters++;
        }
    }
    //return the number of letters to be used later
    return num_letters;
}
// how many words?
float count_words(string text)
{
    //same as letters
    float num_words = 1;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == ' ')
        {
            num_words++;
        }
    }
    return num_words;
}

// how many sentences?
float count_sentences(string text)
{
    //same as letters
    float num_sentences = 0;
    for (int i = 0; i < strlen(text); i++)
    {
        if (text[i] == '.' || text[i] == '!' || text[i] == '?')
        {
            num_sentences++;
        }
    }
    return num_sentences;
}
// calculate index and print
int index(string text)
{
    float L = (100 * (float)count_letters(text) / count_words(text));
    float S = (100 * (float)count_sentences(text) / count_words(text));
    int index = round(0.0588 * L - 0.296 * S - 15.8);
    if (index < 1)
    {
        return printf("Before Grade 1\n");
    }
    else if (index >= 16)
    {
        return printf("Grade 16+\n");
    }
    else
    {
        return printf("Grade %i\n", index);
    }
}