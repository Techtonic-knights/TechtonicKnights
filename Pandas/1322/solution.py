import pandas as pd

def ads_performance(ads: pd.DataFrame) -> pd.DataFrame:
    ads_df = ads.groupby('ad_id')['action'].value_counts().unstack(fill_value=0)
    
    ads_df['Clicked'] = ads_df.get('Clicked', 0)
    ads_df['Viewed'] = ads_df.get('Viewed', 0)

    ads_df = (ads_df['Clicked'] / (ads_df['Clicked'] + ads_df['Viewed']) * 100) \
    .fillna(0) \
    .round(2) \
    .reset_index() \
    .rename(columns={0: 'ctr'}) \
    .sort_values(by=['ctr', 'ad_id'], ascending=[False, True])
    
    return ads_df
