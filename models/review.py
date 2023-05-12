#!/usr/bin/python3
"""Instatiates the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """Reps a review.

    Attributes:
        place_id (string): Place id.
        user_id (string): User id.
        text (string): Text of the review.
    """

    place_id = ""
    user_id = ""
    text = ""