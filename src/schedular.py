import schedule
import time
from src.data_aggregation import aggregate_data

def run_data_aggregation():
    aggregate_data()
    print("Data aggregation completed.")

schedule.every().day.at("13:40").do(run_data_aggregation)

while True:
    schedule.run_pending()
    time.sleep(1)


    #cron schedular