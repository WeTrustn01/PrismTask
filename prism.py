from app import app, db
from app.models import Trade

#in order to test models without using routes
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Trade': Trade}
