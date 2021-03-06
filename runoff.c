#include <cs50.h>
#include <stdio.h>
#include <string.h>
// Max voters and candidates
#define MAX_VOTERS 100
#define MAX_CANDIDATES 9

// preferences[i][j] is jth preference for voter i
int preferences[MAX_VOTERS][MAX_CANDIDATES];

// Candidates have name, vote count, eliminated status
typedef struct
{
    string name;
    int votes;
    bool eliminated;
}
candidate;

// Array of candidates
candidate candidates[MAX_CANDIDATES];

// Numbers of voters and candidates
int voter_count;
int candidate_count;

// Function prototypes
bool vote(int voter, int rank, string name);
void tabulate(void);
bool print_winner(void);
int find_min(void);
bool is_tie(int min);
void eliminate(int min);

int main(int argc, string argv[])
{
    // Check for invalid usage
    if (argc < 2)
    {
        printf("Usage: runoff [candidate ...]\n");
        return 1;
    }

    // Populate array of candidates
    candidate_count = argc - 1;
    if (candidate_count > MAX_CANDIDATES)
    {
        printf("Maximum number of candidates is %i\n", MAX_CANDIDATES);
        return 2;
    }
    for (int i = 0; i < candidate_count; i++)
    {
        candidates[i].name = argv[i + 1];
        candidates[i].votes = 0;
        candidates[i].eliminated = false;
    }

    voter_count = get_int("Number of voters: ");
    if (voter_count > MAX_VOTERS)
    {
        printf("Maximum number of voters is %i\n", MAX_VOTERS);
        return 3;
    }

    // Keep querying for votes
    for (int i = 0; i < voter_count; i++)
    {

        // Query for each rank
        for (int j = 0; j < candidate_count; j++)
        {
            string name = get_string("Rank %i: ", j + 1);

            // Record vote, unless it's invalid
            if (!vote(i, j, name))
            {
                printf("Invalid vote.\n");
                return 4;
            }
        }

        printf("\n");
    }

    // Keep holding runoffs until winner exists
    while (true)
    {
        // Calculate votes given remaining candidates
        tabulate();

        // Check if election has been won
        bool won = print_winner();
        if (won)
        {
            break;
        }

        // Eliminate last-place candidates
        int min = find_min();
        bool tie = is_tie(min);

        // If tie, everyone wins
        if (tie)
        {
            for (int i = 0; i < candidate_count; i++)
            {
                if (!candidates[i].eliminated)
                {
                    printf("%s\n", candidates[i].name);
                }
            }
            break;
        }

        // Eliminate anyone with minimum number of votes
        eliminate(min);

        // Reset vote counts back to zero
        for (int i = 0; i < candidate_count; i++)
        {
            candidates[i].votes = 0;
        }
    }
    return 0;
}

// Record preference if vote is valid
bool vote(int voter, int rank, string name)
{
    //for each candidate
    for (int i = 0; i < candidate_count; i++)
    {
        //if name of candidate is in candidates list
        if (strcmp(name, candidates[i].name) == 0)
        {
            //update preferences for candidate
            preferences[voter][rank] = i;
            return true;
        }
    }
    //if not in the list return false
    return false;
}

// Tabulate votes for non-eliminated candidates
void tabulate(void)
{
    //for each voter
    for (int i = 0; i < voter_count; i++)
    {
        //for each candidate
        for (int j = 0; j < candidate_count; j++)
        {
            //if candidate is not eliminated
            if (candidates[preferences[i][j]].eliminated == false)
            {
                //add a vote and return
                candidates[preferences[i][j]].votes ++;
                break;
            }
        }
    }
    return;
}

// Print the winner of the election, if there is one
bool print_winner(void)
{
    //for each candidate
    for (int i = 0; i < candidate_count; i++)
    {
        //most will store the candidate name
        string most = candidates[i].name;
        //if the votes of candidate > voters count /2 (50% of voters)
        if (candidates[i].votes > voter_count / 2)
        {
            //print him(er) as a winner
            printf("%s\n", most);
            return true;
        }
    }
    //if nobody wins, return false
    return false;
}

// Return the minimum number of votes any remaining candidate has
int find_min(void)
{
    //create variable to store the min value of votes received
    int min_votes = voter_count;
    //for each candidate
    for (int i = 0; i < candidate_count; i++)
    {
        //if candidate is not eliminated and candidate has less votes then the previous min
        if (candidates[i].eliminated == false && candidates[i].votes < min_votes)
        {
            //update the number of minimum votes
            min_votes = candidates[i].votes;
        }
    }
    return min_votes;
}

// Return true if the election is tied between all candidates, false otherwise
bool is_tie(int min_votes)
{
    //for each candidate
    for (int i = 0; i < candidate_count; i++)
    {
        //if candidate is not eliminated and candidate votes is not min votes
        if (candidates[i].eliminated == false && candidates[i].votes != min_votes)
        {
            //it is not a tie
            return false;
        }
    }
    //if remaining candidates have min votes return as tie
    return true;
}

// Eliminate the candidate (or candidates) in last place
void eliminate(int min_votes)
{
    //for each candidate
    for (int i = 0; i < candidate_count; i++)
    {
        //if candidate votes is equal to min votes
        if (candidates[i].votes == min_votes)
        {
            //eliminate candidate
            candidates[i].eliminated = true;
        }
    }
    return;
}