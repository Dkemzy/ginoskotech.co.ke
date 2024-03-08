from flask import Flask, render_template, request, redirect, url_for
from flask_mail import Mail, Message

app = Flask(__name__)

# Configure Flask-Mail
app.config['MAIL_SERVER'] = 'smtp.example.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = '#'
app.config['MAIL_PASSWORD'] = '#'
app.config['MAIL_DEFAULT_SENDER'] = '#'
app.config['MAIL_MAX_EMAILS'] = 1000

mail = Mail(app)

# Home route
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/solutions')
def solutions():
    return render_template('solutions.html')

@app.route('/company')
def company():
    return render_template('company.html')

@app.route('/key-clients')
def key_clients():
    return render_template('key_clients.html')

@app.route('/contact_form')
def contact_form():
    return render_template('contact_form.html')


# Contact form route
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        # Process the form data
        name = request.form['name']
        company = request.form['company']
        email = request.form['email']
        phone = request.form['phone']
        how_help = request.form['how_help']

        # Send email
        subject = 'New Contact Form Submission'
        body = f'''
        Name: {name}
        Company: {company}
        Email: {email}
        Phone: {phone}
        How can we help: {how_help}
        '''

        msg = Message(subject, recipients=['marketingteam@ginoskotech.co.ke'])
        msg.body = body
        mail.send(msg)

        # Redirect to a thank you page or any other page
        return redirect(url_for('thank_you'))

    return render_template('contact_form.html')

# Thank you route
@app.route('/thank-you')
def thank_you():
    return render_template('thank_you.html')

# Newsletter form route
@app.route('/newsletter', methods=['POST'])
def newsletter():
    if request.method == 'POST':
        # Process the newsletter form data
        email = request.form['email']

        # Send an email
        msg = Message('New Newsletter Subscription', recipients=['marketingteam@ginoskotech.co.ke'])
        msg.body = f"Someone subscribed to the newsletter with the email: {email}"
        mail.send(msg)

        # You can add your logic here to handle the newsletter form data

    # Redirect to a thank you page
    return redirect(url_for('thank_you'))

if __name__ == '__main__':
    app.run(debug=True)
