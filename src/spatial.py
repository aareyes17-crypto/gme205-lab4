from shapely.geometry import shape as ShapelyShape


class SpatialObject:
    def __init__(self, geometry_data):
        self.geometry = ShapelyShape(geometry_data)
    
    
    def intersects(self, other):
        return self.geometry.intersects(other.geometry)

class Point(SpatialObject):
    def __init__(self, x, y):
        if not (-180 <= x <= 180):
            raise ValueError("Longitude must be between -180 and 180")
        if not (-90 <= y <= 90):
            raise ValueError("Latitude must be between -90 and 90")
       
        super().__init__({'type': 'Point', 'coordinates': (x, y)})
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Point(x={self.x}, y={self.y})"

class Parcel(SpatialObject):
    VALID_ZONES = {'Residential', 'Commercial', 'Industrial'}

    def __init__(self, p_id, zone, is_active, geometry_data):
        if zone not in self.VALID_ZONES:
            raise ValueError(f"Zone must be one of {self.VALID_ZONES}")
        super().__init__(geometry_data)
        self.p_id = p_id
        self.zone = zone
        self.is_active = is_active

    def __repr__(self):
        return (
            f"Parcel(p_id={self.p_id}, zone='{self.zone}', is_active={self.is_active})"
        )