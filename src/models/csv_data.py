import pandas as pd

class CSVData:
    def __init__(self, dataframe: pd.DataFrame):
        self.df = dataframe

    @classmethod
    def from_csv_string(cls, csv_string: str) -> "CSVData":
        """
        Factory method to create CSVData from a CSV string.
        """
        df = pd.read_csv(pd.io.common.StringIO(csv_string))
        return cls(df)

    def shape(self):
        return self.df.shape  # returns (rows, columns)

    def columns(self):
        return list(self.df.columns)

    def column_types(self):
        """
        Returns a dict of {column_name: data_type}
        """
        return self.df.dtypes.apply(lambda dt: str(dt)).to_dict()

    def numeric_stats(self):
        """
        Returns basic stats (count, mean, std, min, max) for numeric columns.
        Result is a dict keyed by column with the stats as sub-dict.
        """
        stats_df = self.df.describe().transpose()
        stats = {}
        for col in stats_df.index:
            stats[col] = {
                "count": int(stats_df.loc[col, "count"]),
                "mean": float(stats_df.loc[col, "mean"]),
                "std": float(stats_df.loc[col, "std"]),
                "min": float(stats_df.loc[col, "min"]),
                "max": float(stats_df.loc[col, "max"]),
            }
        return stats
