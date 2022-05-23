#!/bin/bash
# Send a request and display the size of th body
curl -sI "$1" | grep 'Content-Length' | awk '{print $2}'
