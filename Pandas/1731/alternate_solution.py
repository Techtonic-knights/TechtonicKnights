import pandas as pd

def count_employees(employees: pd.DataFrame) -> pd.DataFrame:
    manager_stats = employees[employees['reports_to'].notna()].groupby('reports_to').agg(
    reports_count=('reports_to', 'size'),
    average_age=('age',  lambda x: round(x.mean()) if x.mean() % 1 < 0.5 else np.ceil(x.mean()))
    ).reset_index()

    managers = employees[employees['employee_id'].isin(manager_stats['reports_to'])]

    return pd.merge(managers, manager_stats, left_on=['employee_id'], right_on=['reports_to'])[['employee_id','name', 'reports_count', 'average_age' ]].sort_values(by = 'employee_id')
