package com.precisionagri.precisionagri.Service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.precisionagri.precisionagri.Models.Sensor;
import com.precisionagri.precisionagri.Repository.SensorRepository;

import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;

import com.precisionagri.precisionagri.Models.Machine;
import com.precisionagri.precisionagri.Repository.MachineRepository;

import java.util.ArrayList;
import java.util.List;

@Service
public class SensorService {

    @Autowired
    private SensorRepository sensorRepository;

    @Autowired
    private MachineRepository machineRepository;

    public Sensor addSensorToMachine(Sensor sensor) {
        if (sensor.getMachine() == null || sensor.getMachine().getMachineId() == null) {
            throw new IllegalArgumentException("Machine ID must be provided.");
        }
    
        Machine machine = machineRepository.findById(sensor.getMachine().getMachineId())
                .orElseThrow(() -> new RuntimeException("Machine not found"));
    
        sensor.setMachine(machine);
        return sensorRepository.save(sensor);
    }
    
    // Get Machine's Sensors
    public List<String> getSensorsByMachineId(String machineId) {
        List<Sensor> sensors = sensorRepository.findSensorsByMachineId(machineId);
        List<String> sensorIds = new ArrayList<>();
        for (Sensor sensor : sensors) {
            sensorIds.add(sensor.getSensorId());
        }
        return sensorIds;
    }
}

