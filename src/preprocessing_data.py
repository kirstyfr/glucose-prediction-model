import pandas as pd

def calculate_moving_avg_and_count(df, window):
    # define moving average
    def calculate_sma(data, window):
        return data.rolling(window=window).mean()
    # add running average column
    df['SMA'] = calculate_sma(df['current_nA'], window)
    # difference from moving average
    df['moving_avg_diff']= abs(df['SMA']-df['current_nA'])
    # add seconds after glucose column
    df['seconds_after_glucose']=df.groupby(['substrate_reference_mM']).cumcount()
    return df

def filter_by_threshold_second_limit(df, threshold, seconds_after):
    # Filter based on threshold and seconds_after_glucose
    df_filtered = df[
        (df['moving_avg_diff'] < threshold) & 
        (df['substrate_reference_mM'] > 0) & 
        (df['seconds_after_glucose'] > seconds_after)
    ]
 
    return df_filtered
