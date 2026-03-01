from spatial import Parcel

def total_active_area(parcels: list) -> float:
    total = 0.0
    
    for parcel in parcels:                                  # Repetition
        if parcel.is_active:                                # Selection         
            total = total + parcel.area()                   # Modified structure

    return total

def parcels_above_threshold(parcels: list, threshold: float) -> list:
    result = []
    for parcel in parcels:
        if parcel.area() > threshold:                       # Modified structure 
            result.append(parcel)
        
    return result

def count_by_zone(parcels: list) -> dict:
    counts = {}
    for parcel in parcels:
        zone = parcel.zone
        if zone in counts:
            counts[zone] = counts[zone] + 1
        else:    
            counts[zone] = 1

    return counts

def intersecting_parcels(parcels: list, zone) -> list:
    result = []
    for parcel in parcels:
        if parcel.zone == zone:
            result.append(parcel)
        
    return result