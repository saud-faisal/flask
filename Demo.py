from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///test.db"             
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False
db=SQLAlchemy(app)

class User(db.Model):
	id=db.Column(db.Integer,primary_key=True)
	name=db.Column(db.String(100),nullable=False)

from wtforms import Form, BooleanField, StringField, PasswordField, validators 
class RegistrationForm(Form):
	name = StringField('Username', [validators.Length(min=4, max=25)])
	#email = StringField('Email Address', [validators.Length(min=6, max=35)])
	#password = PasswordField('New Password', [ validators.DataRequired(), validators.EqualTo('confirm', message='Passwords must match') ])
	#confirm = PasswordField('Repeat Password') accept_tos = BooleanField('I accept the TOS', [validators.DataRequired()])


@app.route("/")
def fun():
	obj=User.query.filter_by(id=1).first()
	x=obj.name
	return x
	
@app.route('/register', methods=['GET', 'POST'])
def register():
	form = RegistrationForm(request.form)
	if request.method == 'POST' and form.validate():
		user = User(form.name.data)
		db_session.add(user)
		flash('Thanks for registering')
		return redirect(url_for('login'))
	return render_template('register.html', form=form)	
	
	
	
	
if __name__=="__main__":
	app.run(debug=True)
	
	
	
	