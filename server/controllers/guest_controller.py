from flask import Blueprint, request, jsonify
from models import db
from models.guest import Guest
from flask_jwt_extended import jwt_required

guest_bp = Blueprint('guest_bp', __name__, url_prefix='/guests')

@guest_bp.route('/', methods=['GET'])
def get_all_guests():
    guests = Guest.query.all()
    return jsonify([guest.to_dict() for guest in guests]), 200

@guest_bp.route('/<int:id>', methods=['GET'])
def get_guest(id):
    guest = Guest.query.get_or_404(id)
    return jsonify(guest.to_dict()), 200

@guest_bp.route('/', methods=['POST'])
@jwt_required()
def create_guest():
    data = request.get_json()
    new_guest = Guest(name=data['name'], occupation=data['occupation'])
    db.session.add(new_guest)
    db.session.commit()
    return jsonify(new_guest.to_dict()), 201

@guest_bp.route('/<int:id>', methods=['PATCH'])
@jwt_required()
def update_guest(id):
    guest = Guest.query.get_or_404(id)
    data = request.get_json()
    guest.name = data.get('name', guest.name)
    guest.occupation = data.get('occupation', guest.occupation)
    db.session.commit()
    return jsonify(guest.to_dict()), 200

@guest_bp.route('/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_guest(id):
    guest = Guest.query.get_or_404(id)
    db.session.delete(guest)
    db.session.commit()
    return jsonify({'message': 'Guest deleted'}), 200
