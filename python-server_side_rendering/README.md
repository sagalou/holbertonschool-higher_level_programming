# Python - Server-Side Rendering

## Description

This project explores Server-Side Rendering (SSR) in Python. Unlike client-side rendering, where the browser builds the page using JavaScript, SSR generates fully formed HTML pages directly on the server before sending them to the client.

The project covers:
- Generating text files from a template with placeholders
- Building a Flask application that renders HTML templates
- Using the Jinja2 templating engine (loops, conditions)
- Reading and dynamically displaying data from JSON, CSV, and SQLite

## Learning Objectives

- Understand the concepts of server-side rendering and how it differs from client-side rendering
- Learn the benefits of using server-side rendering in web development
- Implement SSR in Python using the Flask framework
- Use Jinja2 to dynamically generate HTML pages
- Read and display data from various sources (JSON, CSV, SQLite)
- Handle dynamic content and user inputs

## Requirements

- Python 3.x
- Flask (`pip install flask`)
- pycodestyle (Holberton style guide)

## Project Structure

```
python-server_side_rendering/
├── task_00_intro.py
├── template.txt
├── task_01_basic_flask_app.py
├── task_02_dynamic_content.py
├── task_03_json_csv_data.py
├── task_04_sqlite_data.py
├── items.json
├── items.csv
├── items.db
└── templates/
    ├── index.html
    ├── items.html
    └── data.html
```

## Tasks

| # | File | Description |
|---|------|-------------|
| 0 | `task_00_intro.py` | Generates personalized invitation files from a template and a list of attendees |
| 1 | `task_01_basic_flask_app.py` | Basic Flask app rendering a static HTML template |
| 2 | `task_02_dynamic_content.py` | Dynamic template using Jinja2 loops and conditions |
| 3 | `task_03_json_csv_data.py` | Displays data read from a JSON or CSV file via a URL parameter |
| 4 | `task_04_sqlite_data.py` | Extends the app to display data from a SQLite database |

## Usage

Run a Flask app:
```bash
python3 task_01_basic_flask_app.py
```

Then open in your browser: `http://127.0.0.1:5000/`

For the data-source tasks (task 3 and 4), specify the source via a URL parameter:
```
http://127.0.0.1:5000/data?source=json
http://127.0.0.1:5000/data?source=csv
http://127.0.0.1:5000/data?source=sql
```

## Author

Sagalou