from flask import Flask, jsonify, Blueprint
from database import db
from models.user import User
from models.division import Division
from models.laboratory import Laboratory
from models.group import Group
from models.civility import Civility
from models.user_supervisor import UserSupervisor  # Assuming you have a UserSupervisor model

profil_bp = Blueprint('profil_bp', __name__)

@profil_bp.route('/api/v1/profil/<int:user_id>', methods=['GET'])
def get_profil(user_id):
    try:
        # Fetch the main user record by user_id
        user = User.query.get(user_id)
        if not user:
            return jsonify({"error": "User not found"}), 404

        # Fetch associated civility
        civility = Civility.query.get(user.civility_id)
        civility_data = {
            "id": civility.id,
            "title": civility.title,
            "description": civility.description
        } if civility else None

        # Fetch associated group
        group = Group.query.get(user.group_id)
        group_data = {
            "id": group.id,
            "name": group.name
        } if group else None

        # Fetch associated division
        division = Division.query.get(user.division_id)
        division_data = {
            "id": division.id,
            "title": division.title
        } if division else None

        # Fetch associated laboratory
        laboratory = Laboratory.query.get(user.laboratory_id)
        laboratory_data = {
            "id": laboratory.id,
            "slug": laboratory.slug
        } if laboratory else None

        # Fetch supervisors for the user
        supervisors = UserSupervisor.query.filter_by(user_id=user_id).all()
        supervisor_data = [{
            "id": supervisor.supervisor_id,
            "username": supervisor.supervisor.username,
            "firstname": supervisor.supervisor.firstname,
            "lastname": supervisor.supervisor.lastname,
            "email": supervisor.supervisor.email,
            "photo" : supervisor.supervisor.photo
        } for supervisor in supervisors] if supervisors else []

        # Fetch students supervised by the user
        students = UserSupervisor.query.filter_by(supervisor_id=user_id).all()
        student_data = [{
            "id": student.user_id,
            "username": student.user.username,
            "firstname": student.user.firstname,
            "lastname": student.user.lastname,
            "email": student.user.email,
            "photo": student.user.photo
        } for student in students] if students else []

        # Aggregate and return the response
        response_data = {
            "user": {
                "user_id": user.id,
                "firstname": user.firstname,
                "lastname": user.lastname,
                "username": user.username,
                "email": user.email,
                "civility": civility_data,
                "group": group_data,
                "division": division_data,
                "laboratory": laboratory_data,
                "photo": user.photo
            },
            "supervisors": supervisor_data,
            "students": student_data
        }

        return jsonify(response_data), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred while retrieving user information.', 'details': str(e)}), 500
