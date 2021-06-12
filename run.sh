#!/bin/bash

PERIOD=600

while :; do
    {
        ./scrape.sh
        ./plot.sh
        sleep $PERIOD
    } 2>&1 | tee -a run_log.txt
done