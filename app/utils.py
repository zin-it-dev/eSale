import json, os

base_dir = os.path.join(os.path.dirname(__file__), "database")


def load_data(filename: str):
    with open(
        os.path.join(base_dir, "json", filename),
        encoding="utf-8",
    ) as f:
        return json.load(f)
