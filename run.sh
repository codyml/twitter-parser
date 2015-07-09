#!/usr/bin/env bash

# the run script for executing the features

# runs the .py file under the python environment
# arguments:
#   input text
#   output for feature 1
#   output for feature 2
#
python ./src/features.py ./tweet_input/tweets.txt ./tweet_output/ft1.txt ./tweet_output/ft2.txt

