import time
import datetime
import schedule

from ccu3 import runSchedule

print("\n\nStarting Script at :: {}".format(datetime.datetime.today()))
print("\nBackup Script for HomeMatic CCU(3).")
print("Backup to Minio or another S3-compatible storage.\n")


def start():
    print("Setting up scheduler...\n\n")
    schedule.every().day.at("00:15").do(runSchedule)
    # runSchedule()
    while True:
        schedule.run_pending()
        time.sleep(60)


if __name__ == '__main__':
    start()
