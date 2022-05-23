#!/bin/bash
# Send a POST request to the passed URL, and displays th bodyof the responde
curl -s "$1" -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
