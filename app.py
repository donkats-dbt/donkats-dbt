from flask import Flask, render_template, request, send_file
from meal_logic import generate_pdf

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/preview', methods=['POST'])
def preview():
    data = request.form.to_dict()
    return render_template('preview.html', data=data)

@app.route('/download', methods=['POST'])
def download():
    data = request.form.to_dict()
    pdf_path = generate_pdf(data)
    return send_file(pdf_path, as_attachment=True)

if __name__ == '__main__':
    
    import os

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
