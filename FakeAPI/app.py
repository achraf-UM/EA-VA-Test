from flask import  send_from_directory
from database import create_app
from routes.lexique_routes import lexique_bp
from routes.user_routes import user_bp
from routes.civility_routes import civility_bp
from routes.laboratory_routes import laboratory_bp
from routes.user_supervisor_routes import usersupervisor_bp
from routes.division_routes import division_bp
from routes.group_routes import group_bp
from routes.profil_routes import profil_bp

from flask_cors import CORS

app = create_app()
CORS(app) 

app.config['UPLOAD_FOLDER'] = 'uploads'  # Path where your images are stored
app.config['STATIC_FOLDER'] = 'static'   # Optional: If you're using a separate static folder

# Route to serve uploaded images
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    # Flask will serve the files from the "uploads" folder when requested
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

# Register blueprints for routes
app.register_blueprint(lexique_bp)
app.register_blueprint(user_bp) 
app.register_blueprint(civility_bp) 
app.register_blueprint(laboratory_bp) 
app.register_blueprint(usersupervisor_bp) 
app.register_blueprint(division_bp) 
app.register_blueprint(group_bp) 
app.register_blueprint(profil_bp)

# Start the Flask app
if __name__ == '__main__':
    app.run(debug=True)
