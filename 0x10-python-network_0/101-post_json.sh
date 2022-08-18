#!/bin/bash
# Request with a JSON file
curl -sd @"$2" -H "Content-Type: application/json" -X POST "$1"
