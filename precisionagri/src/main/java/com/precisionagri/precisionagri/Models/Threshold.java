package com.precisionagri.precisionagri.Models;


import jakarta.persistence.*;
import lombok.*;

import java.time.LocalDateTime;

@Entity
@Table(name = "thresholds")
@Getter
@Setter
@NoArgsConstructor
@AllArgsConstructor
@Builder
public class Threshold {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name = "threshold_id")
    private Long thresholdId;

    @ManyToOne
    @JoinColumn(name = "machine_id", nullable = false, referencedColumnName = "machine_id", foreignKey = @ForeignKey(name = "fk_threshold_machine"))
    private Machine machine;

    @Column(name = "temperature_max")
    private Float temperatureMax;

    @Column(name = "humidity_min")
    private Float humidityMin;

    @Column(name = "soil_moisture_min")
    private Float soilMoistureMin;

    @Column(name = "energy_usage_max")
    private Float energyUsageMax;

    @Column(name = "created_at", updatable = false)
    @Builder.Default
    private LocalDateTime createdAt = LocalDateTime.now();
}
