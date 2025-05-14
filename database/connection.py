import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os
import logging

# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def get_connection():
    try:
        # Fetch values from environment variables
        host = os.getenv("DB_HOST")
        user = os.getenv("DB_USER")
        password = os.getenv("DB_PASSWORD")
        database = os.getenv("DB_DATABASE")

        # Check if any environment variable is missing
        if not all([host, user, password, database]):
            logger.error("One or more required environment variables are missing.")
            return None

        # Establish the database connection
        connection = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        # Check if the connection is successful
        if connection.is_connected():
            logger.info("Connection successful.")
            return connection
        else:
            logger.error("Connection failed.")
            return None
            
    except mysql.connector.Error as e:
        # Log detailed database connection errors
        logger.error(f"Database connection error: {e}")
        return None
    except Exception as e:
        # Catch any other exceptions
        logger.error(f"Unexpected error: {e}")
        return None
