# data_collection/collect_attractions.py
import requests
import json
import time

def collect_kerala_attractions():
    """
    Collect Kerala attractions using Google Places API (Free tier)
    No API key needed for basic Place Search
    """
    
    kerala_cities = [
        "Kochi", "Munnar", "Alleppey", "Kumarakom", 
        "Thekkady", "Wayanad", "Kovalam", "Varkala"
    ]
    
    attractions = []
    
    for city in kerala_cities:
        print(f"Collecting attractions for {city}...")
        
        # Use OpenStreetMap Nominatim (free, no key)
        url = "https://nominatim.openstreetmap.org/search"
        params = {
            "q": f"tourist attractions {city} Kerala India",
            "format": "json",
            "limit": 10
        }
        
        response = requests.get(url, params=params, headers={'User-Agent': 'KeralaTravelAI/1.0'})
        places = response.json()
        
        for place in places:
            attraction = {
                "id": f"attr_{len(attractions):03d}",
                "name": place['display_name'].split(',')[0],
                "location": {
                    "city": city,
                    "coordinates": {
                        "lat": float(place['lat']),
                        "lng": float(place['lon'])
                    }
                },
                "details": {
                    "type": classify_attraction_type(place['display_name']),
                    "duration_hours": estimate_duration(place['display_name'])
                }
            }
            attractions.append(attraction)
        
        time.sleep(1)  # Rate limiting
    
    # Enrich with manual data
    attractions = enrich_with_manual_data(attractions)
    
    with open('processed_data/kerala_attractions.json', 'w') as f:
        json.dump({"attractions": attractions}, f, indent=2)
    
    return attractions

def classify_attraction_type(name):
    """Classify attraction by name"""
    name_lower = name.lower()
    
    if any(word in name_lower for word in ['temple', 'church', 'mosque', 'synagogue']):
        return 'religious'
    elif any(word in name_lower for word in ['beach', 'lake', 'waterfall', 'hill']):
        return 'nature_scenic'
    elif any(word in name_lower for word in ['museum', 'gallery', 'palace', 'fort']):
        return 'cultural_historical'
    elif any(word in name_lower for word in ['park', 'sanctuary', 'reserve']):
        return 'wildlife_nature'
    else:
        return 'general'

def estimate_duration(name):
    """Estimate typical visit duration"""
    name_lower = name.lower()
    
    if any(word in name_lower for word in ['museum', 'gallery', 'sanctuary']):
        return 2
    elif any(word in name_lower for word in ['temple', 'church']):
        return 1
    elif any(word in name_lower for word in ['beach', 'hill', 'trek']):
        return 3
    else:
        return 2

def enrich_with_manual_data(attractions):
    """Add manually curated Kerala highlights"""
    
    kerala_highlights = [
        {
            "id": "attr_munnar_tea",
            "name": "Munnar Tea Gardens",
            "location": {"city": "Munnar", "coordinates": {"lat": 10.0889, "lng": 77.0595}},
            "details": {
                "type": "nature_scenic",
                "duration_hours": 3,
                "entry_fee_inr": 50,
                "best_time_of_day": "morning"
            },
            "insider_tips": ["Visit during sunrise", "Book factory tour in advance"],
            "best_months": ["Sep", "Oct", "Nov", "Dec", "Jan", "Feb"]
        },
        {
            "id": "attr_backwater_cruise",
            "name": "Alleppey Backwater Houseboat",
            "location": {"city": "Alleppey", "coordinates": {"lat": 9.4981, "lng": 76.3388}},
            "details": {
                "type": "unique_experience",
                "duration_hours": 8,
                "price_range_inr": [8000, 25000],
                "best_time_of_day": "all_day"
            },
            "insider_tips": ["Book AC houseboats in summer", "Sunset cruises most romantic"],
            "best_months": ["Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]
        }
        # Add 15-20 more Kerala highlights manually
    ]
    
    return attractions + kerala_highlights

if __name__ == "__main__":
    attractions = collect_kerala_attractions()
