#!/bin/bash

# The script accepts two command line arguments. The first argument is a string that defines the word to search for; the second argument specifies
# an output file. Internally, the script stores the value of the first command line argument in a variable named SEARCH_PATTERN and second in a variable named OUTPUT.

# Store command line args
SEARCH_PATTERN="$1"
OUTPUT="$2"

# Downloading Moby Dick file
curl -L -o mobydick.txt https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt 

# Counting occurrences of input search pattern
OCCURRENCES=$(grep -o "$SEARCH_PATTERN" mobydick.txt | wc -l)

# Writing to output file
echo "The search pattern $SEARCH_PATTERN was found $OCCURRENCES time(s)." > "$OUTPUT"
