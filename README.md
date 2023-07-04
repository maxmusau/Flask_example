## We are going to learn Flask Framework
# Step 1: create a folder known as Flask
# Step 2: Inside the folder, create a python file called app.py and a folder called templates
# Step 3: Inside the templates folder, create an html file called index.html 
# Step 4: Copy the code below and paste it inside the index.html file
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
