from app import create_app, db, socketio
import os
import sys
import webbrowser
from colorama import Fore, Style

debug = False
port = 8080

app = create_app()

with app.app_context():
    db.create_all()

if not debug:
    print(f"{Fore.RED}{Style.BRIGHT}Solo cierra esta ventana cuando ya no vayas a utilizar el programa.{Style.RESET_ALL}")
    sys.stdout = None
    sys.stderr = None
    webbrowser.open(f'http://localhost:{port}')

if __name__ == "__main__":
    socketio.run(app=app, debug=True, host='0.0.0.0', port=int(os.environ.get('PORT', 8080)), allow_unsafe_werkzeug=True)
