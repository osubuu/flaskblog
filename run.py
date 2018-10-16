# this will grab from __init__.py
from flaskblog import app

# this conditonal is only true if we run this script directly
if __name__ == "__main__":
    app.run(debug=True)
