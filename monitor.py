#!/usr/bin/env python3
import time
import shutil
import logging

# Setup logging to the System Journal
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def check_disk_usage():
    total, used, free = shutil.disk_usage("/")
    percent_used = (used / total) * 100
    
    if percent_used > 80:
        logging.warning(f"DISK CRITICAL: {percent_used:.2f}% used!")
    else:
        logging.info(f"Disk Healthy: {percent_used:.2f}% used.")

if __name__ == "__main__":
    logging.info("Starting Linux Health Monitor Service...")
    while True:
        check_disk_usage()
        time.sleep(60) # Check every minute