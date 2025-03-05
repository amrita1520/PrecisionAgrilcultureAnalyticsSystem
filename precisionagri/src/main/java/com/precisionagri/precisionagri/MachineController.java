package com.precisionagri.precisionagri;

import java.util.List;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.precisionagri.precisionagri.Models.Machine;
import com.precisionagri.precisionagri.Service.MachineService;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.RequestParam;


@RestController
@RequestMapping("/machines")
public class MachineController {

    @Autowired
    private MachineService machineService;

    @PostMapping("/create")
    public Machine createMachine(@RequestBody Machine machine) {
        return machineService.saveMachine(machine);
    }

    @GetMapping("/details")
    public List<Machine> allMachinesinPlace(@RequestParam String place) {
    return machineService.getAllMachinesInPlace(place);
    }

    @GetMapping("/user")
    public List<Machine> getMachinesByUser(@RequestParam String userId) {
        return machineService.getMachinesByUser(userId);
    }
    
}