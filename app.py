from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# In-memory storage for registered users
users = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST','GET'])
def register():
    # Get form data
    if request.method=='POST':
        
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')
        confirm = request.form.get('confirm_password')

        # Validate form data
        if not username or not email or not password or not confirm:
            return render_template("signup.html",message="Error: Please  fill in all the fields")
        elif password != confirm:
            return render_template("signup.html",message="Error: Password do not match confirm password")
        # Check if user already exists
        for user in users:
            if user['username'] == username:
                return "Error: User already exists." 

        # Register the user
        user = {'username': username, 'email': email,'password': password}
        users.append(user)
        print(users)

        return 'Registration Successful \n' '<a style="color:blue;" href="/register">Go Back</a>'
    
    else:
        return render_template("signup.html")
@app.route('/users')
def display_users():
    # print(users)
    for user in users:
        print(f"Username: {user['username']}")
    return users


app.run(debug=True)
