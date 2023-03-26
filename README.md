# FastAPI To-Do App

A simple To-Do application using FastAPI, Pydantic, and PostgreSQL.

## Setup and Installation

Follow these steps to set up and run the project:

### 1. Clone the repository

Clone the repository to your local machine:

git clone https://github.com/JohnCarra/todolist.git
cd todolist

### 2. Set up a virtual environment (optional but recommended)

Create and activate a virtual environment to isolate the project's dependencies:

python -m venv venv
source venv/bin/activate # For Linux and macOS
venv\Scripts\activate # For Windows

### 3. Install the required packages

Install the required Python packages using the following command:

pip install -r requirements.txt

### 4. Configure the database connection

Create a `.env` file in the project folder and add the following environment variables:

DB_HOST=<your_database_host>
DB_NAME=<your_database_name>
DB_USER=<your_database_user>
DB_PASSWORD=<your_database_password>

Replace `<your_database_host>`, `<your_database_name>`, `<your_database_user>`, and `<your_database_password>` with your actual PostgreSQL database connection details.

### 5. Set up the database

Run the `setup.sql` script to create the required tables and grant access to the specified user:

psql -h <your_database_host> -U <your_database_user> -d <your_database_name> -f setup.sql

Replace `<your_database_host>`, `<your_database_user>`, and `<your_database_name>` with your actual PostgreSQL database connection details.

### 6. Run the FastAPI server

Start the FastAPI server using the following command:

uvicorn main:app --reload

The server will be available at `http://127.0.0.1:8000`.

### 7. Explore the API

Visit `http://127.0.0.1:8000/docs` to access the interactive API documentation and test the endpoints.
