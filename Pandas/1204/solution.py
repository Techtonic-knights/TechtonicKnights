import pandas as pd

def last_passenger(queue: pd.DataFrame) -> pd.DataFrame:
    queue.sort_values(by='turn', inplace=True)
    total_weight = queue['weight'].cumsum()
    filtered_row = queue[total_weight <= 1000].iloc[-1:]
    return filtered_row[['person_name']]
