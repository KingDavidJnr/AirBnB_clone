#!/usr/bin/python3
"""Instatantiates the State class."""
from models.base_model import BaseModel


class State(BaseModel):
    """Reps the state.

    Attributes:
        name (string): Name of the state.
    """

    name = ""