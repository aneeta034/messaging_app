import os
import time
from supabase import create_client, Client
from dotenv import load_dotenv
import logging
from datetime import datetime


load_dotenv()


url: str = os.getenv("SUPABASE_URL")
key: str = os.getenv("SUPABASE_KEY")
supabase: Client = create_client(url, key)


logging.basicConfig(
    filename="job_logs.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S"
)


def check_flag():
    try:
        response = supabase.table("organization").select("*").eq("flag", 1).execute()
        organizations = response.data

        for org in organizations:
            org_id = org["id"]
            org_name = org["name"]
            logging.info(f"Flag is 1 for Organization ID: {org_id}, Name: {org_name}. Triggering another job...")
            trigger_another_job(org_id, org_name)

    except Exception as e:
        logging.error(f"Error: {e}")


def trigger_another_job(org_id, org_name):
    logging.info(f"Job triggered for Organization ID: {org_id}, Name: {org_name}")
    print(f"Job triggered for Organization ID: {org_id}, Name: {org_name}")


if __name__ == "__main__":
    while True:
        check_flag()
        time.sleep(5)  