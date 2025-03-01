package com.precisionagri.precisionagri.Repository;

import org.springframework.stereotype.Repository;
import org.springframework.data.jpa.repository.JpaRepository;
import com.precisionagri.precisionagri.Models.Machine;



@Repository
public interface MachineRepository extends JpaRepository<Machine, String> {
}

    