#!/bin/bash

# Check if URL argument is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send request to the URL and store the response body in a temporary file
response=$(mktemp)
curl -s "$1" > "$response"

# Get the size of the response body in bytes
size=$(wc -c < "$response")

# Display the size of the response body
echo "Size of the response body: $size bytes"

# Clean up temporary file
rm "$response"
