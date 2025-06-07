// insert_books.js (example)
const { MongoClient } = require('mongodb');

async function main() {
    const uri = "mongodb://localhost:27017"; // or your Atlas connection string
    const client = new MongoClient(uri);

    try {
        await client.connect();
        const database = client.db('library');
        const books = database.collection('books');

        const bookData = [
            { title: "Book 1", author: "Author A", year: 2020, genre: "Fiction", price: 29.99 },
            { title: "Book 2", author: "Author B", year: 2018, genre: "Non-Fiction", price: 19.99 },
            // More books...
        ];

        await books.insertMany(bookData);
        console.log("Books inserted successfully!");
    } finally {
        await client.close();
    }
}

main().catch(console.error);
// queries.js
const { MongoClient } = require('mongodb');

async function runQueries() {
    const uri = "mongodb://localhost:27017"; // or your Atlas connection string
    const client = new MongoClient(uri);

    try {
        await client.connect();
        const database = client.db('library');
        const books = database.collection('books');

        // **CRUD Operations**
        // Create: Insert a new book
        await books.insertOne({
            title: "New Book",
            author: "Author C",
            year: 2023,
            genre: "Science Fiction",
            price: 24.99
        });
        console.log("Inserted new book");

        // Read: Find books published after 2019
        const recentBooks = await books.find({ year: { $gt: 2019 } }).toArray();
        console.log("Books after 2019:", recentBooks);

        // Update: Increase price by 10% for Fiction books
        await books.updateMany(
            { genre: "Fiction" },
            { $mul: { price: 1.1 } }
        );
        console.log("Updated prices for Fiction books");

        // Delete: Remove books older than 2015
        await books.deleteMany({ year: { $lt: 2015 } });
        console.log("Deleted books older than 2015");

        // **Advanced Queries**
        // Find Fiction books priced between $15 and $30, sorted by price
        const filteredBooks = await books.find({
            genre: "Fiction",
            price: { $gte: 15, $lte: 30 }
        })
            .project({ title: 1, price: 1, _id: 0 })
            .sort({ price: 1 })
            .toArray();
        console.log("Filtered Fiction books:", filteredBooks);

        // **Aggregation Pipeline**
        // Group books by genre, calculate average price and count
        const genreStats = await books.aggregate([
            {
                $group: {
                    _id: "$genre",
                    averagePrice: { $avg: "$price" },
                    totalBooks: { $sum: 1 }
                }
            },
            { $sort: { averagePrice: -1 } }
        ]).toArray();
        console.log("Genre statistics:", genreStats);

        // **Indexing**
        // Create an index on the 'year' field for faster queries
        await books.createIndex({ year: 1 });
        console.log("Created index on year");

    } finally {
        await client.close();
    }
}

runQueries().catch(console.error);
