import os
from flask import Flask, jsonify
from dotenv import load_dotenv

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["APP_NAME"] = os.getenv("APP_NAME", "Backend Health Service")
    app.config["ENVIRONMENT"] = os.getenv("APP_ENV", "development")

    @app.get("/")
    def home():
        return jsonify({
            "message": f"Welcome to {app.config['APP_NAME']}",
            "status": "running"
        }), 200

    @app.get("/health")
    def health_check():
        return jsonify({
            "status": "healthy",
            "service": app.config["APP_NAME"],
            "environment": app.config["ENVIRONMENT"]
        }), 200

    return app

app = create_app()

if __name__ == "__main__":
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", "5000"))
    debug = os.getenv("FLASK_DEBUG", "false").lower() == "true"
    app.run(host=host, port=port, debug=debug)
