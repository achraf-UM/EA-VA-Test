from flask import Blueprint, request, jsonify
from models.civility import Civility
from database import db

civility_bp = Blueprint('civility', __name__)

@civility_bp.route('/api/v1/civility', methods=['POST'])
def create_civility():
    try:
        data = request.get_json()
        
        # Creating a new Civility record from the data
        civility = Civility(
            create_user_id=data['create_user_id'],
            update_user_id=data['update_user_id'],
            title=data['title'],
            description=data.get('description'),
            keywords=data.get('keywords'),
            sort=data['sort'],
            revision=data['revision'],
            conditional=data.get('conditional')
        )
        
        # Add the civility object to the session and commit
        db.session.add(civility)
        db.session.commit()
        
        return jsonify({'message': 'Civility created successfully'}), 201
    except Exception as e:
        return jsonify({'error': 'An error occurred while creating the civility.', 'details': str(e)}), 500
    
@civility_bp.route('/api/v1/civility', methods=['GET'])
def get_civilities():
    try:
        # Fetch all civility records
        civilities = Civility.query.all()

        # Create a response with civility data
        result = [{
            'id': civility.id,
            'create_user_id': civility.create_user_id,
            'update_user_id': civility.update_user_id,
            'title': civility.title,
            'description': civility.description,
            'keywords': civility.keywords,
            'sort': civility.sort,
            'revision': civility.revision,
            'create_date': civility.create_date,
            'update_date': civility.update_date,
            'is_valid': civility.is_valid,
            'conditional': civility.conditional
        } for civility in civilities]

        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving civilities.', 'details': str(e)}), 500
    

@civility_bp.route('/api/v1/civility/<int:id>', methods=['GET'])
def get_civility_by_id(id):
    try:
        # Fetch civility record by id
        civility = Civility.query.get(id)

        # If civility is not found, return a 404 error
        if not civility:
            return jsonify({'error': 'Civility not found'}), 404

        # Return the civility data
        return jsonify({
            'id': civility.id,
            'create_user_id': civility.create_user_id,
            'update_user_id': civility.update_user_id,
            'title': civility.title,
            'description': civility.description,
            'keywords': civility.keywords,
            'sort': civility.sort,
            'revision': civility.revision,
            'create_date': civility.create_date,
            'update_date': civility.update_date,
            'is_valid': civility.is_valid,
            'conditional': civility.conditional
        }), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving civility.', 'details': str(e)}), 500

