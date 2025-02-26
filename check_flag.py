import os
import time
from supabase import create_client, Client
from dotenv import load_dotenv
import logging
from datetime import datetime

# Load environment variables
load_dotenv()

# Supabase setup
url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)

# Logging setup
logging.basicConfig(
    filename="job_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)

# Function to check the flag
def check_flag():
    try:
        # Query the organization table
        response = supabase.table("organization").select("*").eq("flag", 1).execute()
        organizations = response.data

        for org in organizations:
            org_id = org["id"]
            org_name = org["name"]
            logging.info(f"Flag is 1 for Organization ID: {org_id}, Name: {org_name}. Triggering another job...")
            trigger_another_job(org_id, org_name)

    except Exception as e:
        logging.error(f"Error: {e}")

# Function to trigger another job
def trigger_another_job(org_id, org_name):
    # Replace this with the logic to trigger your other job
    logging.info(f"Job triggered for Organization ID: {org_id}, Name: {org_name}")
    print(f"Job triggered for Organization ID: {org_id}, Name: {org_name}")

# Main loop to run the job every 5 seconds
if __name__ == "__main__":
    while True:
        check_flag()
        time.sleep(5)  # Adjust the interval as needed