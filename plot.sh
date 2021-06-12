#!/bin/bash
python3 plot.py
git add docs/*.svg
git commit -m "Updated plots"
git push

