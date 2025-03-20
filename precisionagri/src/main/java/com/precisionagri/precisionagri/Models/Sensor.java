package com.precisionagri.precisionagri.Models;

import jakarta.persistence.*;
import lombok.*;
import java.time.LocalDate;
import java.time.LocalDateTime;

@Entity
@Table(name = "sensors") // Ensure this matches your PostgreSQL table
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
public class Sensor {

    @Id
    @Column(name = "sensor_id", length = 50)
    private String sensorId;  // String since it's VARCHAR(50)

    @ManyToOne
    @JoinColumn(name = "machine_id", nullable = false, referencedColumnName = "machine_id")
    private Machine machine; // Foreign key referencing "machines"

    @Column(name = "sensor_type", length = 100, nullable = false)
    private String sensorType;

    @Column(name = "installation_date")
    private LocalDate installationDate;

    @Column(name = "created_at", updatable = false)
private LocalDateTime createdAt;

    @PrePersist
    protected void onCreate() {
        this.createdAt = LocalDateTime.now();
    }

}
