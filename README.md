# FastAPI To-Do App
A simple To-Do application using FastAPI, Pydantic, SQLite and React.

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

