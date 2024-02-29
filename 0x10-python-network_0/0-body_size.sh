#!/bin/bash

# Check if a URL is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Send request and get response body size in bytes
body_size=$(curl -sI "$url" | awk '/Content-Length/ {print $2}')

# Check if Content-Length header exists in the response
if [ -z "$body_size" ]; then
    echo "10"
    exit 1
fi

echo "Body size: $body_size bytes"
