#!/usr/bin/python3
"""
Review view for API.

"""

from flask import abort, request, jsonify

from api.v1.views import app_views
from models import storage
from models.review import Review


@app_views.route(
    '/places/<place_id>/reviews',
    methods=['GET'],
    strict_slashes=False)
def get_review_by_place(place_id):
    """Returns JSON reviews of given place"""
    place = storage.get('Place', place_id)
    if place:
        reviews = []
        for review in place.reviews:
            reviews.append(review.to_dict())
        return (jsonify(reviews), 200)
    abort(404)


@app_views.route(
    '/reviews/<review_id>',
    methods=['GET'],
    strict_slashes=False)
def get_review(review_id):
    """Returns JSON review with a given id"""
    review = storage.get('Review', review_id)
    if review:
        return (jsonify(review.to_dict()), 200)
    abort(404)


