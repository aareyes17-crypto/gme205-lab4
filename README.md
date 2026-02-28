# Laboratory 4: Structured Programming + Object Systems Integration
---
## Description
Integration of structured programming (sequence, selection, and repetition) with object-oriented design to analyze spatial parcel data.

---
## Part C. Required Design (Design Phase)
---
### Algorithm:
i. Start
ii. Load Parcel Data
iii. Convert each record into a Parcel object 
iv. If no parcels are loaded:
        - Display error message
        - Stop program
v. Initialize variables for analysis
vi. Compute total area of active parcels
vii. Identify parcels exceeding threshold area
vii. Count number of parcels per zone
ix. Identify parcels suitable for development based on zone
x. Print results
xi. Save results to output/summary.json
xii. End program

---
### Pseudocode:
```
BEGIN 
        LOAD parcel_data from JSON file

        CONVERT parcel_data into Parcel objects
        STORE in parcel_list

        IF parcel_list is empty THEN
        PRINT "No parcels found."
        STOP
        END IF

        SET total_active_area = 0
        SET threshold_value = 8000
        SET development_zone = "Residential"

        CREATE empty list parcels_above_threshold
        CREATE empty dictionary zone_count
        CREATE empty list development_candidates

        FOR each parcel IN parcel_list DO
                IF parcel is active THEN
                total_active_area = total_active_area + parcel.area()
                END IF

                IF parcel.area() > threshold_value THEN
                ADD parcel TO above_threshold
                END IF

                IF parcel.zone NOT IN zone_count THEN
                zone_count[parcel.zone] = 1
                ELSE
                zone_count[parcel.zone] = zone_count[parcel.zone] + 1
                END IF

                IF parcel.zone == development_zone AND parcel is active THEN
                ADD parcel TO development_candidates
                END IF
        END FOR

        PRINT total_active_area
        PRINT above_threshold
        PRINT zone_count
        PRINT development_candidates

        SAVE results to output/summary.json
END
```
    