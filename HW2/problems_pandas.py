import pandas as pd
from typing import List, Tuple, Any

def get_dataset_shape(df: pd.DataFrame) -> Tuple[int, int]:
    """
    Returns the shape of the dataframe as a tuple of (number of rows, number of columns).
    """
    raise NotImplementedError("Function not implemented")

def get_column_names(df: pd.DataFrame) -> List[str]:
    """
    Returns a list of all column names in the given dataframe.
    """
    raise NotImplementedError("Function not implemented")

def get_summary_statistics(df: pd.DataFrame, column_name: str) -> pd.Series:
    """
    Returns the summary statistics (using .describe()) for the specified column in the dataframe.
    """
    raise NotImplementedError("Function not implemented")

def get_nth_row(df: pd.DataFrame, n: int) -> pd.Series:
    """
    Returns the n-th row of the dataframe, using standard integer-based indexing.
    """
    raise NotImplementedError("Function not implemented")

def filter_by_drink_category(df: pd.DataFrame, category: str) -> pd.DataFrame:
    """
    Returns a dataframe containing only the rows where the "drink_category" matches the given category string.
    """
    raise NotImplementedError("Function not implemented")

def get_high_spenders(df: pd.DataFrame, min_spend: float) -> pd.DataFrame:
    """
    Returns a dataframe containing only the rows where the "total_spend" is STRICTLY GREATER THAN min_spend.
    """
    raise NotImplementedError("Function not implemented")

def get_mobile_rewards_members(df: pd.DataFrame) -> pd.DataFrame:
    """
    Returns a dataframe containing only the rows where the "order_channel" is 'Mobile App' 
    AND they are a rewards member ('is_rewards_member' is True).
    """
    raise NotImplementedError("Function not implemented")

def get_specific_regions(df: pd.DataFrame, regions: List[str]) -> pd.DataFrame:
    """
    Returns a dataframe containing only the rows where the "region" is one of the strings in the given list of regions.
    """
    raise NotImplementedError("Function not implemented")

