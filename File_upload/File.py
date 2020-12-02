#file upload 
import os 
from flask import Flask, flash, request, redirect, url_for 
from werkzeug.utils import secure_filename 
UPLOAD_FOLDER = '/flask/File upload/upload/' 
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__) 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER                     

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET','POST'])
def upload_file():
	if request.method=='POST':
		#checkifthepostrequesthasthefilepart
		if 'file' not in request.files:
			flash('No file part')
			return redirect(request.url)
		file=request.files['file']
		#ifuserdoesnotselectfile,browseralso
		#submitanemptypartwithoutfilename
		if file.filename=='':
			flash('No selected file')
			return redirect(request.url)
		if file and allowed_file(file.filename):
			filename=secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			return redirect(url_for('uploaded_file',filename=filename))
			
	return '''<!doc type html><title>UploadnewFile</title><h1>UploadnewFile</h1><form method=post enctype=multipart/form-data><input type=file name=file><input type=submit value=Upload></form>'''


if __name__=="__main__":
	app.run(debug=True)