import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://yougile.com/api-v2"
API_TOKEN = os.getenv("YOUGILE_TOKEN")

HEADERS = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {API_TOKEN}"
}
