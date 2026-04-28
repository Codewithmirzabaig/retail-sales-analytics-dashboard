import sqlite3
import pandas as pd
import os

conn = sqlite3.connect("data/retail.db")
os.makedirs("reports", exist_ok=True)

queries = {
    "category_sales": """
        SELECT Category, ROUND(SUM(Sales), 2) AS total_sales
        FROM sales
        GROUP BY Category
        ORDER BY total_sales DESC;
    """,
    "top_subcategories": """
        SELECT "Sub-Category", ROUND(SUM(Sales), 2) AS total_sales
        FROM sales
        GROUP BY "Sub-Category"
        ORDER BY total_sales DESC
        LIMIT 10;
    """,
    "region_profit": """
        SELECT Region, ROUND(SUM(Profit), 2) AS total_profit
        FROM sales
        GROUP BY Region
        ORDER BY total_profit DESC;
    """,
    "loss_making_products": """
        SELECT "Sub-Category", ROUND(SUM(Profit), 2) AS total_profit
        FROM sales
        GROUP BY "Sub-Category"
        HAVING total_profit < 0
        ORDER BY total_profit;
    """
}

for name, query in queries.items():
    df = pd.read_sql_query(query, conn)
    df.to_csv(f"reports/{name}.csv", index=False)
    print(f"Saved: reports/{name}.csv")
    print(df)
    print("-" * 40)

conn.close()