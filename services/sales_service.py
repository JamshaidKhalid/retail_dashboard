from database.connection import get_connection


def get_sales_data(start_date=None, end_date=None, product_id=None, 
                    category_id=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT 
            s.id AS sale_id,
            s.sale_date,
            si.quantity,
            si.price_per_unit,
            (si.quantity * si.price_per_unit) AS total_price,
            p.name AS product_name,
            c.name AS category_name
        FROM sales s
        JOIN sale_items si ON s.id = si.sale_id
        JOIN products p ON si.product_id = p.id
        JOIN categories c ON p.category_id = c.id
        WHERE (%s IS NULL OR s.sale_date >= %s)
          AND (%s IS NULL OR s.sale_date <= %s)
          AND (%s IS NULL OR p.id = %s)
          AND (%s IS NULL OR c.id = %s)
    """
    cursor.execute(query, (start_date, start_date, end_date,
                   end_date, product_id, product_id, category_id, category_id))
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results


def get_revenue_summary(period: str):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    group_by_map = {
        "daily": "DATE(sale_date)",
        "weekly": "YEARWEEK(sale_date)",
        "monthly": "DATE_FORMAT(sale_date, '%Y-%m')",
        "yearly": "YEAR(sale_date)"
    }

    group_by = group_by_map.get(period, "DATE(sale_date)")

    query = f"""
        SELECT {group_by} AS period, SUM(total_amount) AS revenue
        FROM sales
        GROUP BY period
        ORDER BY period DESC
        LIMIT 20
    """

    cursor.execute(query)
    results = cursor.fetchall()

    cursor.close()
    conn.close()
    return results
