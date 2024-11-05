Book Hub
Book Hub is a library management system designed to streamline the process of managing books, users, and library-related operations. This system provides an easy-to-use interface for librarians and patrons, enabling efficient book management and user administration.

Features
User Management: Add, update, delete, and search for users. Roles include Librarians and Patrons.
Book Management: Add new books, update book details, delete entries, and search for books by various criteria.
Borrowing and Returning: Track the status of books being borrowed and returned.
Search and Filter: Easily search for books and users with advanced filtering options.
Notifications: Optional notifications for due dates or book availability.
Technologies Used
Backend: Django REST framework for API endpoints.
Frontend: React with Bootstrap for responsive design.
Database: MySQL or PostgreSQL for robust data management.
Others: React Toastify for notifications.
Requirements
Python and Django for backend development.
React for frontend development.
Database: MySQL or PostgreSQL setup.
Installation
Clone the repository:


git clone https://github.com/Rinsan-K/Book_Hub.git
Set up the backend:

Install dependencies:

pip install -r requirements.txt
Configure the database in settings.py.
Run migrations:

python manage.py migrate
Start the server:

python manage.py runserver
Set up the frontend:

Navigate to the frontend directory:

cd frontend
Install npm dependencies:

npm install
Start the frontend server:

npm start
Usage
Access the backend API at http://127.0.0.1:8000.
Use the React frontend at http://localhost:3000 for a user-friendly interface.
Log in as a Librarian or Patron to manage and view books, users, and borrowing statuses.
Project Structure
backend/: Django backend with models, views, and API endpoints.
frontend/: React frontend with components, pages, and styling.
static/: Static assets for frontend design (e.g., images, CSS).
scripts/: Optional utility scripts for database operations.
