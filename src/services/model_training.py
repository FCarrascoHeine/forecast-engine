import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

target_column = "Demand"

class ModelTrainer:
    def train_linear_regression(self, df: pd.DataFrame) -> float:
        """
        Train a linear regression model on the provided DataFrame.
        """
        if target_column not in df.columns:
            raise ValueError(f"Data must contain a {target_column} column.")

        X = df.select_dtypes(include='number').drop(target_column, axis=1)
        y = df[target_column]

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        r2_value = r2_score(y_test, y_pred)

        return r2_value
