import pandas as pd

from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score

class ModelTrainer:
    def train_linear_regression(self, df: pd.DataFrame) -> float:
        """
        Train a linear regression model on the provided DataFrame.
        """
        if 'Demand' not in df.columns:
            raise ValueError("Data must contain a 'Demand' column.")

        X = df[["Price", "Stock_Level"]]
        y = df['Demand']

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

        model = LinearRegression()
        model.fit(X_train, y_train)

        y_pred = model.predict(X_test)
        r2_value = r2_score(y_test, y_pred)

        return r2_value
