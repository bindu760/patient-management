import json
from pathlib import Path


DATABASE_FILE = (
    Path(__file__).resolve().parent.parent
    / "data"
    / "patients.json"
)


def load_patients():
    with open(DATABASE_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def save_patients(patients):
    with open(DATABASE_FILE, "w", encoding="utf-8") as file:
        json.dump(patients, file, indent=4)