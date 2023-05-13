#!/usr/bin/python3
"""Constitutes the Amenity class."""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Describes an amenity.

    Attributes:
        name (string): Name of the amenity.
    """

    name = ""
