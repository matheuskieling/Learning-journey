#include <ctype.h>
#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <strings.h>

// Points assigned to each letter of the alphabet
int POINTS[] = {1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10};

int compute_score(string word);

int main(void)
{
    // Get input words from both players
    string word1 = get_string("Player 1: ");
    string word2 = get_string("Player 2: ");

    // Score both words
    int score1 = compute_score(word1);
    int score2 = compute_score(word2);
    printf("score 1 = %i\n", score1);
    printf("score 2 = %i\n", score2);
    // self explanatory

    if (score1 > score2)
    {
        printf("Player 1 wins!\n");
    }

    else if (score2 > score1)
    {
        printf("Player 2 wins!\n");
    }

    else if (score1 == score2)
    {
        printf("Tie!\n");
    }
}

int compute_score(string word)
{
    //define a variable for score starting with value 0
    int score = 0;
    //create array of alphabet
    char alphabet[26][26] = {"A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"};
    //loop to find characters in the word
    for (int i = 0; i < strlen(word); i++)
    {
        //if character is an alphabetic letter
        if (isalpha(word[i]))
        {
            //change to upper case
            word[i] = toupper(word[i]);
            //define variable for loop in alphabet
            int n = 0;
            //while loop number < 25
            while (n < 25)
            {
                //if the letter in word is = to any in the alphabet
                if (word[i] == *alphabet[n])
                {
                    //add to score points = to the index of the letter in points
                    score += POINTS[n];
                }
                n ++;
            }

        }

    }

    return score;
}