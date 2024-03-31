from flask import Flask, render_template, request, jsonify
import mysql.connector
from reportlab.pdfgen import canvas
from flask import send_file
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors


app = Flask(__name__)

# MySQL connection details
db_config = {
    'user': 'students',
    'password': 'oDLla.4r.]l-t-pY',
    'host': 'localhost',
    'database': 'students'
}

# Function to insert registration data into MySQL database
def insert_registration_data(data):
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    query = "INSERT INTO students (first_name, last_name, father_name, class, dob, phone_number) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(query, (data['firstName'], data['lastName'], data['fatherName'], data['class'], data['dob'], data['phoneNumber']))
    conn.commit()
    conn.close()

    # MySQL connection details (omitting for brevity)

"""def generate_pdf(data):
    file_path = 'chalan.pdf'
    p = canvas.Canvas(file_path)
    p.drawString(100, 750, "Chalan Data:")
    y_position = 730
    for key, value in data.items():
        p.drawString(100, y_position, f"{key}: {value}")
        y_position -= 20
    p.showPage()
    p.save()
    return file_path

    """
def generate_pdf(data):
    file_path = 'chalan.pdf'
    p = canvas.Canvas(file_path, pagesize=letter)

    # Set up some basic styles
    p.setFont("Helvetica", 12)
    p.setStrokeColorRGB(0, 0, 0)
    p.setFillColorRGB(0, 0, 0)

    # Add title and the additional line
    title = "Student Chalan"
    line1 = "Please make your payment and get admission now."
    line2 = "Please make payment and upload your screenshot/challan on email student@gmail.com"
    line3 = "Student Data:"
    
    # Add title and lines with proper justification
    p.drawString(100, 750, title)
    p.drawString(100, 730, line1)
    p.drawString(100, 710, line2)
    p.drawString(100, 690, line3)

    # Define positions for each item
    y_positions = [670, 650, 630, 610, 590, 570]
    
    # Add data to the PDF
    label_map = {
        "firstName": "First Name",
        "lastName": "Last Name",
        "fatherName": "Father's Name",
        "class": "Class",
        "dob": "Date of Birth",
        "phoneNumber": "Phone Number"
    }

    for key, value in data.items():
        text = f"{label_map[key]}: {value}"
        y_position = y_positions.pop(0)
        p.drawString(100, y_position, text)

    p.showPage()
    p.save()
    return file_path


@app.route('/')
def index():
    return render_template('index.html')

"""@app.route('/download_chalan', methods=['POST'])
def download_chalan():
    data = request.get_json()
    pdf_buffer = generate_pdf(data)
    response = make_response(pdf_buffer.getvalue())
    response.headers['Content-Disposition'] = 'attachment; filename=chalan.pdf'
    response.headers['Content-Type'] = 'application/pdf'
    return response
"""
"""@app.route('/download_chalan', methods=['POST'])
def download_chalan():
    data = request.get_json()
    pdf_buffer = generate_pdf(data)
    return send_file(pdf_buffer, attachment_filename='chalan.pdf', as_attachment=True)
"""

@app.route('/download_chalan', methods=['POST'])
def download_chalan():
    # Generate PDF
    data = request.get_json()
    file_path = generate_pdf(data)
    # Render the download.html template with the file path
    return send_file(file_path, as_attachment=True)

@app.route('/submit_registration', methods=['POST'])
def submit_registration():
    data = request.get_json()
    insert_registration_data(data)
    return jsonify({'message': 'Registration successful'})

if __name__ == '__main__':
    app.run(debug=True)
