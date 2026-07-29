"""Module for loading and displaying CSV dataset dimensions using Pandas."""

from typing import Optional
import pandas as pd


def load(path: str) -> Optional[pd.DataFrame]:
    """Loads a CSV file into a pandas DataFrame and displays its dimensions.

    Args:
        path (str): Filepath to the CSV dataset.

    Returns:
        Optional[pd.DataFrame]: Loaded DataFrame if successful, None on error.
    """
    if not isinstance(path, str):
        print("Error: path must be a string.")
        return None

    try:
        df = pd.read_csv(path)
        print(f"Loading dataset of dimensions {df.shape}")
        return df
    except FileNotFoundError:
        print(f"Error: The file at '{path}' was not found.")
    except pd.errors.EmptyDataError:
        print(f"Error: The file at '{path}' is empty.")
    except Exception as e:
        print(f"Error loading dataset: {e}")

    return None
