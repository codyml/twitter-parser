# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
#
#   features.py (Python)
#   written by Cody M Leff
#   for Insight coding challenge
#
#   -----------------------------------
#
#   Given an input file containtaining tweets (strings of words
#   composed of lowercase letters, numbers and ASCII-standard
#   punctuation) separated by newline characters, this program
#   outputs the total number of times each word (string of
#   consecutive non-whitespace characters) appears throughout
#   the tweets and the median number of unique words in each
#   tweet, calculated after each tweet is read.  These outputs
#   are written to files at user-defined paths.
#


#   Imports the sys and regular expressions modules

import sys
import re

#   Constants
COLUMN_WIDTH = 28

#   Function: find_unique_words_in_tweet
#   ------------------------------------
#   Uses a regular expression to parse out the words in a line
#   into the 'words' list.  For each word, the function then
#   updates that word's count in the unique_words_in_tweet
#   dictionary or creates an entry if the word has not been
#   encountered in that tweet before.  The function returns the
#   unique_words_in_tweet dictionary.

def find_unique_words_in_tweet(line):
    words = re.findall(r'[^\s]+', line)
    unique_words_in_tweet = {}
    for word in words:
        if word in unique_words_in_tweet:
            unique_words_in_tweet[word] += 1
        else:
            unique_words_in_tweet[word] = 1
    return unique_words_in_tweet


#   Function: calculate_median
#   --------------------------
#   Calculates and returns the median value from a list of one
#   or more positive integers.

def calculate_median(counts):
    length = len(counts)
    if length == 1:
        return counts[0]
    elif length % 2 == 1:
        return counts[length / 2]
    else:
        return (counts[length / 2 - 1] + counts[length / 2]) / 2.0


#   Function: main
#   --------------
#   Execution entry point: this function creates and updates
#   the dictionary of unique words and their counts across all
#   tweets and the unique word counts of each tweet, calculates
#   the median after each tweet, and records all data to the
#   output files.

def main():

    #   Creates references to the invocation arguments
    input_path = sys.argv[1]
    output_ft1_path = sys.argv[2]
    output_ft2_path = sys.argv[3]

    #   This dictionary stores unique words from all tweets read
    #   so far as keys and the number of times they have been
    #   found as the corresponding values.
    unique_words = {}

    #   This list stores the number of unique words found in
    #   each tweet, in the order read from the file.
    unique_word_counts = []

    #   Reads the input file.
    input_file = open(input_path, 'r')

    #   Sets up writing to the output files.
    output_file_ft1 = open(output_ft1_path, 'w')
    output_file_ft2 = open(output_ft2_path, 'w')

    #   Iterates sequentially through each line in the file.
    for line in input_file:

        #   Get a dictionary of unique words and their counts.
        unique_words_in_tweet = find_unique_words_in_tweet(line)

        #   Saves the number of unique words into the list of
        #   unique word counts.
        unique_word_counts.append(len(unique_words_in_tweet))

        #   Merges the unique_words_in_tweet dictionary with the
        #   main unique_words dictionary.
        for word in unique_words_in_tweet:
            if word in unique_words:
                unique_words[word] += unique_words_in_tweet[word]
            else:
                unique_words[word] = unique_words_in_tweet[word]

        #   Calculates and prints the median unique word count
        #   to the output file.
        output_file_ft2.write("{0:.2f}".format(calculate_median(unique_word_counts)) + '\n')

    #   Sort and print out unique_words
    for word in sorted(unique_words):
        output_file_ft1.write(
            word + ' ' * (
                COLUMN_WIDTH - len(word) if
                COLUMN_WIDTH - len(word) > 0 else
                1
            ) + str(unique_words[word]) + '\n')


#   The 'main()' invocation
if __name__ == '__main__':
    main()
