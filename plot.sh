#!/bin/bash
git pull
python3 plot.py
git add docs/*.svg data.csv
git commit -m "Updated plots"
git push

