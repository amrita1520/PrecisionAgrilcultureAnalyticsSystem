package com.precisionagri.precisionagri.Repository;

import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.jpa.repository.QueryHints;
import org.springframework.data.repository.query.Param;

import com.precisionagri.precisionagri.Models.Sensor;

import jakarta.persistence.QueryHint;

import java.util.List;

@Repository
public interface SensorRepository extends JpaRepository<Sensor, String> {
    
    @Query("SELECT s FROM Sensor s WHERE s.machine.machineId = :machineId")
    List<Sensor> findSensorsByMachineId(@Param("machineId") String machineId);

}

