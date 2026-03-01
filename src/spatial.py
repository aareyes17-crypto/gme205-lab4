from shapely.geometry import shape as ShapelyShape
from shapely.ops import transform
from pyproj import Transformer


class SpatialObject:
    # Consulted chatGPT for UTM zone calculation and caching logic
    _transformer_cache = {}

    def __init__(self, geometry_data):
        self.geometry = ShapelyShape(geometry_data)

    def _get_utm_transformer(self):

        lon = self.geometry.centroid.x
        lat = self.geometry.centroid.y

        utm_zone = int((lon + 180) / 6) + 1

        if lat >= 0:
            epsg_code = 32600 + utm_zone
        else:
            epsg_code = 32700 + utm_zone

        if epsg_code not in self._transformer_cache:
            self._transformer_cache[epsg_code] = Transformer.from_crs(
                "EPSG:4326",
                f"EPSG:{epsg_code}",
                always_xy=True
            )

        return self._transformer_cache[epsg_code]

    def area(self):
        """
        Returns area in square meters.
        """

        transformer = self._get_utm_transformer()
        projected_geom = transform(transformer.transform, self.geometry)
        return projected_geom.area

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
            f"Parcel(p_id={self.p_id}, "
            f"zone='{self.zone}', "
            f"is_active={self.is_active}, "
            f"area={self.area():.2f} sqm)"
        )