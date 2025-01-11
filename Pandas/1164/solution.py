import pandas as pd

def price_at_given_date(products: pd.DataFrame) -> pd.DataFrame:
    def get_new_price(x):
        condition = x['change_date'] <= '2019-08-16'
        if condition.any():
            idx = x['change_date'][condition].idxmax()
            return x['new_price'].loc[idx] 
        else:
            return 10

    return products.groupby('product_id').apply(get_new_price,include_groups=False).reset_index(name='price')
