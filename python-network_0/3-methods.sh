#!/bin/bash
# a script that displays all HTTP methods a server accepts for a given URL
curl -s -X OPTIONS -i "$1" | grep -i "^Allow:" | cut -d ' ' -f2-
