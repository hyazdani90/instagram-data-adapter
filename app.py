import json
from datetime import datetime

accounts = [
    "shila.fastfood",
    "pizzasib360",
    "atawich.ir",
    "chickenfamily.co",
    "perperookfastfood"
]

data = {
    "date": datetime.now().strftime("%Y-%m-%d"),
    "accounts": []
}

for username in accounts:
    data["accounts"].append({
        "username": username,
        "status": "collector_ready"
    })

print(json.dumps(data, indent=2))
