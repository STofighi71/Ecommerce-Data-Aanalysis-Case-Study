import pandas as pd
import numpy as np

np.random.seed(42)

# ------------------------
# CUSTOMERS
# ------------------------
n_customers = 500
customers = pd.DataFrame({
    "customer_id": range(1, n_customers+1),
    "country": np.random.choice(["France", "Germany", "Spain", "Italy"], n_customers),
    "segment": np.random.choice(["Consumer", "Corporate", "Small Business"], n_customers),
    "signup_date": pd.to_datetime("2023-01-01") + pd.to_timedelta(np.random.randint(0, 700, n_customers), unit="D")
})

# introduce missing values
customers.loc[np.random.choice(customers.index, 20), "country"] = None

# ------------------------
# PRODUCTS
# ------------------------
n_products = 100
products = pd.DataFrame({
    "product_id": range(1, n_products+1),
    "category": np.random.choice(["Electronics", "Clothing", "Home", "Sports"], n_products),
    "price": np.round(np.random.uniform(5, 500, n_products), 2)
})

# ------------------------
# ORDERS
# ------------------------
n_orders = 2000
orders = pd.DataFrame({
    "order_id": range(1, n_orders+1),
    "customer_id": np.random.choice(customers["customer_id"], n_orders),
    "order_date": pd.to_datetime("2024-01-01") + pd.to_timedelta(np.random.randint(0, 365, n_orders), unit="D"),
    "status": np.random.choice(["Delivered", "Cancelled", "Returned"], n_orders, p=[0.8, 0.1, 0.1])
})

# duplicate rows (real issue)
orders = pd.concat([orders, orders.sample(50)])

# ------------------------
# ORDER ITEMS
# ------------------------
n_items = 5000
order_items = pd.DataFrame({
    "order_item_id": range(1, n_items+1),
    "order_id": np.random.choice(orders["order_id"], n_items),
    "product_id": np.random.choice(products["product_id"], n_items),
    "quantity": np.random.randint(1, 5, n_items)
})

# ------------------------
# PAYMENTS
# ------------------------
payments = pd.DataFrame({
    "payment_id": range(1, n_orders+1),
    "order_id": orders["order_id"].sample(n_orders, replace=False).values,
    "payment_method": np.random.choice(["Card", "PayPal", "Bank Transfer"], n_orders),
    "payment_status": np.random.choice(["Success", "Failed"], n_orders, p=[0.9, 0.1])
})

# ------------------------
# SAVE FILES
# ------------------------
customers.to_csv("customers.csv", index=False)
products.to_csv("products.csv", index=False)
orders.to_csv("orders.csv", index=False)
order_items.to_csv("order_items.csv", index=False)
payments.to_csv("payments.csv", index=False)

print("Dataset generated successfully with real-world issues.")