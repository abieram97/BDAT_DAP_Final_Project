import sys
import os

# Add the current directory to the path for proper import resolution
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'app')))

try:
    from app import create_app
except ImportError as e:
    print(f"Error while importing: {e}")
    sys.exit(1)  # Exit if import fails

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
