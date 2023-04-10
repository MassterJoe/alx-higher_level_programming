#!/bin/bash
#get the byte size of the http respose header for a given url
curl -s "$1" | wc -c
