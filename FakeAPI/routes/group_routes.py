from flask import Blueprint, request, jsonify
from database import db  # Import db from the database file
from models.group import Group

# Create a blueprint for your group routes
group_bp = Blueprint('group_bp', __name__)

@group_bp.route('/api/v1/group', methods=['POST'])
def create_group():
    try:
        # Get data from the request body
        data = request.get_json()

        name = data.get('name')
        roles = data.get('roles')
        description = data.get('description', None)
        is_valid = data.get('is_valid', True)

        if not name or not roles:
            return jsonify({'error': 'Name and roles are required.'}), 400
        
        # Create the new group
        new_group = Group(
            name=name,
            roles=roles,  # roles will be a list due to JSON
            description=description,
            is_valid=is_valid
        )

        # Add and commit to the database
        db.session.add(new_group)
        db.session.commit()

        return jsonify({
            'message': 'group created successfully',
            'group': {
                'id': new_group.id,
                'name': new_group.name,
                'roles': new_group.roles,
                'description': new_group.description,
                'is_valid': new_group.is_valid
            }
        }), 201

    except Exception as e:
        db.session.rollback()  # Ensure rollback in case of an error
        return jsonify({'error': 'An error occurred while creating the group.', 'details': str(e)}), 500
    

@group_bp.route('/api/v1/group/<int:id>', methods=['GET'])
def get_group(id):
    try:
        # Query the group by ID
        group = Group.query.get(id)
        
        if group is None:
            return jsonify({'error': 'group not found.'}), 404
        
        return jsonify({
            'id': group.id,
            'name': group.name,
            'roles': group.roles,
            'description': group.description,
            'is_valid': group.is_valid
        }), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching the group.', 'details': str(e)}), 500
