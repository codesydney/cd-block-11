from app.bcrypt_extension import bcrypt
from app.models import User
from app.database import db
from sqlalchemy import event
from app.sendgrid_emails import send_email


def get_user(email):
	user = User.query.filter_by(email = email).first()
	return user

def create_user(email, user_password):
	try:
		user = User.query.filter_by(email = email).first()
		if(user):
			return 409
		password = bcrypt.generate_password_hash(user_password).decode('utf-8')
		new_user = User(email = email, password = password)
		db.session.add(new_user)
		db.session.commit()
		return 200
	except Exception as e:
		print(f"Error creating user: {str(e)}")
		return 500

def load_user(user_id):
	user = User.query.filter_by(id = int(user_id)).first()
	return user

@event.listens_for(db.session, 'before_commit')
def before_commit(session):
    for obj in session.new:
    	send_email(obj.email)
