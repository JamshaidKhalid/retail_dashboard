from database.connection import get_connection

def get_inventory_status(quantity_threshold: int = 50):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            p.id AS product_id,
            p.name AS product_name,
            i.quantity AS stock_quantity,
            i.updated_at AS last_updated
        FROM inventory i
        JOIN products p ON i.product_id = p.id
        WHERE i.quantity < %s
    """
    cursor.execute(query, (quantity_threshold,))
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results

def update_inventory_stock(product_id: int, new_stock: int):
    conn = get_connection()
    cursor = conn.cursor()

    # Insert a log for the inventory change
    cursor.execute("SELECT quantity FROM inventory WHERE product_id = %s", (product_id,))
    current = cursor.fetchone()
    if not current:
        cursor.close()
        conn.close()
        return {"error": "Product not found in inventory"}

    old_stock = current[0]
    quantity_change = new_stock - old_stock
    change_type = 'INCREASE' if quantity_change > 0 else 'DECREASE'

    # Update inventory
    update_query = """
        UPDATE inventory
        SET quantity = %s, updated_at = NOW()
        WHERE product_id = %s
    """
    cursor.execute(update_query, (new_stock, product_id))

        # Log inventory change
    log_query = """
        INSERT INTO inventory_logs (product_id, quantity_change, change_type)
        VALUES (%s, %s, %s)
    """
    cursor.execute(log_query, (product_id, abs(quantity_change), change_type))

    conn.commit()
    affected = cursor.rowcount

    cursor.close()
    conn.close()

    return {
        "message": "Inventory updated",
        "rows_affected": affected,
        "change_type": change_type,
        "old_quantity": old_stock,
        "new_quantity": new_stock
    }
