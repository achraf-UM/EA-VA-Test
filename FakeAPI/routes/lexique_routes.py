from flask import Blueprint, request, jsonify
from models.lexique import Lexique
from database import db
from datetime import datetime
import uuid as uuid_lib

lexique_bp = Blueprint('lexique', __name__)

@lexique_bp.route('/api/v1/lexique', methods=['GET'])
def get_lexiques():
    try:
        lexiques = Lexique.query.all()
        return jsonify([{
            'id': lexique.id,
            'title': lexique.title,
            'description': lexique.description,
            'revision': lexique.revision,
            'create_date': lexique.create_date,
            'update_date': lexique.update_date,
            'is_valid': lexique.is_valid,
            'uuid': lexique.uuid
        } for lexique in lexiques]), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving lexiques.', 'details': str(e)}), 500

# Endpoint to get a lexique by id
@lexique_bp.route('/api/v1/lexique/<int:id>', methods=['GET'])
def get_lexique_by_id(id):
    try:
        lexique = Lexique.query.get(id)
        if not lexique:
            return jsonify({'error': 'Lexique not found.'}), 404
        
        return jsonify({
            'id': lexique.id,
            'title': lexique.title,
            'description': lexique.description,
            'revision': lexique.revision,
            'create_date': lexique.create_date,
            'update_date': lexique.update_date,
            'is_valid': lexique.is_valid,
            'uuid': lexique.uuid
        }), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving the lexique.', 'details': str(e)}), 500

@lexique_bp.route('/api/v1/lexique', methods=['POST'])
def add_lexiques():
    data = request.get_json()
    
    # If the input data is a list, add multiple lexiques
    if isinstance(data, list):
        lexiques = []
        for item in data:
            lexique = Lexique(
                title=item.get('title').encode('utf-8').decode('utf-8'),
                description=item.get('description').encode('utf-8').decode('utf-8'),
                revision=2,
                create_date=datetime.now(),
                update_date=datetime.now(),
                is_valid=item.get('is_valid', True),
                uuid=str(uuid_lib.uuid4())  # Generates a unique UUID for each lexique
            )
            db.session.add(lexique)
            lexiques.append({
                'id': lexique.id,
                'title': lexique.title,
                'description': lexique.description,
                'revision': lexique.revision,
                'create_date': lexique.create_date,
                'update_date': lexique.update_date,
                'is_valid': lexique.is_valid,
                'uuid': lexique.uuid
            })
        db.session.commit()
        return jsonify(lexiques), 201
    
    # If the input data is a single lexique, add it directly
    else:
        lexique = Lexique(
            title=data.get('title').encode('utf-8').decode('utf-8'),
            description=data.get('description').encode('utf-8').decode('utf-8'),
            revision=2,
            create_date=datetime.now(),
            update_date=datetime.now(),
            is_valid=data.get('is_valid', True),
            uuid=str(uuid_lib.uuid4())  # Generates a unique UUID
        )
        db.session.add(lexique)
        db.session.commit()
        
        return jsonify({
            'id': lexique.id,
            'title': lexique.title,
            'description': lexique.description,
            'revision': lexique.revision,
            'create_date': lexique.create_date,
            'update_date': lexique.update_date,
            'is_valid': lexique.is_valid,
            'uuid': lexique.uuid
        }), 201

        # Endpoint to delete a lexique by ID
@lexique_bp.route('/api/v1/lexique/<int:id>', methods=['DELETE'])
def delete_lexique(id):
    try:
        lexique = Lexique.query.get_or_404(id)
        db.session.delete(lexique)
        db.session.commit()
        return jsonify({'message': 'Lexique deleted successfully.'}), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while deleting the lexique.', 'details': str(e)}), 500

# Endpoint to update a lexique by ID
@lexique_bp.route('/api/v1/lexique/<int:id>', methods=['PUT'])
def update_lexique(id):
    data = request.get_json()
    
    try:
        lexique = Lexique.query.get(id)
        if not lexique:
            return jsonify({'error': 'Lexique not found.'}), 404
        
        # Update the title and description
        lexique.title = data.get('title', lexique.title)
        lexique.description = data.get('description', lexique.description)
        
        # Set update_date to the current time
        lexique.update_date = datetime.now()
        
        db.session.commit()
        return jsonify({
            'id': lexique.id,
            'title': lexique.title,
            'description': lexique.description,
            'revision': lexique.revision,
            'create_date': lexique.create_date,
            'update_date': lexique.update_date,
            'is_valid': lexique.is_valid,
            'uuid': lexique.uuid
        }), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while updating the lexique.', 'details': str(e)}), 500