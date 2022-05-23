#!/bin/bash
# This script send a request to a URL passed and display only the statu
curl -s -o /dev/null '%{http_code}' "$1"
