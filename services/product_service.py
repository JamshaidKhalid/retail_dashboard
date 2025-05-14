from database.connection import get_connection

def register_product(data):
    conn = get_connection()
    cursor = conn.cursor()

    product_query = """
        INSERT INTO products (id, name, sku, price, category_id, brand_id)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    inventory_query = """
        INSERT INTO inventory (product_id, stock_quantity, last_updated)
        VALUES (%s, %s, NOW())
    """

    try:
        cursor.execute(product_query, (
            data["id"], data["name"], data["sku"], data["price"],
            data["category_id"], data["brand_id"]
        ))

        cursor.execute(inventory_query, (
            data["id"], data["stock_quantity"]
        ))

        conn.commit()

    except Exception as e:
        conn.rollback()
        return {"error": str(e)}
    finally:
        cursor.close()
        conn.close()

    return {"message": "Product registered successfully"}
