package com.precisionagri.precisionagri.Service;
import java.util.ArrayList;
import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import com.precisionagri.precisionagri.Models.Machine;
import com.precisionagri.precisionagri.Repository.MachineRepository;

@Service
public class MachineService {

    @Autowired
    private MachineRepository machineRepository;

    public Machine saveMachine(Machine machine) {
        return machineRepository.save(machine);
    }

    public List<Machine> getAllMachinesInPlace(String place) {
        List<Machine> machines = machineRepository.findAll();
        List<Machine> machinesInBangalore = new ArrayList<>();
        for (Machine machine : machines) {
            if (machine.getLocation().contains(place))
               { machinesInBangalore.add(machine);
               }
        
        }
        return machinesInBangalore;
    } 
    //find all machine for a muser
    public List<Machine> getMachinesByUser(String userId) {
        return machineRepository.getMachinesByUser(userId);
    }
        

}