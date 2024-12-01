import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    df = orders.groupby('customer_number').agg(order_count=('order_number', 'count')).reset_index()
    return df[df['order_count'] == df['order_count'].max()][['customer_number']]
