from flask import Blueprint, request, jsonify
from database import db
from models.user_supervisor import UserSupervisor
from models.user import User


usersupervisor_bp = Blueprint('usersupervisor', __name__)

@usersupervisor_bp.route('/api/v1/usersupervisor', methods=['POST'])
def add_supervisor():
    try:
        data = request.get_json()

        # Check if user_id and supervisor_id are in the body
        if not all(key in data for key in ['user_id', 'supervisor_id']):
            return jsonify({'error': 'Missing user_id or supervisor_id'}), 400

        user_id = data['user_id']
        supervisor_id = data['supervisor_id']

        # Ensure the user and supervisor exist
        user = User.query.get(user_id)
        supervisor = User.query.get(supervisor_id)

        if not user or not supervisor:
            return jsonify({'error': 'User or supervisor not found'}), 404

        # Create and add the new user-supervisor relationship
        new_supervisor = UserSupervisor(user_id=user_id, supervisor_id=supervisor_id)
        db.session.add(new_supervisor)
        db.session.commit()

        return jsonify({
            'message': 'Supervisor added successfully',
            'user_id': user_id,
            'supervisor_id': supervisor_id
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({'error': 'An error occurred while adding the supervisor', 'details': str(e)}), 500
    
@usersupervisor_bp.route('/api/v1/usersupervisor/<int:user_id>', methods=['GET'])
def get_all_supervisors(user_id):
    try:
        # Query for all supervisors where the user_id matches
        supervisors = UserSupervisor.query.filter_by(user_id=user_id).all()

        if not supervisors:
            return jsonify({'message': 'No supervisors found for this user'}), 404

        # Format the results to include supervisor details
        supervisor_list = []
        for supervisor in supervisors:
            supervisor_data = {
                'user_id': supervisor.user_id,
                'supervisor_id': supervisor.supervisor_id,
                'supervisor': {
                    'id': supervisor.supervisor.id,
                    'username': supervisor.supervisor.username,
                    'firstname': supervisor.supervisor.firstname,
                    'lastname': supervisor.supervisor.lastname,
                    'email': supervisor.supervisor.email,
                    'photo': supervisor.user.photo
                }
            }
            supervisor_list.append(supervisor_data)

        return jsonify({'supervisors': supervisor_list}), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching supervisors', 'details': str(e)}), 500
    

@usersupervisor_bp.route('/api/v1/usersupervisor/apprenatsuivi/<int:supervisor_id>', methods=['GET'])
def get_students(supervisor_id):
    try:
        # Query for all users who have the given supervisor_id
        students = UserSupervisor.query.filter_by(supervisor_id=supervisor_id).all()

        if not students:
            return jsonify({'message': 'No students found for this supervisor'}), 404

        # Format the results to include student details
        student_list = []
        for student in students:
            student_data = {
                'user_id': student.user_id,
                'supervisor_id': student.supervisor_id,
                'student': {
                    'id': student.user.id,
                    'username': student.user.username,
                    'firstname': student.user.firstname,
                    'lastname': student.user.lastname,
                    'email': student.user.email,
                    'photo': student.user.photo
                }
            }
            student_list.append(student_data)

        return jsonify({'students': student_list}), 200

    except Exception as e:
        return jsonify({'error': 'An error occurred while fetching students', 'details': str(e)}), 500
