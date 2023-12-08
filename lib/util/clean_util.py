import pandas as pd


def clean_column_with_mean(dataframe, column_name, replace=True):
    df = dataframe.copy()

    new_column_name = column_name
    if not replace:
        new_column_name = 'new_' + column_name
    df[new_column_name] = pd.to_numeric(df[column_name], errors='coerce')
    mean_value = df[new_column_name].mean()
    df[new_column_name].fillna(mean_value, inplace=True)

    return df


