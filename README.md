A FastAPI backend that manages students, instructors, classes, and enrollments for a dance academy. Built using Python, SQLAlchemy, JWT authentication, and Docker.
## 📂 Tech Stack
- **FastAPI** – Web framework
- **SQLAlchemy** – ORM for database models
- **SQLite** – Local file-based database
- **Python-Jose & Passlib** – JWT authentication and password hashing
- **Docker** – Containerization
- **Render** – Free deployment platform

## 🔐 Authentication
- `POST /auth/register` – Register a new user
- `POST /auth/login` – Login and get a JWT token
- Use the token in the `Authorization` header.
  
Visit https://dance-academy-api.onrender.com/docs as it's deployed on Render.
**OR**
Run with Docker
# Build Docker image
docker build -t dance-academy-api .

# Run the container
docker run -d -p 8000:8000 dance-academy-api
Visit http://localhost:8000/docs#/
