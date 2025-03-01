package com.precisionagri.precisionagri.Models;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDateTime;

@Entity
@Table(name = "machines") // Ensure this matches your PostgreSQL table
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Machine {

    @Id
    @Column(name = "machine_id", length = 50)
    private String machineId;  // String since it's VARCHAR(50)

    @Column(name = "user_id", length = 50)
    private String userId; // Foreign key referencing "users"

    @Column(name = "location", length = 255)
    private String location;

    @Column(name = "type", length = 100)
    private String type;

    @Column(name = "created_at", updatable = false)
    private LocalDateTime createdAt;
}
