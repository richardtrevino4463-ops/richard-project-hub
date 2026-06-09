from flask import Flask, render_template, request

app = Flask(__name__)

visitor_count = 0

@app.route("/")
def home():
    global visitor_count
    visitor_count += 1
    return render_template("home.html", count=visitor_count)

@app.route("/projects")
def projects():
    my_projects = [
        {"title": "Python Web Server", "description": "Built a local Flask web application from scratch, bypassing OneDrive permission locks.", "status": "Completed 🚀"},
        {"title": "Future Project #1", "description": "A cool script, game, or automation tool I plan to build next.", "status": "In Progress 🛠️"},
        {"title": "Future Project #2", "description": "Another awesome coding creation to show off here.", "status": "Planning 📝"}
    ]
    return render_template("index.html", projects=my_projects)

# NEW: This route handles both viewing the contact page and submitting the form
@app.route("/contact", methods=["GET", "POST"])
def contact():
    message_sent = False
    if request.method == "POST":
        # Capture what the user typed into the form fields
        name = request.form.get("name")
        email = request.form.get("email")
        user_message = request.form.get("message")
        
        # Print the message cleanly right into your VS Code terminal
        print("\n=== 📨 NEW MESSAGE RECEIVED ===")
        print(f"From: {name} ({email})")
        print(f"Message: {user_message}")
        print("===============================\n")
        
        message_sent = True
        
    return render_template("contact.html", message_sent=message_sent)

if __name__ == "__main__":
    app.run(debug=True)