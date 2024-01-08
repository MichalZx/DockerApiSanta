# DockerApiSanta

This FastAPI application serves as an API for managing gifts and elves in Santa's workshop. It uses SQLite as a database to store information about gifts and elves.

## Setup

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/MichalZx/DockerApiSanta.git
   cd DockerApiSanta
   
2. Install dependencies:
pip install -r requirements.txt

3. Running Locally
Make sure you have SQLite installed, and create the SQLite database:
sqlite3 santa.db

4. In the SQLite prompt, you can run:
.read schema.sql
.exit
This will create the necessary tables for the application.

5. Run the FastAPI application:
uvicorn your_app_name:app --reload
Replace your_app_name with the actual name of your FastAPI application file.

6. Access the API documentation:
Open your browser and go to http://127.0.0.1:8000/docs to view and interact with the API using Swagger.

7. Docker Deployment
Build the Docker image:
docker build -t santas-workshop-api.

8. Run the Docker container:
docker run -p 8000:8000 santas-workshop-api
This will expose the application on http://127.0.0.1:8000.

Note
Ensure that the SQLite database file santa.db is present in the same directory as your FastAPI application.
Feel free to customize and expand upon this README as needed for your project.

In this README, I've added sections for Docker deployment. Make sure to replace `your-username` with your GitHub username in the clone command. Also, replace `your_app_name` with the actual name of your FastAPI application file as mentioned before.
