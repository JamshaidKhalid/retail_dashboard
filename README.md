# FastAPI Project

This project is a FastAPI-based API server with MySQL. Create a MySQL database and follow the steps below to set up and run the project.

##  Environment Setup

1. **Create a Virtual Environment**
   ```bash
   python -m venv venv
   ```

2. **Activate the Virtual Environment**
   - On Windows:
     ```bash
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a .env file in root directory with these variables**
   ```bash
    DB_HOST=
    DB_USER=
    DB_PASSWORD=
    DB_DATABASE=
   ```

##  Database Schema Creation

Navigate to the `scripts` directory and run:

```bash
cd scripts
python create_schema.py
```

##  Start the API Server

Return to the root directory and run:

```bash
uvicorn main:app --reload
```

The server will be available at [http://127.0.0.1:8000](http://127.0.0.1:8000)

##  API Endpoints

Interactive API documentation:

- Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

##  Testing the API

You can test the API using:

- Swagger UI (browser interface)
- Postman (API client)
- `curl` (command line)

Example:

```bash
curl http://127.0.0.1:8000/inventory/
```
with optinal parameter on quantity of inventory

##  Notes

- Ensure your database is configured before running `create_schema.py`.
