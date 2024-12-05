import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    df = (actor_director.groupby(['actor_id', 'director_id'])
        .size()
        .loc[lambda x: x >= 3]
        .reset_index())
    return df[['actor_id', 'director_id']]    

