#dummy training data generated throught gpt
import pandas as pd
import numpy as np

# Define possible values
sensor_ids = [f"S{i}" for i in range(1, 21)]
areagrids = ["A", "B", "C"]
timestamps = pd.date_range("2025-03-20 10:00:00", periods=20, freq="5min")

# Generate random data
np.random.seed(42)
data = {
    "sensor_id": np.random.choice(sensor_ids, 20),
    "areagrid": np.random.choice(areagrids, 20),
    "droughtalert": np.round(np.random.uniform(0.1, 0.5, 20), 2),
    "energy_usage": np.round(np.random.uniform(170, 230, 20), 1),
    "humidity": np.round(np.random.uniform(48, 56, 20), 1),
    "temperature": np.round(np.random.uniform(25, 32, 20), 1),
    "timestamp": timestamps,
    "soil_moisture": np.round(np.random.uniform(9.5, 15.5, 20), 1),
}

# Create training DataFrame
df = pd.DataFrame(data)
# Write DataFrame to CSV
output_path = r"C:\Users\Arghya\PrecisionAgricultureAnalyticsSystem\iotdatagenerator\predictionMLService\training_data.csv"
df.to_csv(output_path, index=False)
print(df)