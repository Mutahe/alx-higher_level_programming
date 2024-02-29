#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Send GET request and display body if response status code is 200
response=$(curl -s -o response.txt -w "%{http_code}" "$url")

status_code=$(tail -n1 response.txt)

if [ "$status_code" = "200" ]; then
    echo "Response body:"
    cat response.txt
else
    echo "Response status code: $status_code"
fi

# Clean up response.txt
rm -f response.txt
