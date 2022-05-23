#!/bin/bash
# This script send a GET request to the URL, and displays the body of th respone
curl -s -X GET "$1" -H "X-School-User-Id: 98" 
