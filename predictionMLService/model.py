import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import joblib

# Load the dataset
df = pd.read_csv(r"C:\Users\Arghya\PrecisionAgricultureAnalyticsSystem\iotdatagenerator\predictionMLService\training_data.csv")

# Step 1: Define Features (X) and Target Variable (y)
X = df.drop(columns=["energy_usage", "timestamp"])  # Features
y = df["energy_usage"]  # Target Variable

print(X)
print(y)


# Step 2: Identify Feature Types
categorical_features = ["sensor_id", "areagrid"]
numerical_features = ["droughtalert", "humidity", "temperature"]


# Step 3: Preprocessing - OneHotEncode Categorical & Scale Numerical Features
preprocessor = ColumnTransformer([
    ("num", StandardScaler(), numerical_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features)
])



# Step 4: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)

# Step 5: Linear Regression Pipeline
model = Pipeline([
    ("preprocessor", preprocessor),
    ("regressor", LinearRegression())
])

# Step 6: Train the Model
model.fit(X_train, y_train)

# Step 7: Model Evaluation
y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"📊 Model Evaluation: RMSE: {rmse:.2f}")

# Save the model as a .pkl file
model_filename = r"C:\Users\Arghya\PrecisionAgricultureAnalyticsSystem\iotdatagenerator\predictionMLService\linear_regression_model.pkl"
joblib.dump(model, model_filename)

print(f"Model saved to {model_filename}")