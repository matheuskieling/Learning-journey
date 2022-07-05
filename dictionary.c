// Implements a dictionary's functionality

#include <ctype.h>
#include <stdbool.h>
#include <stdio.h>
#include "dictionary.h"

// Represents a node in a hash table
typedef struct node
{
    char word[LENGTH + 1];
    struct node *next;
}
node;

// TODO: Choose number of buckets in hash table
const unsigned int N = 26;

// Hash table
node *table[N];

// Returns true if word is in dictionary, else false
bool check(const char *word)
{
    // TODO
    return false;
}

// Hashes word to a number
unsigned int hash(const char *word)
{
    // TODO: Improve this hash function
    return toupper(word[0]) - 'A';
}

// Loads dictionary into memory, returning true if successful, else false
bool load(const char *dictionary)
{
//open dictionary file
	//use fopen
	FILE *dict_file = fopen(dictionary, "r");
	//check if return value is null
	if (dict_file != NULL)
	{
	//determine variables
	char word[LENGHT+1];
	unsigned int = 0;
//read strings from file one at a time
	//use loop for fscan f
	while (fscanf(dict_file, "%s", word) != EOF)
	{
		index = hash(word)
		node *new_node = malloc(sizeof(node));
		if (new_node != NULL)
		{
			return false;
		}
		strcopy(new_node->word, word);
		new_word->next = table[index]
		table[index] = new_node;
		word_count++;
	}
	return true;
	}
	else
	{
		return false;
	}

}

// Returns number of words in dictionary if loaded, else 0 if not yet loaded
unsigned int size(void)
{
    // TODO
    return 0;
}

// Unloads dictionary from memory, returning true if successful, else false
bool unload(void)
{
    // TODO
    return false;
}
