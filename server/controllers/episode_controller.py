from flask import Blueprint, request, jsonify
from models import db
from models.episode import Episode
from flask_jwt_extended import jwt_required

episode_bp = Blueprint('episode_bp', __name__, url_prefix='/episodes')

@episode_bp.route('/', methods=['GET'])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([episode.to_dict() for episode in episodes]), 200

@episode_bp.route('/<int:id>', methods=['GET'])
def get_episode(id):
    episode = Episode.query.get_or_404(id)
    return jsonify(episode.to_dict()), 200

@episode_bp.route('/', methods=['POST'])
@jwt_required()
def create_episode():
    data = request.get_json()
    new_episode = Episode(date=data['date'], number=data['number'])
    db.session.add(new_episode)
    db.session.commit()
    return jsonify(new_episode.to_dict()), 201

@episode_bp.route('/<int:id>', methods=['PATCH'])
@jwt_required()
def update_episode(id):
    episode = Episode.query.get_or_404(id)
    data = request.get_json()
    episode.date = data.get('date', episode.date)
    episode.number = data.get('number', episode.number)
    db.session.commit()
    return jsonify(episode.to_dict()), 200

@episode_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_episode(id):
    episode = Episode.query.get_or_404(id)
    db.session.delete(episode)
    db.session.commit()
    return jsonify({'message': 'Episode deleted'}), 200
