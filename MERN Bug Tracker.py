MERN Bug Tracker
A full-stack MERN application for tracking project bugs with comprehensive testing and debugging implementations.
Project Setup
Prerequisites

Node.js (v18 or higher)
MongoDB
Git

Installation

Clone the repository:

git clone https://github.com/your-username/mern-bug-tracker.git
cd mern-bug-tracker


Install backend dependencies:

cd backend
npm install


Install frontend dependencies:

cd ../frontend
npm install


Create a .env file in the backend folder:

MONGODB_URI=mongodb://localhost:27017/bug-tracker
PORT=5000


Start the development servers:


Backend: cd backend && npm run dev
Frontend: cd frontend && npm start

Running Tests
Backend Tests
cd backend
npm test

Frontend Tests
cd frontend
npm test

Testing Approach

Backend:
Unit tests for helper functions (e.g., validation logic) using Jest.
Integration tests for API routes using Supertest.
Mocked MongoDB interactions with jest-mock.


Frontend:
Unit tests for components using React Testing Library.
Integration tests for API interactions and UI updates.
Snapshot testing for UI consistency.



Test coverage is tracked using Jest's coverage report (npm test -- --coverage).
Debugging Techniques

Backend:
Console logs for tracing request/response flows.
Node.js inspector (node --inspect server.js) for breakpoint debugging.
Express error-handling middleware for centralized error management.


Frontend:
Chrome DevTools for network request inspection and state debugging.
React Error Boundaries to handle component crashes gracefully.
React Developer Tools for component hierarchy analysis.



Project Structure
mern-bug-tracker/
├── backend/
│   ├── __tests__/
│   ├── controllers/
│   ├── models/
│   ├── routes/
│   ├── middleware/
│   └── server.js
├── frontend/
│   ├── src/
│   │   ├── __tests__/
│   │   ├── components/
│   │   ├── pages/
│   │   └── services/
│   └── public/
└── README.md

Features

Create, view, update, and delete bugs.
Form validation for bug submissions.
Status tracking (Open, In-Progress, Resolved).
Error handling for API and UI failures.

