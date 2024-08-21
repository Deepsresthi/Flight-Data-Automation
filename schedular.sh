#!/bin/bash 

source venv/bin/activate 

export PYTHONPATH="/Users/ishasa-blrm20/Desktop/Flight Data Automation"

cd "/Users/ishasa-blrm20/Desktop/Flight Data Automation/src" || exit

python3 data_aggregation.py >> "/Users/ishasa-blrm20/Desktop/Flight Data Automation/logfile.log" 2>&1