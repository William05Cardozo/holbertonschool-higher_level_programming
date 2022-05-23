#!/bin/bash
# This script send a GET request to the URL, and displays the body of th respone
curl "$1" -sX GET -H "X-HolbertonSchool-User-Id:98"
