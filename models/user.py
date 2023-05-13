#!/usr/bin/python3
"""Expresses the User class."""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents the User.

    Attributes:
        email (string): Email of the user.
        password (string): Password of the user.
        first_name (string): First name of the user.
        last_name (string): Last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
