from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

class AnimalShelter:
    """A class that provides CRUD functionality for MongoDB."""
    
    def __init__(self, username, password, host="nv-desktop-services.apporto.com", port=31580, db_name="AAC", collection_name="animals"):
        """Initialize MongoDB connection."""
        try:
            self.client = MongoClient(f"mongodb://{username}:{password}@{host}:{port}/{db_name}")
            self.database = self.client[db_name]
            self.collection = self.database[collection_name]
            print("MongoDB connection established successfully.")
        except ConnectionFailure as e:
            print(f"MongoDB connection failed: {e}")

    def create(self, data):
        """Insert a document into the collection."""
        if isinstance(data, dict) and data:  # Ensure data is not empty
            try:
                result = self.collection.insert_one(data)
                return True if result.acknowledged else False
            except Exception as e:
                print(f"Error inserting data: {e}")
                return False
        print("Warning: Invalid or empty data provided for insertion.")
        return False

    def read(self, query={}):
        """Retrieve documents from the collection based on a query."""
        try:
            documents = list(self.collection.find(query))  # Ensure a list is returned
            return documents if documents else []
        except Exception as e:
            print(f"Error reading data: {e}")
            return []

    def update(self, query, new_values):
        """Update documents that match the query."""
        if not query or not new_values:
            print("Warning: Update query and new values cannot be empty.")
            return 0
        try:
            result = self.collection.update_many(query, {"$set": new_values})
            return result.modified_count
        except Exception as e:
            print(f"Error updating data: {e}")
            return 0

    def delete(self, query):
        """Delete documents that match the query."""
        if not query:
            print("Warning: Delete query cannot be empty.")
            return 0
        try:
            result = self.collection.delete_many(query)
            return result.deleted_count
        except Exception as e:
            print(f"Error deleting data: {e}")
            return 0

