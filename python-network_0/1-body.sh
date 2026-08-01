#!/bin/bash
# a script that displays the body of a GET request only if status code is 200
curl -s -o /tmp/body -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/body
