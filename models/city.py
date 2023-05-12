#!/usr/bin/python3
"""Instantiate the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """Reps a city.

    Attributes:
        state_id (string): State id.
        name (string): Name of the city.
    """

    state_id = ""
    name = ""