# Readstack API

Backend service for Readstack, a newsletter aggregation platform. This API, built with FastAPI and SQLAlchemy, provides robust endpoints for managing newsletters and categories, complete with filtering, sorting, and pagination.

## ✨ Features

- **Newsletter Management**: CRUD operations for newsletters.
- **Category Management**: CRUD operations for categories.
- **Advanced Filtering**: Filter newsletters by category.
- **Dynamic Sorting**: Sort newsletters by `published_date`, `created_at`, `source`, or `title`.
- **Pagination**: Efficiently browse through large sets of data using page and size parameters.
- **Data Aggregation**: Get statistics on newsletter counts per category.
- **Containerized**: Fully containerized with Docker and Docker Compose for easy setup and deployment.
- **Modern Tech Stack**: Built with Python 3.11, FastAPI, and `uv` for dependency management.

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Dependency Management**: uv
- **Containerization**: Docker, Docker Compose
- **Linting & Formatting**: Ruff, MyPy

## 🚀 Getting Started

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/rabberdabber/readstack-api.git
    cd readstack-api
    ```

2.  **Run the application:**
    ```bash
    docker compose up --build
    ```
    The API will be available at `http://localhost:8000`.

## 📖 API Documentation

Interactive API documentation (provided by Swagger UI) is available at `http://localhost:8000/docs` when the application is running.

### Main Endpoints

#### Newsletters

- `GET /newsletters/`: List all newsletters with filtering, sorting, and pagination.
- `POST /newsletters/`: Create a new newsletter.
- `GET /newsletters/{newsletter_id}`: Get a single newsletter by ID.

#### Categories

- `GET /categories/`: List all categories.
- `POST /categories/`: Create a new category.
- `GET /categories/{category_id}`: Get a single category by ID.
- `GET /categories/stats/`: Get newsletter count statistics for each category.

## 📁 Project Structure

```
readstack-api/
├── app/
│   ├── api/
│   │   └── routers/
│   │       ├── __init__.py
│   │       ├── categories.py
│   │       └── newsletters.py
│   ├── __init__.py
│   ├── config.py       # Pydantic settings management
│   ├── crud.py         # Database CRUD operations
│   ├── database.py     # Database session and engine setup
│   ├── deps.py         # FastAPI dependencies (e.g., pagination)
│   ├── main.py         # Main FastAPI application
│   ├── models.py       # SQLAlchemy ORM models
│   └── schemas.py      # Pydantic schemas
├── Dockerfile          # Docker configuration for the application
├── compose.yaml        # Docker Compose setup for services
├── pyproject.toml      # Project metadata and dependencies
└── README.md
```
