from app import create_app, db, socketio
import os

debug = True
port = 8080

app = create_app()

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    socketio.run(app=app, debug=debug, host='0.0.0.0', port=int(os.environ.get('PORT', port)), allow_unsafe_werkzeug=True)
