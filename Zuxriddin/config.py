from dotenv import load_dotenv
import os

load_dotenv()

DB_CONFIG = {
    "host": os.getenv("DB_HOST"),
    "port": os.getenv("DB_PORT"),
    "user": os.getenv("DB_USER"),
    "password": os.getenv("DB_PASSWORD"),
    "database": os.getenv("DB_NAME"),
}

SCRAPER_CONFIG = {
    "navigation": "Certifications",
    "card_class_name": "certification-content",
    "card_title": "UI/UX Designer Certification",
    "wait_timeout": 10,
}
