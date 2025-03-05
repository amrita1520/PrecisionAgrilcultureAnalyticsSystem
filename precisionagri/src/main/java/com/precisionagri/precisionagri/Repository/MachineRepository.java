package com.precisionagri.precisionagri.Repository;

import org.springframework.stereotype.Repository;

import java.util.List;

import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import com.precisionagri.precisionagri.Models.Machine;



@Repository
public interface MachineRepository extends JpaRepository<Machine, String> {
    @Query("SELECT m FROM Machine m WHERE m.userId = :userId")
    List<Machine> getMachinesByUser(@Param("userId") String userId);
}

    