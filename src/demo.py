from spatial import Point, Parcel
from analysis import total_active_area, parcels_above_threshold, count_by_zone, intersecting_parcels

# p1 = Point(121.0437, 14.6760)
# p2 = Point(121.0512, 14.6835)

# print(p1,p2)

parcel_1 = Parcel(
    p_id=1,
    zone='Residential',
    is_active=True,
    geometry_data={'type': 'Polygon', 'coordinates': [[
            (121.0418, 14.6749),
            (121.0443, 14.6749),
            (121.0443, 14.6773),
            (121.0418, 14.6773),
            (121.0418, 14.6749)
        ]]
    }
)

parcel_2 = Parcel(    
    p_id=2,
    zone='Commercial',
    is_active=False,
    geometry_data={'type': 'Polygon', 'coordinates': [[
            (121.0498, 14.6821),
            (121.0526, 14.6821),
            (121.0526, 14.6850),
            (121.0498, 14.6850),
            (121.0498, 14.6821)
        ]]
    }
)

# print(parcel_1)
# print(parcel_2)

# print("Do parcels intersect?", parcel_1.intersects(parcel_2))

parcels = [parcel_1, parcel_2] 
print("Total active:", total_active_area(parcels))

'''
for parcels above threshold
'''
total_threshold = 1                                                
above_threshold = parcels_above_threshold(parcels, total_threshold)
print (f"Parcels with area > {total_threshold}:")
for par in above_threshold:
    print(par)

'''
parcel counts by zone
'''
counts_zone = count_by_zone(parcels)
print("Parcel counts by zone:")
for zone, count in counts_zone.items():
    print(f"{zone}: {count}")

'''
Intersecting parcels
'''
parcel_residential = intersecting_parcels(parcels, "Residential")
print("Residential parcels:")
for residential in parcel_residential:
    print(residential)