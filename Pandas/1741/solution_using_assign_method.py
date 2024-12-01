import pandas as pd

def total_time(employees: pd.DataFrame) -> pd.DataFrame:
    total_time = (
        employees
        .assign(total_time=employees['out_time'] - employees['in_time'])
        .groupby(['emp_id', 'event_day'], as_index=False)['total_time']
        .sum()
        .rename(columns={'event_day': 'day'})
    )
    return total_time[['day', 'emp_id', 'total_time']]
