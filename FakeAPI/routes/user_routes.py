from flask import Blueprint, request, jsonify, current_app
from models.user import User
from database import db
from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.utils import secure_filename
import os
# Define the directory where uploaded images will be stored
UPLOAD_FOLDER = 'uploads/'  # Adjust this path as needed
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

user_bp = Blueprint('user', __name__)

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@user_bp.route('/api/v1/user/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    try:
        # Fetch the user by ID
        user = User.query.get(user_id)

        if not user:
            return jsonify({'error': 'User not found'}), 404

        # Get the updated data from the request body
        data = request.form  # Use `request.form` for text fields
        file = request.files.get('photo')  # Use `request.files` for file data
        
        # Update text fields if provided
        group_id = data.get('group_id')
        division_id = data.get('division_id')
        if group_id:
            user.group_id = group_id
        if division_id:
            user.division_id = division_id

        # Process and save the uploaded file if it exists and is allowed
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            user.photo = filepath  # Save the path to the `photo` field in the database

        # Update the `update_date` field
        user.update_date = datetime.utcnow()

        # Commit the changes to the database
        db.session.commit()

        return jsonify({
            'message': 'User updated successfully',
            'user': {
                'id': user.id,
                'username': user.username,
                'group_id': user.group_id,
                'division_id': user.division_id,
                'photo': user.photo  # Return the photo path
            }
        }), 200

    except Exception as e:
        db.session.rollback()  # Ensure rollback in case of an error
        return jsonify({'error': 'An error occurred while updating the user.', 'details': str(e)}), 500
@user_bp.route('/api/v1/user', methods=['POST'])
def create_user():
    try:
        data = request.form

        image_file = request.files.get('photo')
        
        # Get data from the request body
        civility_id = data.get('civility_id')
        firstname = data.get('firstname')
        lastname = data.get('lastname')
        username = data.get('username')
        email = data.get('email')
        laboratory_id = data.get('laboratory_id')
        password = data.get('password')  # Get password from request body
        division_id = data.get('division_id')
        group_id = data.get('group_id')
        
        
        if not password:
            return jsonify({'error': 'Password is required.'}), 400
        
        # Hash the password
        hashed_password = generate_password_hash(password)

        photo_path = None
        if image_file:
            filename = secure_filename(image_file.filename)
            upload_dir = os.path.join(current_app.config['UPLOAD_FOLDER'], 'user_images')
            os.makedirs(upload_dir, exist_ok=True)
            photo_path = os.path.join(upload_dir, filename)
            image_file.save(photo_path)
        
        # Set username_canonical and email_canonical
        username_canonical = username.lower() if username else None
        email_canonical = email.lower() if email else None
        
        # Create the user
        new_user = User(
            civility_id=civility_id,
            firstname=firstname,
            lastname=lastname,
            username=username,
            username_canonical=username_canonical,
            email=email,
            email_canonical=email_canonical,
            laboratory_id=laboratory_id,
            password=hashed_password,  # Store hashed password
            roles='0',  # Default roles to 0
            photo=photo_path,
            create_date=datetime.utcnow(),
            update_date=datetime.utcnow(),
            is_valid=True,  # Assuming the user is valid by default
            revision=1,  # Assuming version 1
            group_id=1,
            division_id=1,
        )
        
        # Add and commit to the database
        db.session.add(new_user)
        db.session.commit()
        
        return jsonify({
            'message': 'User created successfully',
            'user': {
                'id': new_user.id,
                'username': new_user.username,
                'email': new_user.email,
                'photo': new_user.photo,
                'group_id' : new_user.group_id,
                'division_id' : new_user.division_id
            }
        }), 201
        
    except Exception as e:
        db.session.rollback()  # Ensure rollback in case of an error
        return jsonify({'error': 'An error occurred while creating the user.', 'details': str(e)}), 500


@user_bp.route('/api/v1/user/<int:user_id>', methods=['GET'])
def get_user(user_id):
    try:
        # Fetch user by ID
        user = User.query.get(user_id)
        
        if user:
            # Return user data as JSON
            return jsonify({
                'id': user.id,
                'civility_id': user.civility_id,
                'firstname': user.firstname,
                'lastname': user.lastname,
                'username': user.username,
                'email': user.email,
                'laboratory_id': user.laboratory_id,
                'create_date': user.create_date,
                'update_date': user.update_date,
                'roles': user.roles,
                'division_id' : user.division_id,
                'group_id' : user.division_id,
                'photo': user.photo
            }), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving the user.', 'details': str(e)}), 500

# @user_bp.route('/api/v1/user/<int:user_id>', methods=['PUT'])
# def update_user(user_id):
#     try:
#         # Fetch the user by ID
#         user = User.query.get(user_id)

#         if not user:
#             return jsonify({'error': 'User not found'}), 404
        
#         # Get the updated data from the request body
#         data = request.get_json()
#         group_id = data.get('group_id')
#         division_id = data.get('division_id')

#         # Update only if values are provided
#         if group_id:
#             user.group_id = group_id
#         if division_id:
#             user.division_id = division_id

#         # Update the update_date field
#         user.update_date = datetime.utcnow()

#         # Commit the changes to the database
#         db.session.commit()

#         return jsonify({
#             'message': 'User updated successfully',
#             'user': {
#                 'id': user.id,
#                 'username': user.username,
#                 'group_id': user.group_id,
#                 'division_id': user.division_id
#             }
#         }), 200

#     except Exception as e:
#         db.session.rollback()  # Ensure rollback in case of an error
#         return jsonify({'error': 'An error occurred while updating the user.', 'details': str(e)}), 500


