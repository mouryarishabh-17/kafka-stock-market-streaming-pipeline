def generate_sql(intent: dict) -> str:
    company = intent["company"]
    limit = intent.get("limit", 5)

    return f"""
    SELECT symbol, timestamp, close
    FROM stock_prices
    WHERE symbol = '{company}'
    ORDER BY timestamp DESC
    LIMIT {limit};
    """
