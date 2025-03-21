import { useState } from "react";
import "./index.css"; // Using styles from index.css

const PredictComponent = () => {
  const [inputData, setInputData] = useState({
    sensor_id: "",
    areagrid: "",
    droughtalert: "",
    humidity: "",
    temperature: "",
  });

  const [prediction, setPrediction] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setInputData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          sensor_id: inputData.sensor_id,
          areagrid: inputData.areagrid,
          droughtalert: parseFloat(inputData.droughtalert),
          humidity: parseFloat(inputData.humidity),
          temperature: parseFloat(inputData.temperature),
        }),
      });

      if (!response.ok) {
        throw new Error(`HTTP Error! Status: ${response.status}`);
      }

      const data = await response.json();
      setPrediction(data);
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h2>Predict Sensor Data</h2>
      <form onSubmit={handleSubmit} className="sensor-form">
        <input
          type="text"
          name="sensor_id"
          value={inputData.sensor_id}
          onChange={handleChange}
          placeholder="Sensor ID"
          required
        />

        <input
          type="text"
          name="areagrid"
          value={inputData.areagrid}
          onChange={handleChange}
          placeholder="Area Grid"
          required
        />

        <input
          type="number"
          step="0.01"
          name="droughtalert"
          value={inputData.droughtalert}
          onChange={handleChange}
          placeholder="Drought Alert (e.g., 0.3)"
          required
        />

        <input
          type="number"
          step="0.1"
          name="humidity"
          value={inputData.humidity}
          onChange={handleChange}
          placeholder="Humidity (%)"
          required
        />

        <input
          type="number"
          step="0.1"
          name="temperature"
          value={inputData.temperature}
          onChange={handleChange}
          placeholder="Temperature (°C)"
          required
        />

        <button type="submit" disabled={loading}>
          {loading ? "Predicting..." : "Get Prediction"}
        </button>
      </form>

      {prediction && <div className="response-box">Prediction: {JSON.stringify(prediction)}</div>}
      {error && <div className="error-box">Error: {error}</div>}
    </div>
  );
};

export default PredictComponent;
