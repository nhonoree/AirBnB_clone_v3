from flask import jsonify, abort
from models import storage
from models.place import Place
from models.amenity import Amenity
from api.v1.views import app_views

@app_views.route("/places/<place_id>/amenities", methods=["GET"])
def get_place_amenities(place_id):
    """Retrieve all amenities of a place."""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    
    if storage.__class__.__name__ == "DBStorage":
        amenities = [amenity.to_dict() for amenity in place.amenities]
    else:  # FileStorage
        amenities = [storage.get(Amenity, amenity_id).to_dict() for amenity_id in place.amenity_ids]
    
    return jsonify(amenities)

@app_views.route("/places/<place_id>/amenities/<amenity_id>", methods=["DELETE"])
def delete_place_amenity(place_id, amenity_id):
    """Delete an amenity from a place."""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    
    if storage.__class__.__name__ == "DBStorage":
        if amenity not in place.amenities:
            abort(404)
        place.amenities.remove(amenity)
    else:  # FileStorage
        if amenity_id not in place.amenity_ids:
            abort(404)
        place.amenity_ids.remove(amenity_id)
    
    storage.save()
    return jsonify({}), 200

@app_views.route("/places/<place_id>/amenities/<amenity_id>", methods=["POST"])
def link_place_amenity(place_id, amenity_id):
    """Link an amenity to a place."""
    place = storage.get(Place, place_id)
    if not place:
        abort(404)
    
    amenity = storage.get(Amenity, amenity_id)
    if not amenity:
        abort(404)
    
    if storage.__class__.__name__ == "DBStorage":
        if amenity in place.amenities:
            return jsonify(amenity.to_dict()), 200
        place.amenities.append(amenity)
    else:  # FileStorage
        if amenity_id in place.amenity_ids:
            return jsonify(amenity.to_dict()), 200
        place.amenity_ids.append(amenity_id)
    
    storage.save()
    return jsonify(amenity.to_dict()), 201
