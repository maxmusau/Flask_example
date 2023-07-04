# We are going to learn Flask Framework
## Step 1: create a folder known as Flask
## Step 2: Inside the folder, create a python file called app.py and a folder called templates
## Step 3: Inside the templates folder, create an html file called index.html 
### Copy the code below and paste it inside the index.html file
 ``` <!DOCTYPE html>
<html>
    <head>
        <title>Welcome to Our Website</title>
        <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        .header {
            background-color: #333;
            color: #fff;
            padding: 20px;
            text-align: center;
        }

        .container {
            max-width: 800px;
            margin: 20px auto;
            background-color: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        span {
            font-size: 32px;
            margin-bottom: 20px;
        }

        p {
            font-size: 18px;
            margin-bottom: 10px;
        }

        .cta-button {
            display: inline-block;
            background-color: #4CAF50;
            color: #fff;
            padding: 10px 20px;
            font-size: 18px;
            text-decoration: none;
            border-radius: 4px;
        }

        .cta-button:hover {
            background-color: #45a049;
        }
    </style>
    </head>
    <body>
        <div class="header">
            <span><b>Welcome to Our Website</b>
                &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <a class="cta-button"
                    href="/register">Register</a></span>

        </div>

        <div class="container">
            <h1>About Us</h1>
            <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Donec ac
                elit ipsum. Sed vitae urna vel elit convallis tristique.
                Suspendisse potenti. Vestibulum ante ipsum primis in faucibus
                orci luctus et ultrices posuere cubilia Curae; Sed sit amet
                lacus nec orci pulvinar tristique non at lorem. Nullam nec est
                elit. Praesent vitae nibh eu nisl tristique fringilla. Aliquam
                eget eros sed nunc interdum convallis. Donec elementum tellus
                sit amet dui sollicitudin sollicitudin. Mauris et mi vitae dui
                varius efficitur in eu ex. Nunc nec posuere leo.</p>

            <p>Sed sit amet ligula id risus rutrum facilisis. Sed ac maximus
                purus. Vivamus volutpat euismod nunc non rutrum. In interdum,
                velit at fermentum hendrerit, mauris dolor blandit nisl, sit
                amet scelerisque enim lectus vitae nunc. Nunc consectetur, odio
                ac vulputate suscipit, purus nulla facilisis mi, nec tempor est
                elit id sem. Donec malesuada condimentum leo vel cursus. Duis
                vel luctus ex, id gravida metus. Aliquam condimentum velit quis
                diam suscipit, sed consectetur lorem facilisis. Donec eget metus
                vel nisl vulputate vulputate non a mi.</p>

            <a href="#" class="cta-button">Learn More</a>
        </div>
    </body>
</html>
``` 
## Step 4: Still inside the templates folder, create another html file called signup.html
### Copy and paste the code below inside the signup.html
```
<!DOCTYPE html>
<html>
<head>
    <title>User Registration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
            margin: 0;
            padding: 0;
        }

        .container {
            max-width: 400px;
            margin: 100px auto;
            background-color: #fff;
            padding: 40px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            text-align: center;
            margin-bottom: 30px;
        }

        label {
            display: block;
            margin-bottom: 10px;
        }

        input[type="text"],
        input[type="password"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border-radius: 4px;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }
        input[type="email"] {
            width: 100%;
            padding: 10px;
            margin-bottom: 20px;
            border-radius: 4px;
            border: 1px solid #ccc;
            box-sizing: border-box;
        }

        input[type="submit"] {
            width: 100%;
            padding: 10px;
            background-color: #4CAF50;
            color: #fff;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }

        input[type="submit"]:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
   
    <div class="container">
        <h1>User Registration</h1>
        <h2 style="color:red">{{message}}</h2>
        <form action="/register" method="post">
            <label for="username">Username:</label>
            <input type="text" id="username" name="username" >
            <label for="email">Email:</label>
            <input type="email" id="email" name="email" >
            <label for="password">Password:</label>
            <input type="password" id="password" name="password" >
            <label for="confirm_password">Confirm password:</label>
            <input type="password" id="confirm_password" name="confirm_password" >

            <input type="submit" value="Register">
        </form>
    </div>
</body>
</html>


```
## Step 5: To do in class
```
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

```
