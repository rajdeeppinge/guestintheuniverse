from flask import Flask
from routes.api_routes import api_bp
from routes.main_routes import main_bp

def create_app():
    app = Flask(__name__)
    
    # Register blueprints
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    
    return app

app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
