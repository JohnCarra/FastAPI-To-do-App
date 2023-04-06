# FastAPI To-Do App
This is a To-Do application built using FastAPI, Pydantic, and SQLite for the backend, and React for the frontend. The application allows users to create, read, update, and delete to-do items, and all the data is stored in a SQLite database. The backend is built using FastAPI and uses Pydantic for validation, while the frontend is built using React and uses Axios to make HTTP requests to the backend API. The application can be run locally using Docker Compose.

## 1. Clone the repository
Clone the repository to your local machine:

git clone https://github.com/JohnCarra/todolist.git  

cd todolist

## Requirements 
### The requirements for this repository are:

Python 3.6 or higher  
FastAPI  
aiosqlite  
pydantic   

### Additionally, if you want to use the Docker setup, you will also need:

Docker  
docker-compose  
### To run the React front-end, you will need:

Node.js  
React  
react-router-dom  
axios  
### To run the FastAPI server, you will need to install the required Python packages using the following command:  

pip install -r requirements.txt  

## Starting it up
### To run the React front-end, navigate to the todolist-frontend directory and run the following commands:

npm install  
npm start  

### To run the FastAPI: 
cd todolist/backend  
uvicorn main:app --reload  

### To run the entire application using Docker, run the following command from the root directory of the repository:

docker-compose up  
This will build and start both the FastAPI server and the React front-end.   

