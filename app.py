import os
from flask import Flask, render_template, request, redirect, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "supersecretkeyforflashmessages"  # Required for flash messages to work

# Flask-Mail Configuration
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'richardtrevino4463@gmail.com'

# SECURITY FIX: Pulling the password safely from Render's environment variables
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config['MAIL_DEFAULT_SENDER'] = 'richardtrevino4463@gmail.com'

mail = Mail(app)

# Route 1: Home Page (Skyline)
@app.route("/")
def home():
    return render_template("home.html")

# Route 2: Projects Showcase Page
@app.route("/projects")
def projects():
    return render_template("index.html")

# Route 3: Contact Form Page (Handles both viewing the form and submitting it)
@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        message_content = request.form.get("message")
        
        # Create the email message
        msg = Message(
            subject=f"New Portfolio Message from {name}",
            recipients=['richardtrevino4463@gmail.com'],
            body=f"You have received a new message from your portfolio contact form:\n\n"
                 f"Name: {name}\n"
                 f"Email: {email}\n\n"
                 f"Message:\n{message_content}"
        )
        
        try:
            mail.send(msg)
            flash("Success! Your message has been sent.", "success")
        except Exception as e:
            flash("Something went wrong. Please try again later.", "danger")
            print(f"Email Error: {e}")
            
        return redirect("/contact")
        
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)