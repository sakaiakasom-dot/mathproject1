from flask import Flask



def create_app():
    app = Flask(__name__)

    app.config["SECRET_KEY"] = "your-secret-key"
    
    from .drill import drill_bp
    app.register_blueprint(drill_bp)
    
    from .auth import auth_bp
    app.register_blueprint(auth_bp)

    from .hint import hint_bp
    app.register_blueprint(hint_bp)

    from .summary import summary_bp
    app.register_blueprint(summary_bp)
    
    return app

