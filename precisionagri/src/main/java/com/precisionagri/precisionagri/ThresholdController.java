package com.precisionagri.precisionagri;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import com.precisionagri.precisionagri.Models.Threshold;
import com.precisionagri.precisionagri.Service.ThresholdService;

import java.util.Optional;

@RestController
@RequestMapping("/thresholds")
public class ThresholdController {

    @Autowired
    private ThresholdService thresholdService;

    // Set Thresholds for a Machine
    @PostMapping("/create")
    public ResponseEntity<Threshold> setThreshold(@RequestBody Threshold threshold) {
        Threshold savedThreshold = thresholdService.setThreshold(threshold);
        return ResponseEntity.ok(savedThreshold);
    }

    // Get Thresholds for a Specific Machine
    @GetMapping("/{machineId}")
    public ResponseEntity<Threshold> getThresholdByMachine(@PathVariable String machineId) {
        Optional<Threshold> threshold = Optional.of(thresholdService.getThresholdByMachineId(machineId));
        return threshold.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
    }
}

