import pandas as pd

def food_delivery(delivery: pd.DataFrame) -> pd.DataFrame:
    delivery['is_immediate'] = (delivery['order_date'] == delivery['customer_pref_delivery_date'])
    immediate_orders_percentage = (delivery['is_immediate'].mean() * 100)
    percentage_df = pd.DataFrame({'immediate_percentage': [round(immediate_orders_percentage, 2)]})
    return percentage_df
