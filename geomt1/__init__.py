"""Top-level package for GeoMT1."""

__author__ = """Alex McCorkel"""
__email__ = "amccorketutoring@gmail.com"
__version__ = "0.0.1"


from .leaflet_map import LeafletMap
from .folium_map import FoliumMap

__all__ = [
    "LeafletMap",
    "FoliumMap",
]