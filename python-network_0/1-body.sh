#!/bin/bash
# a script that displays the body of a GET request only if the final status code is 200, following redirects
curl -s -L -o /tmp/body -w "%{http_code}" "$1" | grep -q "^200$" && cat /tmp/body
