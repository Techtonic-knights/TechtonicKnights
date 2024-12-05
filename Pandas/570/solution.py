import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    manager_ids = (employee.groupby('managerId')
                .size()
                .loc[lambda x: x >= 5]
                .reset_index()
                )
    return employee[employee['id'].isin(manager_ids['managerId'])][['name']]
