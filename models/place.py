#!/usr/bin/python3
"""Instantiates the Place class."""
from models.base_model import BaseModel


class Place(BaseModel):
    """Reps a place.

    Attributes:
        city_id (string): City id.
        user_id (string): User id.
        name (string): Name of the place.
        description (string): Description of the place.
        number_rooms (integer): Number of rooms of the place.
        number_bathrooms (integer): Number of bathrooms of the place.
        max_guest (integer): Maximum number of guests of the place.
        price_by_night (integer): Price by night of the place.
        latitude (float): Latitude of the place.
        longitude (float): Longitude of the place.
        amenity_ids (list): The list of Amenity ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []