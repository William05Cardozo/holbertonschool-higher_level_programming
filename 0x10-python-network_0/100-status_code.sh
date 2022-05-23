#!/bin/bash
# This script send a request to a URL passed and display only the statu
curl -s -o /dev/null -w '%{http_code}' "$1"
