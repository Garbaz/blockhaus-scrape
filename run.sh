#!/bin/bash

PERIOD=600

while :; do
    ./scrape.sh
    ./plot.sh
    sleep $PERIOD
done