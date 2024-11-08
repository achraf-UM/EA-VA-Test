from flask import Flask, request, jsonify, Blueprint
from database import db
from models.division import Division  # Import your Division model

division_bp = Blueprint('division_bp', __name__)

@division_bp.route('/api/v1/division', methods=['POST'])
def create_division():
    # Get the data from the request body
    data = request.get_json()

    # Extract the slug and title from the request body
    slug = data.get('slug')
    title = data.get('title')

    # Check if both fields are provided
    if not slug or not title:
        return jsonify({"error": "Slug and title are required"}), 400

    # Check if the slug is already taken (optional)
    existing_division = Division.query.filter_by(slug=slug).first()
    if existing_division:
        return jsonify({"error": "Slug already exists"}), 400

    # Create a new Division object
    new_division = Division(
        slug=slug,
        title=title,
        laboratory_id=1,  # Example default, replace as needed
        create_user_id=1,  # Example default, replace as needed
        update_user_id=1,  # Example default, replace as needed
    )

    # Add the new division to the database
    db.session.add(new_division)
    db.session.commit()

    # Return a response indicating success
    return jsonify({"message": "Division created successfully", "id": new_division.id}), 201

@division_bp.route('/api/v1/division/<int:division_id>', methods=['GET'])
def get_division(division_id):
    # Query the Division by id
    division = Division.query.get(division_id)

    # Check if the division exists
    if not division:
        return jsonify({"error": "Division not found"}), 404

    # Return the division details as JSON
    return jsonify({
        "id": division.id,
        "slug": division.slug,
        "title": division.title,
        "laboratory_id": division.laboratory_id,
        "create_user_id": division.create_user_id,
        "update_user_id": division.update_user_id,
        "create_date": division.create_date,
        "update_date": division.update_date,
        "is_valid": division.is_valid
    }), 200


