from flask import Blueprint, request, jsonify
from models import db
from models.appearance import Appearance
from models.guest import Guest
from models.episode import Episode
from flask_jwt_extended import jwt_required

appearance_bp = Blueprint('appearance_bp', __name__, url_prefix='/appearances')

@appearance_bp.route('/', methods=['GET'])
def get_appearances():
    appearances = Appearance.query.all()
    return jsonify([appearance.to_dict() for appearance in appearances]), 200

@appearance_bp.route('/', methods=['POST'])
@jwt_required()
def create_appearance():
    data = request.get_json()
    guest = Guest.query.get(data['guest_id'])
    episode = Episode.query.get(data['episode_id'])

    if not guest or not episode:
        return jsonify({'error': 'Guest or Episode not found'}), 404

    new_appearance = Appearance(guest_id=guest.id, episode_id=episode.id, rating=data['rating'])
    db.session.add(new_appearance)
    db.session.commit()
    return jsonify(new_appearance.to_dict()), 201

@appearance_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_appearance(id):
    appearance = Appearance.query.get_or_404(id)
    db.session.delete(appearance)
    db.session.commit()
    return jsonify({'message': 'Appearance deleted'}), 200
