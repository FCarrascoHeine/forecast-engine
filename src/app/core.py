import pandas as pd
from fastapi import UploadFile

class CSVProcessor:
    """
    Core business logic class for handling CSV files.
    """

    async def read_csv(self, upload_file: UploadFile) -> pd.DataFrame:
        """
        Read the uploaded CSV file asynchronously into a pandas DataFrame.

        Parameters:
            upload_file (UploadFile): The uploaded file object from FastAPI.

        Returns:
            pd.DataFrame: Parsed CSV data.
        """
        # Read file content bytes asynchronously
        content = await upload_file.read()

        # Convert bytes to a string buffer and load to pandas
        from io import StringIO
        s = StringIO(content.decode("utf-8"))

        # Read CSV using pandas
        df = pd.read_csv(s)
        return df
