# 📋 ToDo App - CRUD API with FastAPI and SQLAlchemy

### Overview

This project is a simple ToDo application built using **FastAPI** for the backend API and **SQLAlchemy** as the ORM (Object-Relational Mapping) tool to interact with a **MySQL** database. The app provides a CRUD (Create, Read, Update, Delete) API to manage tasks, allowing users to create, retrieve, update, and delete todos.

### Features

- **Create a ToDo**: Add a new todo item.
- **Read Todos**: Retrieve a list of all todos or a specific todo by ID.
- **Update a ToDo**: Modify an existing todo item.
- **Delete a ToDo**: Remove a todo item from the list.

### Tech Stack

- **Backend Framework**: [FastAPI](https://fastapi.tiangolo.com/)
- **Database**: MySQL
- **ORM**: [SQLAlchemy](https://www.sqlalchemy.org/)
- **Database Driver**: `mysql-connector-python`
- **Other Dependencies**: `pydantic`, `uvicorn`,`pymysql`, `python-dotenv`

### Getting Started

To get started with the project, follow these steps:

#### Prerequisites

- Python 3.7+
- MySQL Server
- `pip` (Python package manager)

#### Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/bhagwati021/To_do_using_fast_api.git
   cd To_do_using_fast_api
   ```

2. **Create a virtual environment:**

   ```bash
   python -m venv venv
   ```

   Activate the virtual environment:

   - On Windows:

     ```bash
     venv\Scripts\activate
     ```

   - On macOS/Linux:

     ```bash
     source venv/bin/activate
     ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure the Database:**

   - Make sure your MySQL server is running.
   - Create a new database:

     ```sql
     CREATE DATABASE database;
     ```

   - Update the `DATABASE_URL` in `database.py` with your MySQL credentials:

   ```python
   DATABASE_URL = "mysql+mysqlconnector://<username>:<password>@localhost:3306/database"
   ```

5. **Run the application:**

   ```bash
   uvicorn main:app --reload
   ```

   The app will run at `http://127.0.0.1:8000`.

### API Endpoints

The following endpoints are available in the API:

- **GET** `/todos/` - Retrieve all todos
- **GET** `/todos/{todo_id}` - Retrieve a todo by its ID
- **POST** `/todos/` - Create a new todo
- **PUT** `/todos/{todo_id}` - Update an existing todo
- **DELETE** `/todos/{todo_id}` - Delete a todo

#### Example Requests

- **Create a ToDo:**

  ```http
  POST /todos/
  Content-Type: application/json

  {
    "title": "Buy groceries",
    "completed": 0
  }
  ```

- **Get All ToDos:**

  ```http
  GET /todos/
  ```

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

### Contact

For any questions or feedback, feel free to reach out at [bhagwatibashyal1234@gmail.com].

---
