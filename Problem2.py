import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    a=tweets[tweets['content'].str.len()>15]
    b=a[['tweet_id']]
    return b