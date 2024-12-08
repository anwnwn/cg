#!/bin/bash

# Check if the correct number of arguments are provided
if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <dot_file_name>"
    exit 1
fi

# Get the .dot file name from the argument
DOT_FILE_NAME=$1

# Get the directory where the script is located (Wheeler_Graph)
SCRIPT_DIR=$(cd "$(dirname "$0")" && pwd)

# Define paths
TOOLKIT_DIR="$SCRIPT_DIR/Wheeler_Graph_Toolkit"
RECOGNIZER_DIR="$TOOLKIT_DIR/recognizer"
DOT_FILE="$SCRIPT_DIR/$DOT_FILE_NAME"
SEARCHWHEELER_DIR="$SCRIPT_DIR" # Same as the main directory

# Validate the .dot file exists
if [ ! -f "$DOT_FILE" ]; then
    echo "Error: .dot file '$DOT_FILE_NAME' not found in '$SCRIPT_DIR'."
    exit 1
fi

# Validate recognizer directory
if [ ! -d "$RECOGNIZER_DIR" ]; then
    echo "Error: Recognizer directory '$RECOGNIZER_DIR' does not exist. Please check your setup."
    exit 1
fi

# Navigate to recognizer directory
cd "$RECOGNIZER_DIR" || exit

# Run the recognizer command
./bin/recognizer "$DOT_FILE" -w

# Move generated folder to the target location
OUTPUT_FOLDER="out__${DOT_FILE_NAME%.dot}"
if [ -d "$OUTPUT_FOLDER" ]; then
    mv "$OUTPUT_FOLDER" "$SEARCHWHEELER_DIR"
    echo "Success: Wheeler Graph created and moved to $SEARCHWHEELER_DIR."
else
    echo "Error: Output folder '$OUTPUT_FOLDER' not found. Something went wrong with the recognizer command."
    exit 1
fi

exit 0
