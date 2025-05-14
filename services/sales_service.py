from database.connection import get_connection

def get_sales_data(start_date=None, end_date=None):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT s.id, s.sale_date, s.quantity, s.total_amount,
               p.name AS product_name, c.name AS category_name
        FROM sales s
        JOIN products p ON s.product_id = p.id
        JOIN categories c ON p.category_id = c.id
        WHERE (%s IS NULL OR s.sale_date >= %s)
          AND (%s IS NULL OR s.sale_date <= %s)
    """
    cursor.execute(query, (start_date, start_date, end_date, end_date))
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
