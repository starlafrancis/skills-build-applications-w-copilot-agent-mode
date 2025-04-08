# Test data for populating the octofit_db database

test_data = {
    "users": [
        {"username": "thundergod", "email": "thundergod@mhigh.edu", "password": "password123"},
        {"username": "metalgeek", "email": "metalgeek@mhigh.edu", "password": "password123"},
        {"username": "zerocool", "email": "zerocool@mhigh.edu", "password": "password123"},
        {"username": "crashoverride", "email": "crashoverride@mhigh.edu", "password": "password123"},
        {"username": "sleeptoken", "email": "sleeptoken@mhigh.edu", "password": "password123"},
    ],
    "teams": [
        {"name": "Blue Team"},
        {"name": "Gold Team"},
    ],
    "activities": [
        {"username": "thundergod", "activity_type": "Cycling", "duration": "01:00:00"},
        {"username": "metalgeek", "activity_type": "Crossfit", "duration": "02:00:00"},
        {"username": "zerocool", "activity_type": "Running", "duration": "01:30:00"},
        {"username": "crashoverride", "activity_type": "Strength", "duration": "00:30:00"},
        {"username": "sleeptoken", "activity_type": "Swimming", "duration": "01:15:00"},
    ],
    "leaderboard": [
        {"username": "thundergod", "score": 100},
        {"username": "metalgeek", "score": 90},
        {"username": "zerocool", "score": 95},
        {"username": "crashoverride", "score": 85},
        {"username": "sleeptoken", "score": 80},
    ],
    "workouts": [
        {"name": "Cycling Training", "description": "Training for a road cycling event"},
        {"name": "Crossfit", "description": "Training for a crossfit competition"},
        {"name": "Running Training", "description": "Training for a marathon"},
        {"name": "Strength Training", "description": "Training for strength"},
        {"name": "Swimming Training", "description": "Training for a swimming competition"},
    ],
}
