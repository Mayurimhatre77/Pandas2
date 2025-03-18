import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    views = views[views['author_id'] == views['viewer_id']]
    views = views.rename(columns={'author_id' : 'id'})
    result = views[['id']].drop_duplicates()
    return result.sort_values(by='id')