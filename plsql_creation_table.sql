CREATE TABLE users (
    user_id VARCHAR(50) PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    phone VARCHAR(15) UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE machines (
    machine_id VARCHAR(50) PRIMARY KEY,
    user_id VARCHAR(50) REFERENCES users(user_id) ON DELETE CASCADE,
    location VARCHAR(255),
    type VARCHAR(100),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Step 5: Create Sensors Table
CREATE TABLE sensors (
    sensor_id VARCHAR(50) PRIMARY KEY,
    machine_id VARCHAR(50) REFERENCES machines(machine_id) ON DELETE CASCADE,
    sensor_type VARCHAR(100) NOT NULL,
    installation_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Step 6: Create Thresholds Table
CREATE TABLE thresholds (
    threshold_id SERIAL PRIMARY KEY,
    machine_id VARCHAR(50) REFERENCES machines(machine_id) ON DELETE CASCADE,
    temperature_max FLOAT,
    humidity_min FLOAT,
    soil_moisture_min FLOAT,
    energy_usage_max FLOAT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Step 7: Create Alert Preferences Table
CREATE TABLE alert_preferences (
    alert_id SERIAL PRIMARY KEY,
    user_id VARCHAR(50) REFERENCES users(user_id) ON DELETE CASCADE,
    machine_id VARCHAR(50) REFERENCES machines(machine_id) ON DELETE CASCADE,
    notify_email BOOLEAN DEFAULT TRUE,
    notify_sms BOOLEAN DEFAULT FALSE,
    notify_push BOOLEAN DEFAULT TRUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Step 8: Create Sensor Data Table (Storing Readings)
CREATE TABLE sensor_data (
    data_id SERIAL PRIMARY KEY,
    sensor_id VARCHAR(50) REFERENCES sensors(sensor_id) ON DELETE CASCADE,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    temperature FLOAT,
    humidity FLOAT,
    soil_moisture FLOAT,
    energy_usage FLOAT
);

-- Step 9: Create Indexes for Faster Queries
CREATE INDEX idx_sensor_machine ON sensors(machine_id);
CREATE INDEX idx_threshold_machine ON thresholds(machine_id);
CREATE INDEX idx_alert_user ON alert_preferences(user_id);
CREATE INDEX idx_alert_machine ON alert_preferences(machine_id);
CREATE INDEX idx_sensor_data_sensor ON sensor_data(sensor_id);