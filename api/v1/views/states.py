from flask import jsonify, request, abort
from models import storage
from models.state import State
from api.v1.views import app_views

@app_views.route("/states", methods=["GET"])
def get_states():
        """Retrieve all states."""
            states = storage.all(State).values()
                return jsonify([state.to_dict() for state in states])

            @app_views.route("/states/<state_id>", methods=["GET"])
            def get_state(state_id):
                    """Retrieve a specific state."""
                        state = storage.get(State, state_id)
                            if not state:
                                        abort(404)
                                            return jsonify(state.to_dict())

                                        @app_views.route("/states/<state_id>", methods=["DELETE"])
                                        def delete_state(state_id):
                                                """Delete a state."""
                                                    state = storage.get(State, state_id)
                                                        if not state:
                                                                    abort(404)
                                                                        storage.delete(state)
                                                                            storage.save()
                                                                                return jsonify({}), 200

                                                                            @app_views.route("/states", methods=["POST"])
                                                                            def create_state():
                                                                                    """Create a new state."""
                                                                                        data = request.get_json()
                                                                                            if not data:
                                                                                                        abort(400, description="Not a JSON")
                                                                                                            if "name" not in data:
                                                                                                                        abort(400, description="Missing name")
                                                                                                                            state = State(**data)
                                                                                                                                state.save()
                                                                                                                                    return jsonify(state.to_dict()), 201

                                                                                                                                @app_views.route("/states/<state_id>", methods=["PUT"])
                                                                                                                                def update_state(state_id):
                                                                                                                                        """Update a state."""
                                                                                                                                            state = storage.get(State, state_id)
                                                                                                                                                if not state:
                                                                                                                                                            abort(404)
                                                                                                                                                                data = request.get_json()
                                                                                                                                                                    if not data:
                                                                                                                                                                                abort(400, description="Not a JSON")
                                                                                                                                                                                    for key, value in data.items():
                                                                                                                                                                                                if key not in ["id", "created_at", "updated_at"]:
                                                                                                                                                                                                                setattr(state, key, value)
                                                                                                                                                                                                                    state.save()
                                                                                                                                                                                                                        return jsonify(state.to_dict()), 200
