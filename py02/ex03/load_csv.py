import pandas as pd


def load(path: str) -> pd.DataFrame:
    """
        Load a csv file in a dataframe.
        Can raise Exceptions.
    """
    df = pd.read_csv(path, index_col=0)
    print('Loading dataset of dimensions ', df.shape)
    return df
# df.iloc[:2, :4]
