from database.connection import get_connection

def get_inventory_status():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT p.id, p.name, p.sku, i.stock_quantity, i.last_updated
        FROM inventory i
        JOIN products p ON i.product_id = p.id
        WHERE i.stock_quantity < 50
    """
    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results

def update_inventory_stock(product_id: int, new_stock: int):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
        UPDATE inventory
        SET stock_quantity = %s, last_updated = NOW()
        WHERE product_id = %s
    """
    cursor.execute(query, (new_stock, product_id))
    conn.commit()

    affected = cursor.rowcount

    cursor.close()
    conn.close()

    return {"message": "Inventory updated", "rows_affected": affected}
