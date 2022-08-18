#!/bin/bash
# Display authorized methods
curl -sI "$1" | grep Allow | cut -c8-
