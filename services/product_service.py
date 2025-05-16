from database.connection import get_connection
from models.schemas import ProductCreate
import mysql.connector

def register_product(data: ProductCreate):
    conn = get_connection()
    cursor = conn.cursor()

    product_query = """
        INSERT INTO products (name, description, category_id, price)
        VALUES (%s, %s, %s, %s)
    """

    inventory_query = """
        INSERT INTO inventory (product_id, quantity, updated_at)
        VALUES (%s, %s, NOW())
    """

    try:
        # Insert product
        cursor.execute(product_query, (
            data.name,
            data.description,
            data.category_id,
            data.price
        ))

        product_id = cursor.lastrowid

        # Insert inventory entry
        cursor.execute(inventory_query, (
            product_id,
            data.quantity
        ))

        conn.commit()

    except mysql.connector.Error as err:
        conn.rollback()
        return {"error": f"MySQL Error: {err.msg}"}

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}

    finally:
        cursor.close()
        conn.close()

    return {"message": "Product registered successfully", "product_id": product_id}
