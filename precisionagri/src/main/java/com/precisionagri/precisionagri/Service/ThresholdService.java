package com.precisionagri.precisionagri.Service;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import com.precisionagri.precisionagri.Models.Threshold;
import com.precisionagri.precisionagri.Repository.ThresholdRepository;
import com.precisionagri.precisionagri.Models.Machine;
import com.precisionagri.precisionagri.Repository.MachineRepository;
import jakarta.persistence.EntityManager;
import jakarta.persistence.PersistenceContext;
import java.util.Optional;

@Service
public class ThresholdService {

    @Autowired
    private ThresholdRepository thresholdRepository;

    @Autowired
    private MachineRepository machineRepository;

    @PersistenceContext
    private EntityManager entityManager;

    // Set threshold for a machine
    public Threshold setThreshold(Threshold threshold) {
        if (threshold.getMachine().getMachineId() == null) {
            throw new IllegalArgumentException("Machine ID must be provided.");
        }

        // Check if the machine exists
        Optional<Machine> machine = machineRepository.findById(threshold.getMachine().getMachineId());
        if (machine.isEmpty()) {
            throw new RuntimeException("Machine not found");
        }

        return thresholdRepository.save(threshold);
    }

    // Get threshold by machine ID
    public Threshold getThresholdByMachineId(String machineId) {
        entityManager.clear();
        return thresholdRepository.findThresholdByMachineId(machineId)
                .orElseThrow(() -> new RuntimeException("Threshold not set for this machine"));
    }
}
