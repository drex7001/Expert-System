# Sri Lanka Tourism Recommendation Engine

# Database of tourist attractions
attractions = [
    {
        "name": "Sigiriya",
        "type": ["Historical", "UNESCO World Heritage"],
        "region": "Central Province",
        "ideal_season": ["Jan", "Feb", "Mar", "Apr", "Aug", "Sep"],
        "budget_category": "Medium",
        "activities": ["Hiking", "Sightseeing", "Photography"],
        "duration": 1,  # in days
        "crowd_level": "High"
    },
    {
        "name": "Yala National Park",
        "type": ["Wildlife", "Nature"],
        "region": "Southern Province",
        "ideal_season": ["Feb", "Mar", "Apr", "May", "Jun", "Jul"],
        "budget_category": "Medium",
        "activities": ["Safari", "Birdwatching", "Photography"],
        "duration": 2,
        "crowd_level": "Medium"
    },
    # Add more attractions here
]

# Database of accommodations
accommodations = [
    {
        "name": "Heritance Kandalama",
        "type": "Hotel",
        "location": "Dambulla",
        "price_category": "Luxury",
        "amenities": ["Pool", "Spa", "Restaurant"],
        "nearby_attractions": ["Sigiriya", "Dambulla Cave Temple"]
    },
    {
        "name": "Cinnamon Wild Yala",
        "type": "Resort",
        "location": "Yala",
        "price_category": "Upper Midrange",
        "amenities": ["Pool", "Restaurant", "Safari Tours"],
        "nearby_attractions": ["Yala National Park"]
    },
    # Add more accommodations here
]

# User preferences
user_preferences = {
    "interests": [],
    "budget": "",
    "travel_season": "",
    "trip_duration": 0,
    "preferred_activities": [],
    "accommodation_type": "",
}

# Recommendation functions
def recommend_attractions(preferences, attractions_db):
    recommended = []
    for attraction in attractions_db:
        score = 0
        
        # Match interests
        if any(interest in attraction["type"] for interest in preferences["interests"]):
            score += 2
        
        # Match budget
        if attraction["budget_category"].lower() == preferences["budget"].lower():
            score += 1
        
        # Match season
        if preferences["travel_season"] in attraction["ideal_season"]:
            score += 1
        
        # Match activities
        if any(activity in preferences["preferred_activities"] for activity in attraction["activities"]):
            score += 1
        
        if score > 2:  # Adjust this threshold as needed
            recommended.append((attraction["name"], score))
    
    return sorted(recommended, key=lambda x: x[1], reverse=True)

def recommend_accommodations(preferences, accommodations_db, recommended_attractions):
    recommended = []
    for accommodation in accommodations_db:
        score = 0
        
        # Match budget
        if accommodation["price_category"].lower() == preferences["budget"].lower():
            score += 2
        
        # Match type
        if accommodation["type"].lower() == preferences["accommodation_type"].lower():
            score += 1
        
        # Proximity to recommended attractions
        if any(attraction in recommended_attractions for attraction in accommodation["nearby_attractions"]):
            score += 2
        
        if score > 2:  # Adjust this threshold as needed
            recommended.append((accommodation["name"], score))
    
    return sorted(recommended, key=lambda x: x[1], reverse=True)

def generate_itinerary(recommended_attractions, recommended_accommodations, preferences):
    itinerary = []
    current_day = 1
    remaining_duration = preferences["trip_duration"]

    while remaining_duration > 0 and recommended_attractions:
        attraction, _ = recommended_attractions.pop(0)
        for attr in attractions:
            if attr["name"] == attraction:
                itinerary.append({
                    "day": current_day,
                    "attraction": attraction,
                    "activities": attr["activities"],
                    "duration": attr["duration"]
                })
                current_day += attr["duration"]
                remaining_duration -= attr["duration"]
                break

    # Add accommodation recommendations
    if recommended_accommodations:
        itinerary.append({
            "accommodation_options": [name for name, _ in recommended_accommodations[:3]]
        })

    return itinerary

# Function to update user preferences
def update_preferences(preferences, key, value):
    preferences[key] = value

# Main recommendation function
def get_recommendations(preferences, attractions_db, accommodations_db):
    recommended_attractions = recommend_attractions(preferences, attractions_db)
    recommended_accommodations = recommend_accommodations(preferences, accommodations_db, [a[0] for a in recommended_attractions])
    itinerary = generate_itinerary(recommended_attractions, recommended_accommodations, preferences)
    return itinerary

# Example usage
update_preferences(user_preferences, "interests", ["Historical", "Nature"])
update_preferences(user_preferences, "budget", "Medium")
update_preferences(user_preferences, "travel_season", "Feb")
update_preferences(user_preferences, "trip_duration", 5)
update_preferences(user_preferences, "preferred_activities", ["Hiking", "Sightseeing", "Safari"])
update_preferences(user_preferences, "accommodation_type", "Hotel")

recommendations = get_recommendations(user_preferences, attractions, accommodations)
print("Recommended itinerary:", recommendations)