import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:

    employees['total_time'] = employees['out_time'] - employees['in_time']
    total_time = employees.groupby(['emp_id', 'event_day'], as_index=False).agg({'total_time': 'sum'})
    total_time.rename(columns = {'event_day': 'day'}, inplace=True)
    return total_time[['day', 'emp_id', 'total_time']]
