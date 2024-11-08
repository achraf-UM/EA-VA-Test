from app import app
from database import db
from sqlalchemy import text

def update_user_columns(division_id_value, group_id_value, user_id=None):
    # SQL query to update division_id and group_id
    update_query = text("""
        UPDATE user
        SET division_id = :division_id, group_id = :group_id
        WHERE (id = :user_id)
    """)
    
    # Execute the query inside the app context
    with app.app_context():
        with db.engine.connect() as conn:
            conn.execute(update_query, {'division_id': division_id_value, 'group_id': group_id_value, 'user_id': user_id})

# Example usage:
# To update division_id and group_id for a specific user
update_user_columns(division_id_value=1, group_id_value=1, user_id=1)


