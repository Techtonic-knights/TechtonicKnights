import pandas as pd

def find_primary_department(employee: pd.DataFrame) -> pd.DataFrame:
    return employee.loc[employee.groupby('employee_id')['primary_flag'].idxmax()][['employee_id', 'department_id']]
