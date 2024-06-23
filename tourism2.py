import chromadb
from chromadb.utils import embedding_functions
from datetime import datetime, timedelta

# Initialize ChromaDB client
client = chromadb.Client()

# Create a collection for tourist places
collection = client.create_collection(name="sri_lanka_tourist_places")

# Initialize the embedding function (using default SentenceTransformer)
embedding_func = embedding_functions.SentenceTransformerEmbeddingFunction()

# Function to add places to the database
def add_place(name, description, type, budget_range, tips, duration):
    collection.add(
        documents=[description],
        metadatas=[{"name": name, "type": type, "budget_range": budget_range, "tips": tips, "duration": duration}],
        ids=[name]
    )

# Add more diverse example places with duration (in hours)
add_place("Sigiriya", "Ancient rock fortress with frescoes and water gardens, known for its stunning views and historical significance.", "cultural", "low", "Visit early morning to avoid crowds and bring plenty of water for the climb.", 12)
add_place("Yala National Park", "Renowned wildlife sanctuary, home to leopards, elephants, and a variety of bird species.", "natural", "medium", "Best visited between February and July for optimal wildlife viewing. Hire a knowledgeable guide for the safari.", 12)
add_place("Temple of the Tooth", "Sacred Buddhist temple in Kandy, housing a relic of the tooth of Buddha.", "cultural", "high", "Visit during the Esala Perahera festival for a unique cultural experience. Dress modestly and be prepared for security checks.", 12)
add_place("Galle Fort", "Historic fort and UNESCO World Heritage site, featuring colonial architecture and a picturesque coastline.", "cultural", "medium", "Explore the fort in the late afternoon to avoid the heat. Wear comfortable walking shoes.", 12)
add_place("Horton Plains National Park", "Scenic plateau with stunning landscapes, including the famous World's End cliff and Baker's Falls.", "natural", "low", "Start early in the morning to catch the best views before the mist sets in. Bring warm clothing as it can get chilly.", 12)
add_place("Dambulla Cave Temple", "Complex of cave temples with ancient Buddhist murals and statues, a UNESCO World Heritage site.", "cultural", "medium", "Visit early in the day to avoid crowds. Be prepared to climb stairs and remove shoes before entering the temples.", 12)
add_place("Ella", "Charming town surrounded by tea plantations, known for its hiking trails and stunning viewpoints.", "natural", "low", "Hike to Ella Rock or Little Adam's Peak for breathtaking views. Try the local cuisine in one of the many cafes.", 12)
add_place("Mirissa", "Popular beach destination with opportunities for whale watching and surfing.", "natural", "medium", "Best time for whale watching is from November to April. Stay hydrated and use sunscreen to protect yourself from the sun.", 12)
add_place("Anuradhapura", "Ancient city with well-preserved ruins, including stupas, temples, and pools, a UNESCO World Heritage site.", "cultural", "low", "Rent a bicycle to explore the vast area. Visit the Sri Maha Bodhi tree, one of the oldest trees in the world.", 12)
add_place("Nuwara Eliya", "Hill station known for its cool climate, tea plantations, and colonial-era bungalows.", "natural", "medium", "Visit a tea factory to learn about tea production. Pack layers as the weather can change quickly.", 12)
add_place("Polonnaruwa", "Ancient city with well-preserved ruins, including temples, tombs, and statues, a UNESCO World Heritage site.", "cultural", "low", "Explore early in the morning to avoid the heat and crowds. Rent a bicycle to cover more ground efficiently.", 12)
add_place("Udawalawe National Park", "Wildlife reserve famous for its large elephant population and bird watching.", "natural", "medium", "Visit during the dry season from May to September for better wildlife sightings. Hire a local guide for the best experience.", 12)
add_place("Sinharaja Forest Reserve", "Biodiverse rainforest and UNESCO World Heritage site, known for its unique flora and fauna.", "natural", "low", "Wear long sleeves and insect repellent to protect against leeches. Hire a guide to navigate the dense forest.", 12)
add_place("Adam's Peak", "Sacred mountain and pilgrimage site, known for the 'Sri Pada' footprint at its summit.", "cultural", "high", "Begin the hike at night to reach the summit for sunrise. Wear sturdy shoes and bring warm clothing for the ascent.", 12)
add_place("Pinnawala Elephant Orphanage", "Sanctuary for orphaned elephants, offering close encounters and feeding opportunities.", "natural", "high", "Visit during feeding and bathing times for the best experience. Follow guidelines to ensure the well-being of the elephants.", 12)
add_place("Trincomalee", "Coastal city with beautiful beaches, historical sites, and marine activities.", "natural", "medium", "Explore Nilaveli and Uppuveli beaches for snorkeling and diving. Visit Koneswaram Temple for panoramic views.", 12)
add_place("Bentota", "Resort town known for its pristine beaches, water sports, and luxury accommodations.", "natural", "medium", "Engage in water sports like jet skiing and windsurfing. Visit the nearby Brief Garden for a tranquil retreat.", 12)
add_place("Arugam Bay", "Famous surfing destination with a laid-back atmosphere and beautiful beaches.", "natural", "medium", "Best surf season is from April to October. Relax at local cafes and enjoy the vibrant surf culture.", 12)
add_place("Jaffna", "Cultural hub in the northern part of Sri Lanka, known for its Tamil heritage, temples, and cuisine.", "cultural", "low", "Visit the Nallur Kandaswamy Temple and sample local Jaffna cuisine. Respect local customs and traditions.", 12)
add_place("Hikkaduwa", "Popular beach town with vibrant nightlife, coral reefs, and surf spots.", "natural", "medium", "Snorkel at the coral sanctuary and enjoy the nightlife. Use reef-safe sunscreen to protect marine life.", 12)


# Function to get user input
def get_user_input():
    days = int(input("How many days would you like to travel in Sri Lanka? "))
    budget = input("What is your budget range (low/medium/high)? ").lower()
    preferences = input("Describe what you're looking for in your trip: ")
    return days, budget, preferences

# Function to recommend places
# Function to recommend places
# Function to recommend places
def recommend_places(days, budget, preferences):
    embedded_preferences = embedding_func([preferences])[0]
    
    results = collection.query(
        query_embeddings=[embedded_preferences],
        n_results=days * 3,  # Get more results than needed
        where={"$or": [{"budget_range": budget}, {"budget_range": "medium"}]}
    )
    
    if not results['metadatas']:
        return []
    
    recommendations = []
    for metadata, distance in zip(results['metadatas'][0], results['distances'][0]):
        similarity_score = 1 - distance
        print(f"Place: {metadata['name']}, Similarity Score: {similarity_score}")  # Debug print
        recommendations.append({
            "name": metadata['name'],
            "type": metadata['type'],
            "budget": metadata['budget_range'],
            "tips": metadata['tips'],
            "duration": metadata['duration'],
            "similarity": similarity_score
        })
    
    # Filter recommendations to be more relevant
    min_similarity_threshold = 0.5  # Adjust this threshold as needed
    recommendations = [r for r in recommendations if r['similarity'] >= min_similarity_threshold]

    recommendations.sort(key=lambda x: x['similarity'], reverse=True)
    recommendations = [r for r in recommendations if r['budget'] == budget or (budget == 'medium' and r['budget'] == 'low')]
    
    return recommendations

# Function to generate itinerary
def generate_itinerary(days, budget, preferences):
    recommendations = recommend_places(days, budget, preferences)
    if not recommendations:
        return "We couldn't find suitable recommendations for your preferences."
    
    itinerary = []
    current_day = 1
    total_duration = 0
    start_date = datetime.now().date()

    for place in recommendations:
        if total_duration + int(place['duration']) <= days * 10:  # Assuming 10 hours per day for activities
            itinerary.append({
                "day": current_day,
                "date": start_date + timedelta(days=current_day - 1),
                "place": place['name'],
                "duration": place['duration'],
                "tips": place['tips']
            })
            total_duration += int(place['duration'])
            if total_duration >= 10:
                current_day += 1
                total_duration = 0
        else:
            break

    return format_itinerary(itinerary)

# Helper function to format the itinerary
def format_itinerary(itinerary):
    formatted = "Your Itinerary:\n\n"
    for item in itinerary:
        formatted += f"Day {item['day']} - {item['date'].strftime('%A, %B %d, %Y')}:\n"
        formatted += f"  Visit: {item['place']} (Duration: {item['duration']} hours)\n"
        formatted += f"  Tips: {item['tips']}\n\n"
    return formatted

# Main function
def main():
    print("Welcome to the Sri Lanka Tourism Expert System!")
    days, budget, preferences = get_user_input()
    itinerary = generate_itinerary(days, budget, preferences)
    print("\nBased on your preferences, here's your recommended itinerary:")
    print(itinerary)

if __name__ == "__main__":
    main()


















































# import random
# import chromadb
# from chromadb.config import Settings
# from chromadb.utils import embedding_functions

# class SustainableTourismPlanner:
#     def __init__(self):
#         self.chroma_client = chromadb.Client(Settings(persist_directory="./chromadb_data"))
#         self.embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(model_name="all-MiniLM-L6-v2")
        
#         self.attractions = {
#             "Sigiriya": {
#                 "type": "cultural", 
#                 "impact": 3, 
#                 "popularity": 9,
#                 "description": "Ancient rock fortress with frescoes and water gardens"
#             },
#             "Yala National Park": {
#                 "type": "nature", 
#                 "impact": 2, 
#                 "popularity": 8,
#                 "description": "Wildlife sanctuary famous for leopards and elephants"
#             },
#             "Galle Fort": {
#                 "type": "cultural", 
#                 "impact": 1, 
#                 "popularity": 7,
#                 "description": "Historic fortified city with colonial architecture"
#             },
#             "Ella": {
#                 "type": "nature", 
#                 "impact": 1, 
#                 "popularity": 6,
#                 "description": "Picturesque hill country with tea plantations and hiking trails"
#             },
#             "Kandy": {
#                 "type": "cultural", 
#                 "impact": 2, 
#                 "popularity": 8,
#                 "description": "Sacred Buddhist site with the Temple of the Tooth Relic"
#             },
#             "Mirissa Beach": {
#                 "type": "nature", 
#                 "impact": 2, 
#                 "popularity": 7,
#                 "description": "Beautiful beach known for whale watching and surfing"
#             },
#             "Polonnaruwa": {
#                 "type": "cultural", 
#                 "impact": 1, 
#                 "popularity": 5,
#                 "description": "Ancient city with well-preserved ruins and Buddha statues"
#             },
#             "Horton Plains": {
#                 "type": "nature", 
#                 "impact": 2, 
#                 "popularity": 6,
#                 "description": "National park with diverse flora, fauna, and World's End viewpoint"
#             },
#             "Anuradhapura": {
#                 "type": "cultural", 
#                 "impact": 1, 
#                 "popularity": 6,
#                 "description": "Sacred city with ancient Buddhist monasteries and stupas"
#             },
#             "Udawalawe National Park": {
#                 "type": "nature", 
#                 "impact": 2, 
#                 "popularity": 7,
#                 "description": "Wildlife reserve known for its large elephant population"
#             }
#         }
        
#         self.accommodations = {
#             "Eco Lodge": {"impact": 1, "comfort": 3},
#             "Homestay": {"impact": 1, "comfort": 2},
#             "Boutique Hotel": {"impact": 2, "comfort": 4},
#             "Sustainable Resort": {"impact": 2, "comfort": 5}
#         }

#         self.setup_chromadb()

#     def setup_chromadb(self):
#         # Create or get the collection
#         self.collection = self.chroma_client.get_or_create_collection(
#             name="sri_lanka_attractions",
#             embedding_function=self.embedding_function
#         )

#         # Add documents if the collection is empty
#         if self.collection.count() == 0:
#             self.collection.add(
#                 documents=[details['description'] for details in self.attractions.values()],
#                 metadatas=[{"name": name, **{k: str(v) for k, v in details.items() if k != 'description'}} 
#                            for name, details in self.attractions.items()],
#                 ids=[name for name in self.attractions.keys()]
#             )

#     def get_user_preferences(self):
#         print("Welcome to the Sustainable Tourism Planner for Sri Lanka!")
#         duration = int(input("How many days is your trip? "))
#         interests = input("What are you looking for in your trip? Describe your ideal experiences: ")
#         budget = input("What's your budget level? (low/medium/high): ").lower()
#         return duration, interests, budget

#     def find_similar_attractions(self, description, n=3):
#         results = self.collection.query(
#             query_texts=[description],
#             n_results=n
#         )
#         return list(zip(results['ids'][0], results['distances'][0]))

#     def generate_itinerary(self, duration, interests, budget):
#         itinerary = []
#         similar_attractions = self.find_similar_attractions(interests, n=duration)
        
#         for day in range(1, duration + 1):
#             attraction, _ = similar_attractions[day - 1]
            
#             if budget == "low":
#                 accommodation = random.choice(["Eco Lodge", "Homestay"])
#             elif budget == "medium":
#                 accommodation = random.choice(["Eco Lodge", "Homestay", "Boutique Hotel"])
#             else:
#                 accommodation = random.choice(list(self.accommodations.keys()))

#             itinerary.append({
#                 "day": day,
#                 "attraction": attraction,
#                 "accommodation": accommodation
#             })

#         return itinerary

#     def display_itinerary(self, itinerary):
#         print("\nYour Sustainable Sri Lanka Itinerary:")
#         for day in itinerary:
#             print(f"\nDay {day['day']}:")
#             print(f"  Visit: {day['attraction']}")
#             print(f"  Description: {self.attractions[day['attraction']]['description']}")
#             print(f"  Stay at: {day['accommodation']}")
#             print(f"  Eco-tip: {self.get_eco_tip(day['attraction'], day['accommodation'])}")

#     def get_eco_tip(self, attraction, accommodation):
#         tips = [
#             f"When visiting {attraction}, stick to marked trails to protect the local ecosystem.",
#             f"Bring a reusable water bottle to reduce plastic waste during your trip.",
#             f"Support local artisans by purchasing authentic, locally-made souvenirs.",
#             f"At {accommodation}, use towels and linens for multiple days to conserve water.",
#             "Use public transportation or bike rentals when possible to reduce your carbon footprint.",
#             "Respect wildlife by maintaining a safe distance and not feeding animals.",
#             "Learn a few local phrases to connect better with the Sri Lankan community.",
#             "Choose reef-safe sunscreen to protect marine ecosystems when visiting beaches.",
#             "Participate in a local beach or trail clean-up activity if available.",
#             "Opt for locally-sourced, plant-based meals to reduce your environmental impact."
#         ]
#         return random.choice(tips)

#     def run(self):
#         duration, interests, budget = self.get_user_preferences()
#         itinerary = self.generate_itinerary(duration, interests, budget)
#         self.display_itinerary(itinerary)

# if __name__ == "__main__":
#     planner = SustainableTourismPlanner()
#     planner.run()

# # import random

# # class SustainableTourismPlanner:
# #     def __init__(self):
# #         self.attractions = {
# #             "Sigiriya": {"type": "cultural", "impact": 3, "popularity": 9},
# #             "Yala National Park": {"type": "nature", "impact": 2, "popularity": 8},
# #             "Galle Fort": {"type": "cultural", "impact": 1, "popularity": 7},
# #             "Ella": {"type": "nature", "impact": 1, "popularity": 6},
# #             "Kandy": {"type": "cultural", "impact": 2, "popularity": 8},
# #             "Mirissa Beach": {"type": "nature", "impact": 2, "popularity": 7},
# #             "Polonnaruwa": {"type": "cultural", "impact": 1, "popularity": 5},
# #             "Horton Plains": {"type": "nature", "impact": 2, "popularity": 6},
# #             "Anuradhapura": {"type": "cultural", "impact": 1, "popularity": 6},
# #             "Udawalawe National Park": {"type": "nature", "impact": 2, "popularity": 7}
# #         }
        
# #         self.accommodations = {
# #             "Eco Lodge": {"impact": 1, "comfort": 3},
# #             "Homestay": {"impact": 1, "comfort": 2},
# #             "Boutique Hotel": {"impact": 2, "comfort": 4},
# #             "Sustainable Resort": {"impact": 2, "comfort": 5}
# #         }

# #     def get_user_preferences(self):
# #         print("Welcome to the Sustainable Tourism Planner for Sri Lanka!")
# #         duration = int(input("How many days is your trip? "))
# #         interests = input("What are your main interests? (nature/culture/both): ").lower()
# #         budget = input("What's your budget level? (low/medium/high): ").lower()
# #         return duration, interests, budget

# #     def generate_itinerary(self, duration, interests, budget):
# #         itinerary = []
# #         visited = set()

# #         for day in range(1, duration + 1):
# #             # Select attraction
# #             available_attractions = [a for a in self.attractions.items() 
# #                                      if a[0] not in visited and 
# #                                      (interests == "both" or a[1]["type"] == interests)]
            
# #             if not available_attractions:
# #                 available_attractions = [a for a in self.attractions.items() if a[0] not in visited]
            
# #             attraction, details = random.choice(available_attractions)
# #             visited.add(attraction)

# #             # Select accommodation
# #             if budget == "low":
# #                 accommodation = random.choice(["Eco Lodge", "Homestay"])
# #             elif budget == "medium":
# #                 accommodation = random.choice(["Eco Lodge", "Homestay", "Boutique Hotel"])
# #             else:
# #                 accommodation = random.choice(list(self.accommodations.keys()))

# #             itinerary.append({
# #                 "day": day,
# #                 "attraction": attraction,
# #                 "accommodation": accommodation
# #             })

# #         return itinerary

# #     def display_itinerary(self, itinerary):
# #         print("\nYour Sustainable Sri Lanka Itinerary:")
# #         for day in itinerary:
# #             print(f"\nDay {day['day']}:")
# #             print(f"  Visit: {day['attraction']}")
# #             print(f"  Stay at: {day['accommodation']}")
# #             print(f"  Eco-tip: {self.get_eco_tip(day['attraction'], day['accommodation'])}")

# #     def get_eco_tip(self, attraction, accommodation):
# #         tips = [
# #             f"When visiting {attraction}, stick to marked trails to protect the local ecosystem.",
# #             f"Bring a reusable water bottle to reduce plastic waste during your trip.",
# #             f"Support local artisans by purchasing authentic, locally-made souvenirs.",
# #             f"At {accommodation}, use towels and linens for multiple days to conserve water.",
# #             "Use public transportation or bike rentals when possible to reduce your carbon footprint.",
# #             "Respect wildlife by maintaining a safe distance and not feeding animals.",
# #             "Learn a few local phrases to connect better with the Sri Lankan community.",
# #             "Choose reef-safe sunscreen to protect marine ecosystems when visiting beaches.",
# #             "Participate in a local beach or trail clean-up activity if available.",
# #             "Opt for locally-sourced, plant-based meals to reduce your environmental impact."
# #         ]
# #         return random.choice(tips)

# #     def run(self):
# #         duration, interests, budget = self.get_user_preferences()
# #         itinerary = self.generate_itinerary(duration, interests, budget)
# #         self.display_itinerary(itinerary)

# # if __name__ == "__main__":
# #     planner = SustainableTourismPlanner()
# #     planner.run()



# import random
# import numpy as np
# from scipy.spatial.distance import cosine
# from sentence_transformers import SentenceTransformer

# class SustainableTourismPlanner:
#     def __init__(self):
#         self.model = SentenceTransformer('all-MiniLM-L6-v2')
#         self.attractions = {
#             "Sigiriya": {
#                 "type": "cultural", 
#                 "impact": 3, 
#                 "popularity": 9,
#                 "description": "Ancient rock fortress with frescoes and water gardens"
#             },
#             "Yala National Park": {
#                 "type": "nature", 
#                 "impact": 2, 
#                 "popularity": 8,
#                 "description": "Wildlife sanctuary famous for leopards and elephants"
#             },
#             "Galle Fort": {
#                 "type": "cultural", 
#                 "impact": 1, 
#                 "popularity": 7,
#                 "description": "Historic fortified city with colonial architecture"
#             },
#             "Ella": {
#                 "type": "nature", 
#                 "impact": 1, 
#                 "popularity": 6,
#                 "description": "Picturesque hill country with tea plantations and hiking trails"
#             },
#             "Kandy": {
#                 "type": "cultural", 
#                 "impact": 2, 
#                 "popularity": 8,
#                 "description": "Sacred Buddhist site with the Temple of the Tooth Relic"
#             },
#             "Mirissa Beach": {
#                 "type": "nature", 
#                 "impact": 2, 
#                 "popularity": 7,
#                 "description": "Beautiful beach known for whale watching and surfing"
#             },
#             "Polonnaruwa": {
#                 "type": "cultural", 
#                 "impact": 1, 
#                 "popularity": 5,
#                 "description": "Ancient city with well-preserved ruins and Buddha statues"
#             },
#             "Horton Plains": {
#                 "type": "nature", 
#                 "impact": 2, 
#                 "popularity": 6,
#                 "description": "National park with diverse flora, fauna, and World's End viewpoint"
#             },
#             "Anuradhapura": {
#                 "type": "cultural", 
#                 "impact": 1, 
#                 "popularity": 6,
#                 "description": "Sacred city with ancient Buddhist monasteries and stupas"
#             },
#             "Udawalawe National Park": {
#                 "type": "nature", 
#                 "impact": 2, 
#                 "popularity": 7,
#                 "description": "Wildlife reserve known for its large elephant population"
#             }
#         }
        
#         self.accommodations = {
#             "Eco Lodge": {"impact": 1, "comfort": 3},
#             "Homestay": {"impact": 1, "comfort": 2},
#             "Boutique Hotel": {"impact": 2, "comfort": 4},
#             "Sustainable Resort": {"impact": 2, "comfort": 5}
#         }

#         self.attraction_embeddings = {
#             name: self.model.encode(details['description']) 
#             for name, details in self.attractions.items()
#         }

#     def get_user_preferences(self):
#         print("Welcome to the Sustainable Tourism Planner for Sri Lanka!")
#         duration = int(input("How many days is your trip? "))
#         interests = input("What are you looking for in your trip? Describe your ideal experiences: ")
#         budget = input("What's your budget level? (low/medium/high): ").lower()
#         return duration, interests, budget

#     def find_similar_attractions(self, description, n=3):
#         description_embedding = self.model.encode(description)
#         similarities = {
#             name: 1 - cosine(embedding, description_embedding)
#             for name, embedding in self.attraction_embeddings.items()
#         }
#         return sorted(similarities.items(), key=lambda x: x[1], reverse=True)[:n]

#     def generate_itinerary(self, duration, interests, budget):
#         itinerary = []
#         similar_attractions = self.find_similar_attractions(interests, n=duration)
        
#         for day in range(1, duration + 1):
#             attraction, _ = similar_attractions[day - 1]
            
#             if budget == "low":
#                 accommodation = random.choice(["Eco Lodge", "Homestay"])
#             elif budget == "medium":
#                 accommodation = random.choice(["Eco Lodge", "Homestay", "Boutique Hotel"])
#             else:
#                 accommodation = random.choice(list(self.accommodations.keys()))

#             itinerary.append({
#                 "day": day,
#                 "attraction": attraction,
#                 "accommodation": accommodation
#             })

#         return itinerary

#     def display_itinerary(self, itinerary):
#         print("\nYour Sustainable Sri Lanka Itinerary:")
#         for day in itinerary:
#             print(f"\nDay {day['day']}:")
#             print(f"  Visit: {day['attraction']}")
#             print(f"  Description: {self.attractions[day['attraction']]['description']}")
#             print(f"  Stay at: {day['accommodation']}")
#             print(f"  Eco-tip: {self.get_eco_tip(day['attraction'], day['accommodation'])}")

#     def get_eco_tip(self, attraction, accommodation):
#         tips = [
#             f"When visiting {attraction}, stick to marked trails to protect the local ecosystem.",
#             f"Bring a reusable water bottle to reduce plastic waste during your trip.",
#             f"Support local artisans by purchasing authentic, locally-made souvenirs.",
#             f"At {accommodation}, use towels and linens for multiple days to conserve water.",
#             "Use public transportation or bike rentals when possible to reduce your carbon footprint.",
#             "Respect wildlife by maintaining a safe distance and not feeding animals.",
#             "Learn a few local phrases to connect better with the Sri Lankan community.",
#             "Choose reef-safe sunscreen to protect marine ecosystems when visiting beaches.",
#             "Participate in a local beach or trail clean-up activity if available.",
#             "Opt for locally-sourced, plant-based meals to reduce your environmental impact."
#         ]
#         return random.choice(tips)

#     def run(self):
#         duration, interests, budget = self.get_user_preferences()
#         itinerary = self.generate_itinerary(duration, interests, budget)
#         self.display_itinerary(itinerary)

# if __name__ == "__main__":
#     planner = SustainableTourismPlanner()
#     planner.run()


