import requests, json, time

cities = ["Kochi", "Thiruvananthapuram", "Kozhikode", "Thrissur", "Munnar", "Wayanad"]
restaurants = []

for city in cities:
    print(f"Fetching restaurants in {city}...")
    query = f"""
    [out:json][timeout:60];
    area["name"="{city}"]->.a;
    node["amenity"="restaurant"](area.a);
    out center;
    """
    r = requests.get("https://overpass-api.de/api/interpreter", params={"data": query})
    if r.status_code != 200:
        print(f"Skipping {city} (status {r.status_code})")
        continue
    try:
        data = r.json()
    except Exception:
        print(f"{city}: Could not parse JSON")
        continue

    for i, el in enumerate(data.get("elements", []), 1):
        tags = el.get("tags", {})
        restaurants.append({
            "id": f"rest_{len(restaurants)+1:03}",
            "name": tags.get("name", "Unknown"),
            "location": {
                "city": city,
                "area": tags.get("addr:suburb", ""),
                "coordinates": {"lat": el.get("lat"), "lng": el.get("lon")}
            },
            "cuisine": {
                "primary": tags.get("cuisine", "Kerala Traditional"),
                "specialties": [],
                "dietary_options": ["vegetarian", "non_vegetarian"]
            },
            "pricing": {
                "avg_cost_per_person_inr": 300,
                "budget_category": "mid_range",
                "value_rating": 4.0
            },
            "experience": {
                "ambiance": "local",
                "seating": ["indoor"],
                "reservations_required": False,
                "wait_time_peak": "15-30 mins"
            },
            "ratings": {
                "food_quality": 0,
                "service": 0,
                "ambiance": 0,
                "google_rating": 0
            },
            "signature_dishes": [],
            "best_for": [],
            "influencer_mentions": []
        })
    time.sleep(2)  
with open("kerala_restaurants.json", "w", encoding="utf-8") as f:
    json.dump({"restaurants": restaurants}, f, indent=2, ensure_ascii=False)

print(f"Saved {len(restaurants)} restaurants.")
