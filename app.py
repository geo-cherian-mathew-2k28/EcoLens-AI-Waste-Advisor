import os
from flask import Flask, request, render_template, redirect, url_for
from werkzeug.utils import secure_filename
from model import predict_waste_type # Import our AI prediction function

# --- Configuration ---
UPLOAD_FOLDER = 'uploads' # Directory to temporarily store uploaded files
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# Initialize the Flask app
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

# Ensure the upload folder exists
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    """Checks if the file extension is allowed."""
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# --- Route 1: Home Page (File Upload Form) ---
@app.route('/', methods=['GET'])
def index():
    """Renders the main upload form."""
    # The 'index.html' file will be created in the next step (Phase 3)
    return render_template('index.html')

# --- Route 2: Prediction Endpoint ---
@app.route('/', methods=['POST'])
def upload_file():
    # Check if the post request has the file part
    if 'file' not in request.files:
        return render_template('index.html', error='No file part in the request.')
    
    file = request.files['file']
    
    # If the user does not select a file, the browser submits an empty part
    if file.filename == '':
        return render_template('index.html', error='No selected file.')
    
    if file and allowed_file(file.filename):
        # Securely save the filename and the file itself
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)
        
        # --- Call the AI Model ---
        try:
            predicted_label, advice = predict_waste_type(filepath)
        except Exception as e:
            # Handle potential prediction failures
            predicted_label = "Error"
            advice = f"Prediction system failed: {str(e)}"
            
        # Clean up the uploaded file to save space (Good practice!)
        os.remove(filepath)
        
        # Render the result back to the user
        return render_template('index.html', 
                               prediction=predicted_label, 
                               advice=advice,
                               filename=filename)
                               
    else:
        return render_template('index.html', error='File type not allowed. Use PNG, JPG, or JPEG.')

# Run the application
if __name__ == '__main__':
    # Set debug=True for easier development (reloads server on code changes)
    app.run(debug=True)