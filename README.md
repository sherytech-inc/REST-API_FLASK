# REST-API_FLASK
# 📝 Flask Todo API

A lightweight and beginner-friendly RESTful API for managing a simple in-memory Todo list using **Flask**!  
Perfect for quick testing, tutorials, and Python web development practice. 🚀

## 🔧 Features

- ✅ Add new todo items
- 📋 Retrieve all todos
- 🕵️ Get a specific todo by ID
- ✏️ Update existing todos
- 🗑️ Delete todos by ID

## 🧪 Tech Stack

- **Python 3.x**
- **Flask** – A micro web framework

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/flask-todo-api.git
   cd flask-todo-api
   ```

2. (Optional) Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the app:
   ```bash
   python app.py
   ```

The API will be live at: `http://localhost:5000`

## 📬 API Endpoints

| Method | Endpoint              | Description                    |
|--------|------------------------|--------------------------------|
| GET    | `/get_todos`          | Retrieve all todos             |
| GET    | `/get_todo/<id>`      | Get a specific todo by ID      |
| POST   | `/add_todo`           | Add a new todo (JSON body)     |
| PUT    | `/update_todo/<id>`   | Update an existing todo        |
| DELETE | `/delete_todo/<id>`   | Delete a todo by its ID        |

### Sample JSON for POST or PUT
```json
{
  "task": "Learn Flask with style"
}
```

## 📌 Notes

- All todos are stored **in-memory**, meaning data resets on restart.
- Ideal for learning RESTful concepts or pairing with a frontend.

