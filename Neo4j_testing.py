from neo4j import GraphDatabase

# Configuration for Neo4j database
NEO4J_URI = "bolt://localhost:7687"
NEO4J_USERNAME = "neo4j"
NEO4J_PASSWORD = "Neoj1234"

# Initialize the Neo4j driver
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USERNAME, NEO4J_PASSWORD))

# Function to save user preferences
def save_user_preference(user_id, preference_category, preference_detail):
    with driver.session() as session:
        session.write_transaction(_add_preference, user_id, preference_category, preference_detail)

# Helper function to add preference to the database
def _add_preference(tx, user_id, preference_category, preference_detail):
    query = """
    MERGE (user:User {id: $user_id})
    MERGE (preference:Preference {category: $preference_category, detail: $preference_detail})
    MERGE (user)-[:HAS_PREFERENCE]->(preference)
    """
    tx.run(query, user_id=user_id, preference_category=preference_category, preference_detail=preference_detail)

# Function to retrieve user preferences
def fetch_user_preferences(user_id):
    with driver.session() as session:
        return session.read_transaction(_retrieve_preferences, user_id)

# Helper function to retrieve preferences from the database
def _retrieve_preferences(tx, user_id):
    query = """
    MATCH (user:User {id: $user_id})-[:HAS_PREFERENCE]->(preference:Preference)
    RETURN preference.category AS category, preference.detail AS detail
    """
    result = tx.run(query, user_id=user_id)
    return [{"category": record["category"], "detail": record["detail"]} for record in result]

# Example usage
if __name__ == "__main__":
    # Example user ID
    user_id = "user123"

    # Preferences to save
    user_preferences_list = [
        {"category": "Activity", "detail": "Historical Sites"},
        {"category": "Food", "detail": "Italian Cuisine"},
        {"category": "Budget", "detail": "Moderate"}
    ]

    for preference in user_preferences_list:
        save_user_preference(user_id, preference["category"], preference["detail"])

    print("User preferences have been successfully saved!")

    # Fetch and display preferences for further use
    retrieved_preferences = fetch_user_preferences(user_id)
    print("Retrieved user preferences for the next interaction:")
    for preference in retrieved_preferences:
        print(f"{preference['category']}: {preference['detail']}")

# Close the Neo4j driver when done
driver.close()
