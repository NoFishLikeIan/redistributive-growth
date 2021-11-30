import pandas as pd

def read_fred(raw:pd.DataFrame) -> pd.DataFrame:

    data = raw.iloc[2:, :].dropna(how = 'all')
    data['sasdate'] = data.sasdate.apply(pd.to_datetime)
    data = data.set_index('sasdate')

    return data