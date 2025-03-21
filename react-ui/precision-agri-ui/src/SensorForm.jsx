import { useState } from "react";
import "./index.css"; // Import CSS file

const SensorForm = () => {
  const [sensorData, setSensorData] = useState({
    sensorId: "",
    machineId: "",
    sensorType: "",
    installationDate: "",
  });

  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleChange = (e) => {
    const { name, value } = e.target;
    setSensorData((prev) => ({
      ...prev,
      [name]: value,
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError(null);

    const payload = {
      sensorId: sensorData.sensorId,
      machine: { machineId: sensorData.machineId },
      sensorType: sensorData.sensorType,
      installationDate: sensorData.installationDate,
    };

    try {
      const res = await fetch("http://localhost:8080/sensors/create", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(payload),
      });

      if (!res.ok) {
        throw new Error(`HTTP error! Status: ${res.status}`);
      }

      const data = await res.json();
      setResponse(data);
      setSensorData({ sensorId: "", machineId: "", sensorType: "", installationDate: "" });
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="form-container">
      <h2>Create Sensor</h2>
      <form onSubmit={handleSubmit} className="sensor-form">
        <input
          type="text"
          name="sensorId"
          value={sensorData.sensorId}
          onChange={handleChange}
          placeholder="Sensor ID"
          required
        />

        <input
          type="text"
          name="machineId"
          value={sensorData.machineId}
          onChange={handleChange}
          placeholder="Machine ID"
          required
        />

        <select
          name="sensorType"
          value={sensorData.sensorType}
          onChange={handleChange}
          required
        >
          <option value="">Select Sensor Type</option>
          <option value="Humidity">Humidity</option>
          <option value="Temperature">Temperature</option>
          <option value="Pressure">Pressure</option>
        </select>

        <input
          type="date"
          name="installationDate"
          value={sensorData.installationDate}
          onChange={handleChange}
          required
        />

        <button type="submit" disabled={loading}>
          {loading ? "Submitting..." : "Submit"}
        </button>
      </form>

      {response && <div className="response-box">Sensor Created Successfuly </div>}
      {error && <div className="error-box">Error: {error}</div>}
    </div>
  );
};

export default SensorForm;
