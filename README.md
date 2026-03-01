# Laboratory 4: Structured Programming + Object Systems Integration
---
## Description
Integration of structured programming (sequence, selection, and repetition) with object-oriented design to analyze spatial parcel data.

---
## Part C. Required Design (Design Phase)
---
### Algorithm:
1. Start
2. Load Parcel Data
3. Convert each record into a Parcel object 
4. If no parcels are loaded:
        - Display error message
        - Stop program
5. Initialize variables for analysis
6. Compute total area of active parcels
7. Identify parcels exceeding threshold area
8. Count number of parcels per zone
9. Identify parcels suitable for development based on zone
10. Print results
11. Save results to output/summary.json
12. End program

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

## Reflection — Laboratory 4

1. Where in your system do Sequence, Selection, and Repetition explicitly appear?
- Sequence appeared in the run_lab4.py, where the program followed the flow: loading data, creating Parcel objects, calling analysis functions, printing results, and saving the summary file.
- Selection also appeared in the run_lab4.py, in the conditional statements. It validated if the parcel list was empty. It also appeared in analysis.py where it filtered specific parcel attributes.
- Repetition appeared in analysis.py in the loops to iterate through the list of parcels to perform calculations like computing totals, filtering by threshold, and zone counting.
---
2. If you removed your algorithm planning step, how would your implementation likely change? 
- If I removed my algorithm planning step, my implementation would have been disorganized. There would have been redundant and unclear codes. Without the planning step, my implementation would have been messy and the codes would have mixed up and duplicated. I would have put some parts of the code in the wrong places and order. The responsibilities and boundaries would have been unclear and functions would have not worked. 
---
3. Where does spatial behavior live in your system, and why is that important?
- Spatial behavior lives within the object, or the SpatialObject class in my system. It is important because it made the system scalable and reusable. It encapsulates geometry-related behavior that belongs to spatial objects. It also made sure that the analysis functions did not directly manipulate geometry. 
---
4. Why does analysis.py contain structured logic instead of demo.py? 
- Analysis.py contained structured logic instead of demo.py because it is the one responsible for coordinating all the operations, such as filtering, counting, and aggregating results. It made sure that the logic remained clean and reusable, because if structured logic was put in demo.py, it would become cluttered with loops and conditionals.
---
5. What would happen if all filtering logic were placed inside the Parcel class? 
- If all filtering logic were placed inside the Parcel class, the parcel class would become very complex and overloaded with responsibilities. It would become a God Class and violate the Single Responsibility Principle.
---
6. If a new rule is added (e.g., “exclude inactive industrial parcels”), how easily can your current design adapt? 
- If a new rule is added, the current design would easily adapt, because the structured logic is separated from object behavior. The new rule would simply need a new function or modify an existing function, and not need to rewrite the parcel class.
---
7. How does separating structured logic from object behavior prevent “God classes”? 
- Separating structured logic from object behavior prevents God classes by ensuring that objects are only responsible and store their own state and spatial behavior. This avoids the accumulation of unrelated responsibilities inside one class, and no single class becomes responsible for every task in the system.
---
### Author
- Audrey Marie Justine A. Reyes
- MS Geomatics Engineering (GeoInf)