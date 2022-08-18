#!/bin/bash
# Get the size in bytes of the response
curl -s "$1" | wc -c
