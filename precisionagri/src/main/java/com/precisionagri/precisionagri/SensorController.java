package com.precisionagri.precisionagri;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import com.precisionagri.precisionagri.Models.Sensor;
import com.precisionagri.precisionagri.Service.SensorService;
import com.precisionagri.precisionagri.DTO.SensorIdResponse;


import java.util.List;

@RestController
@RequestMapping("/sensors")
public class SensorController {

    @Autowired
    private SensorService sensorService;

    // Add Sensor to Machine
    @PostMapping("/create")
    public Sensor addSensor(@RequestBody Sensor sensor) {
        return sensorService.addSensorToMachine(sensor);

    }

    // Get only Sensor IDs for a Machine
    @GetMapping("/machine")
    public ResponseEntity<SensorIdResponse> getSensorIdsByMachine(@RequestParam String machineId) {
        System.out.println("Machine ID: " + machineId);
        List<String> sensorIds = sensorService.getSensorsByMachineId(machineId);
        return ResponseEntity.ok(new SensorIdResponse(sensorIds));
    }


}

