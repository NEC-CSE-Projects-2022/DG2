from flask import Flask, render_template, request, redirect, url_for, flash
import os
import pandas as pd
from werkzeug.utils import secure_filename

app = Flask(__name__, static_url_path='/static')
app.secret_key = 'your_secret_key'
UPLOAD_FOLDER = './uploads'
ALLOWED_EXTENSIONS = {'csv', 'xlsx', 'xls'}
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    """Check if file has a valid extension."""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def index():
    return render_template('index.html')  # Changed this line to render index.html

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file uploaded!')
            return redirect(request.url)
        
        file = request.files['file']
        if file.filename == '':
            flash('No file selected!')
            return redirect(request.url)
        
        if not allowed_file(file.filename):
            flash('Invalid file type! Please upload a CSV or Excel file.')
            return redirect(request.url)

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        try:
            if filename.endswith('.csv'):
                df = pd.read_csv(filepath)
            else:
                df = pd.read_excel(filepath)
            
            if df.empty:
                os.remove(filepath)
                flash('Empty file! Please upload a file with data.')
                return redirect(request.url)
        except Exception as e:
            os.remove(filepath)
            flash(f'Error reading file: {str(e)}')
            return redirect(request.url)

        flash('File uploaded successfully!')
        return redirect(url_for('train', filename=filename))

    return render_template('prediction/base.html')

@app.route('/predict')
def predict():
    return render_template('prediction/base.html')

@app.route('/train/<filename>', methods=['GET'])
def train(filename):
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    try:
        from model.train_model import train_model
        results = train_model(filepath, target_column='Label')
        return render_template('prediction/results.html', results=results)
    except Exception as e:
        return f"An error occurred during training: {str(e)}"

if __name__ == '__main__':
    app.run(debug=True)
