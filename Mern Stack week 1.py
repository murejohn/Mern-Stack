from pymongo import MongoClient, ASCENDING
from pprint import pprint
from datetime import datetime

# Part 1: Set up MongoDB Database
def setup_database():
    """Connect to MongoDB and set up the database and collection."""
    client = MongoClient('mongodb://localhost:27017/')  # Adjust URI if using Atlas
    db = client['library_db']  # Create/use database
    collection = db['books']   # Create/use collection
    return db, collection

# Part 2: CRUD Operations
def perform_crud_operations(collection):
    """Demonstrate Create, Read, Update, Delete operations."""
    print("\n=== CRUD Operations ===")
    
    # Create: Insert multiple book documents
    books = [
        {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "genre": "Fiction", "price": 9.99},
        {"title": "1984", "author": "George Orwell", "year": 1949, "genre": "Dystopian", "price": 12.50},
        {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "genre": "Fiction", "price": 10.75},
        {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932, "genre": "Dystopian", "price": 11.25}
    ]
    result = collection.insert_many(books)
    print(f"Inserted {len(result.inserted_ids)} books.")

    # Read: Find one book by title
    book = collection.find_one({"title": "1984"})
    print("\nRead (Find one):")
    pprint(book)

    # Update: Increase price of all Fiction books by 10%
    collection.update_many({"genre": "Fiction"}, {"$mul": {"price": 1.10}})
    print("\nUpdated prices for Fiction books by +10%.")

    # Read: Verify update
    print("\nRead (After Update):")
    for book in collection.find({"genre": "Fiction"}):
        pprint(book)

    # Delete: Remove books older than 1950
    result = collection.delete_many({"year": {"$lt": 1950}})
    print(f"\nDeleted {result.deleted_count} books older than 1950.")

# Part 3: Advanced Queries
def advanced_queries(collection):
    """Perform queries with filtering, projection, and sorting."""
    print("\n=== Advanced Queries ===")
    
    # Query 1: Find books with price > 10, project only title and price, sort by price descending
    print("\nBooks with price > $10 (sorted by price descending):")
    query = {"price": {"$gt": 10}}
    projection = {"title": 1, "price": 1, "_id": 0}
    for book in collection.find(query, projection).sort("price", -1):
        pprint(book)

    # Query 2: Find books published after 1950 in Fiction genre
    print("\nFiction books published after 1950:")
    query = {"$and": [{"year": {"$gt": 1950}}, {"genre": "Fiction"}]}
    for book in collection.find(query):
        pprint(book)

# Part 4: Aggregation Pipelines
def aggregation_pipelines(collection):
    """Create aggregation pipelines for data analysis."""
    print("\n=== Aggregation Pipelines ===")
    
    # Pipeline 1: Group by genre, calculate average price and count
    pipeline = [
        {"$group": {
            "_id": "$genre",
            "avg_price": {"$avg": "$price"},
            "book_count": {"$sum": 1}
        }},
        {"$sort": {"avg_price": -1}}
    ]
    print("\nAverage price and count per genre:")
    for result in collection.aggregate(pipeline):
        pprint(result)

    # Pipeline 2: Filter books > $10, group by author, list titles
    pipeline = [
        {"$match": {"price": {"$gt": 10}}},
        {"$group": {
            "_id": "$author",
            "titles": {"$push": "$title"},
            "total_price": {"$sum": "$price"}
        }}
    ]
    print("\nAuthors with books > $10, their titles, and total price:")
    for result in collection.aggregate(pipeline):
        pprint(result)

# Part 5: Indexing for Performance
def create_indexes(collection):
    """Create indexes to optimize query performance."""
    print("\n=== Indexing ===")
    
    # Create index on 'year' for queries filtering by year
    collection.create_index([("year", ASCENDING)])
    print("Created index on 'year' field.")
    
    # Create compound index on 'genre' and 'price' for advanced queries
    collection.create_index([("genre", ASCENDING), ("price", ASCENDING)])
    print("Created compound index on 'genre' and 'price'.")
    
    # Display indexes
    print("\nIndexes in collection:")
    pprint(collection.index_information())

# Main Execution
if __name__ == "__main__":
    # Set up database
    db, collection = setup_database()
    
    # Clear collection to ensure clean state
    collection.drop()
    
    # Perform all operations
    perform_crud_operations(collection)
    advanced_queries(collection)
    aggregation_pipelines(collection)
    create_indexes(collection)
    
    # Clean up (optional)
    # db.drop_database()