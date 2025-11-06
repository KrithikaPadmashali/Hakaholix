# data_collection/curate_influencers.py
from youtube_transcript_api import YouTubeTranscriptApi
import json
import re

def curate_kerala_influencers():
    """
    Manually curate Kerala travel influencers
    Note: YouTube API requires key, but you can do this manually for 15-20 influencers
    """
    
    influencers = [
        {
            "id": "inf_mark_wiens",
            "name": "Mark Wiens",
            "platform": "YouTube",
            "channel_url": "https://youtube.com/@MarkWiens",
            "kerala_videos": [
                {
                    "title": "Ultimate Kerala Food Tour",
                    "video_id": "dQw4w9WgXcQ",  # Replace with actual
                    "upload_date": "2023-01-15",
                    "key_moments": [
                        {"timestamp": "5:23", "description": "Kayees Biryani recommendation", "location": "Kochi"},
                        {"timestamp": "12:45", "description": "Appam and stew breakfast", "location": "Fort Kochi"}
                    ]
                }
            ],
            "travel_style": {
                "budget": "mid_range",
                "focus": ["food", "culture"],
                "personality": ["enthusiastic", "authentic"]
            },
            "kerala_tips": [
                "Always try toddy with fish curry",
                "Best food is in local homes, not tourist restaurants"
            ]
        },
        {
            "id": "inf_karl_rock",
            "name": "Karl Rock",
            "platform": "YouTube",
            "kerala_videos": [...],
            "travel_style": {"budget": "budget", "focus": ["culture", "budget_tips"]}
        },
        {
            "id": "inf_tanya_khanijow",
            "name": "Tanya Khanijow",
            "platform": "YouTube",
            "kerala_videos": [...],
            "travel_style": {"budget": "mid_range", "focus": ["solo_female", "adventure"]}
        }
        # Add 12-15 more influencers manually
    ]
    
    with open('processed_data/kerala_influencers.json', 'w') as f:
        json.dump({"influencers": influencers}, f, indent=2)
    
    return influencers

if __name__ == "__main__":
    influencers = curate_kerala_influencers()# data_collection/curate_influencers.py
from youtube_transcript_api import YouTubeTranscriptApi
import json
import re

def curate_kerala_influencers():
    """
    Manually curate Kerala travel influencers
    Note: YouTube API requires key, but you can do this manually for 15-20 influencers
    """
    
    influencers = [
        {
            "id": "inf_mark_wiens",
            "name": "Mark Wiens",
            "platform": "YouTube",
            "channel_url": "https://youtube.com/@MarkWiens",
            "kerala_videos": [
                {
                    "title": "Ultimate Kerala Food Tour",
                    "video_id": "dQw4w9WgXcQ",  # Replace with actual
                    "upload_date": "2023-01-15",
                    "key_moments": [
                        {"timestamp": "5:23", "description": "Kayees Biryani recommendation", "location": "Kochi"},
                        {"timestamp": "12:45", "description": "Appam and stew breakfast", "location": "Fort Kochi"}
                    ]
                }
            ],
            "travel_style": {
                "budget": "mid_range",
                "focus": ["food", "culture"],
                "personality": ["enthusiastic", "authentic"]
            },
            "kerala_tips": [
                "Always try toddy with fish curry",
                "Best food is in local homes, not tourist restaurants"
            ]
        },
        {
            "id": "inf_karl_rock",
            "name": "Karl Rock",
            "platform": "YouTube",
            "kerala_videos": [...],
            "travel_style": {"budget": "budget", "focus": ["culture", "budget_tips"]}
        },
        {
            "id": "inf_tanya_khanijow",
            "name": "Tanya Khanijow",
            "platform": "YouTube",
            "kerala_videos": [...],
            "travel_style": {"budget": "mid_range", "focus": ["solo_female", "adventure"]}
        }
        # Add 12-15 more influencers manually
    ]
    
    with open('processed_data/kerala_influencers.json', 'w') as f:
        json.dump({"influencers": influencers}, f, indent=2)
    
    return influencers

if __name__ == "__main__":
    influencers = curate_kerala_influencers()
