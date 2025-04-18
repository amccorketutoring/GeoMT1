
from ipyleaflet import Map, LayersControl, TileLayer, GeoJSON
import geopandas as gpd

class LeafletMap(Map):
    def add_basemap(self, name="OpenStreetMap"):
        tile = TileLayer(url=f'https://{name.lower()}.org/{{z}}/{{x}}/{{y}}.png')
        self.add_layer(tile)

    def add_layer_control(self):
        self.add_control(LayersControl(position='topright'))

    def add_vector(self, vector_path):
        gdf = gpd.read_file(vector_path)
        geo_json = GeoJSON(data=gdf.__geo_interface__)
        self.add_layer(geo_json)
