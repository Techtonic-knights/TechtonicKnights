import pandas as pd

def sales_person(sales_person: pd.DataFrame, company: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    try:
        red_company_id = company.loc[company['name'] == 'RED', 'com_id'].iloc[0]
    except IndexError:
        return sales_person[['name']]

    red_sales_ids = orders.loc[orders['com_id'] == red_company_id, 'sales_id']
    return sales_person.loc[~sales_person['sales_id'].isin(red_sales_ids), ['name']]
