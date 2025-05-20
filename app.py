from flask import Flask, render_template, request, send_file, session, redirect
from meal_logic import generate_pdf
import os

app = Flask(__name__)
app.secret_key = 'your-secret-key'

@app.route('/')
def home():
    return render_template("landing.html")

@app.route('/form')
def form():
    return render_template("form.html")

@app.route('/preview', methods=['POST'])
def preview():
    data = request.form.to_dict()
    data['include_fish_friday'] = request.form.get('include_fish_friday') in ['on', 'true', '1']
    return render_template('preview.html', data=data)

@app.route('/download', methods=['GET', 'POST'])
def download():
    if not session.get('paid'):
        return redirect("/pay")
    if request.method == 'POST':
        data = request.form.to_dict()
        pdf_path = generate_pdf(data)
        return send_file(pdf_path, as_attachment=True)
    return send_file("meal_plan_output.pdf", as_attachment=True)

@app.route('/confirm', methods=['POST'])
def confirm():
    session['paid'] = True
    return '', 204

@app.route("/pay")
def pay():
    return render_template("pay.html")

@app.route("/landing")
def landing():
    return render_template("landing.html")

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port, debug=True)
