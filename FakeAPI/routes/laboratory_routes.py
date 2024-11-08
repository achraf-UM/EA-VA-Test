from flask import Blueprint, request, jsonify
from models.laboratory import Laboratory, db
from datetime import datetime

laboratory_bp = Blueprint('laboratory', __name__)

@laboratory_bp.route('/api/v1/laboratory', methods=['GET'])
def get_laboratories():
    # Query all laboratories from the database
    laboratories = Laboratory.query.all()

    # Convert the result to a list of dictionaries
    laboratories_list = []
    for lab in laboratories:
        laboratory_data = {
            'id': lab.id,
            'slug': lab.slug,
            'create_user_id': lab.create_user_id,
            'update_user_id': lab.update_user_id,
            'logo': lab.logo,
            'url': lab.url,
            'city': lab.city,
            'address': lab.address,
            'title': lab.title,
            'description': lab.description,
            'create_date': lab.create_date.isoformat(),  # Convert datetime to string
        }
        laboratories_list.append(laboratory_data)

    # Return the list of laboratories as a JSON response
    return jsonify(laboratories_list)

@laboratory_bp.route('/api/v1/laboratory/<int:id>', methods=['GET'])
def get_laboratory_by_id(id):
    try:
        # Fetch laboratory record by id
        laboratory = Laboratory.query.get(id)

        # If the laboratory is not found, return a 404 error
        if not laboratory:
            return jsonify({'error': 'Laboratory not found'}), 404

        # Return the laboratory data
        return jsonify({
            'id': laboratory.id,
            'slug': laboratory.slug,
            'create_user_id': laboratory.create_user_id,
            'update_user_id': laboratory.update_user_id,
            'logo': laboratory.logo,
            'url': laboratory.url,
            'city': laboratory.city,
            'address': laboratory.address,
            'address_bis': laboratory.address_bis,
            'phone': laboratory.phone,
            'email': laboratory.email,
            'zip_code': laboratory.zip_code,
            'title': laboratory.title,
            'description': laboratory.description,
            'keywords': laboratory.keywords,
            'sort': laboratory.sort,
            'revision': laboratory.revision,
            'create_date': laboratory.create_date,
            'update_date': laboratory.update_date,
            'is_valid': laboratory.is_valid,
            'conditional': laboratory.conditional,
            'ladp_server_id': laboratory.ladp_server_id,
            'dashboard_blocks': laboratory.dashboard_blocks,
            'mail_formation_ouverture': laboratory.mail_formation_ouverture,
            'mail_formation_relance': laboratory.mail_formation_relance,
            'afficher_module_informations': laboratory.afficher_module_informations,
            'afficher_formation_informations': laboratory.afficher_formation_informations
        }), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving laboratory.', 'details': str(e)}), 500
    
@laboratory_bp.route('/api/v1/laboratory', methods=['POST'])
def create_laboratory():
    try:
        # Get the JSON data from the request
        data = request.get_json()

        # Ensure 'slug' is provided
        if not data.get('slug'):
            return jsonify({'error': 'Slug is required'}), 400
        
        # Create a new laboratory record with the slug and default values for other fields
        new_laboratory = Laboratory(
            slug=data['slug'],
            create_user_id=data.get('create_user_id', None),  # Optional, defaults to None
            update_user_id=data.get('update_user_id', None),  # Optional, defaults to None
            logo=data.get('logo', None),  # Optional, defaults to None
            url=data.get('url', None),  # Optional, defaults to None
            city=data.get('city', None),  # Optional, defaults to None
            address=data.get('address', None),  # Optional, defaults to None
            address_bis=data.get('address_bis', None),  # Optional, defaults to None
            phone=data.get('phone', None),  # Optional, defaults to None
            email=data.get('email', None),  # Optional, defaults to None
            zip_code=data.get('zip_code', None),  # Optional, defaults to None
            title=data.get('title', None),  # Optional, defaults to None
            description=data.get('description', None),  # Optional, defaults to None
            keywords=data.get('keywords', None),  # Optional, defaults to None
            sort=data.get('sort', None),  # Optional, defaults to None
            revision=data.get('revision', 0),  # default revision to 0
            create_date=datetime.utcnow(),  # Current date as default
            update_date=datetime.utcnow(),  # Current date as default
            is_valid=data.get('is_valid', True),  # default is_valid to True
            conditional=data.get('conditional', None),  # Optional, defaults to None
            ladp_server_id=data.get('ladp_server_id', None),  # Optional, defaults to None
            dashboard_blocks=data.get('dashboard_blocks', None),  # Optional, defaults to None
            mail_formation_ouverture=data.get('mail_formation_ouverture', None),  # Optional, defaults to None
            mail_formation_relance=data.get('mail_formation_relance', None),  # Optional, defaults to None
            afficher_module_informations=data.get('afficher_module_informations', False),  # default False
            afficher_formation_informations=data.get('afficher_formation_informations', False)  # default False
        )

        # Add the new laboratory to the database
        db.session.add(new_laboratory)
        db.session.commit()

        # Return a success response with the newly created laboratory's id and slug
        return jsonify({
            'message': 'Laboratory created successfully',
            'id': new_laboratory.id,
            'slug': new_laboratory.slug
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while creating the laboratory', 'details': str(e)}), 500
