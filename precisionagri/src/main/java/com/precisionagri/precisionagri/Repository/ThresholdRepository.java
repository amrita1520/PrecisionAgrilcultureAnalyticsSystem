package com.precisionagri.precisionagri.Repository;

import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;

import org.springframework.data.repository.query.Param;

import com.precisionagri.precisionagri.Models.Threshold;


import java.util.Optional;

@Repository
public interface ThresholdRepository extends JpaRepository<Threshold, Long> {

    @Query("SELECT t FROM Threshold t WHERE t.machine.machineId = :machineId")
    Optional<Threshold> findThresholdByMachineId(@Param("machineId") String machineId);
}

