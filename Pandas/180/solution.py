import pandas as pd

def consecutive_numbers(logs: pd.DataFrame) -> pd.DataFrame:
    logs['isConsecutive'] = logs['num'].rolling(window=3).apply(lambda x: len(set(x)) == 1, raw=True)

    consecutive_logs = logs[logs['isConsecutive'] == 1]

    return consecutive_logs[['num']].drop_duplicates().rename(columns={'num': 'ConsecutiveNums'})
