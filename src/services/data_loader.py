import os
import pandas as pd

class DataLoader:
    def __init__(self, base_path: str = "data"):
        """
        Initialize the DataLoader with a base path.
        This is the directory where CSV files are stored.
        """
        self.base_path = base_path

    def list_csv_files(self) -> list[str]:
        """
        List all CSV files in the base directory.

        Returns:
            List of filenames (strings) that end with '.csv'.
        """
        # Use os.listdir to get all entries in the base_path folder
        # Filter to include only files that end with '.csv'
        return [
            f for f in os.listdir(self.base_path)
            if f.endswith(".csv")
        ]
    
    def load_csv_as_df(self, filename: str) -> pd.DataFrame:
        """Load a CSV file as a pandas DataFrame."""
        filepath = os.path.join(self.base_path, filename)
        if not os.path.isfile(filepath):
            raise FileNotFoundError(f"{filepath} does not exist.")
        return pd.read_csv(filepath)
