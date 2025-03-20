package com.precisionagri.precisionagri.DTO;

import java.util.List;

public class SensorIdResponse {
    private List<String> sensorIds;

    public SensorIdResponse(List<String> sensorIds) {
        this.sensorIds = sensorIds;
    }

    public List<String> getSensorIds() {
        return sensorIds;
    }

    public void setSensorIds(List<String> sensorIds) {
        this.sensorIds = sensorIds;
    }
}

