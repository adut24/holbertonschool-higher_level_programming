#!/bin/bash
# Get the response status
curl -sI -o /dev/null -w "%{http_code}" "$1"
