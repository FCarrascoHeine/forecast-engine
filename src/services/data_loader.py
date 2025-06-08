import os
from typing import List

class DataLoader:
    def __init__(self, base_path: str = "data"):
        self.base_path = base_path

    def list_csv_files(self) -> List[str]:
        return [
            f for f in os.listdir(self.base_path)
            if f.endswith(".csv")
        ]
