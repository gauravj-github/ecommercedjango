<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
 
</head>
<body>

<h1>Django eCommerce Project - Created by Gaurav</h1>

<p>This project is a full-fledged eCommerce platform built using the Django framework. It includes essential features such as product management, cart functionality, user authentication, and payment integration.</p>

<h2>Features</h2>
<ul>
    <li>User authentication (login, signup, logout)</li>
    <li>Product listing and detail view</li>
    <li>Shopping cart functionality</li>
    <li>Order management</li>
    <li>Payment gateway integration</li>
    <li>Search and filtering of products</li>
    <li>Admin dashboard for product and order management</li>
</ul>

<h2>Installation</h2>

<p>Follow these steps to set up the project locally:</p>

<ol>
    <li>Clone the repository:</li>
    <pre><code>git clone https://github.com/gauravj-github/ecommercedjango.git</code></pre>

    <li>Navigate to the project directory:</li>
    <pre><code>cd ecommercedjango/shopin</code></pre>

    <li>Create and activate a virtual environment:</li>
    <pre><code>
# For Linux/macOS:
python3 -m venv venv
source venv/bin/activate

# For Windows:
python -m venv venv
venv\Scripts\activate
    </code></pre>

    <li>Install dependencies:</li>
    <pre><code>pip install -r requirements.txt</code></pre>

    <li>Apply the migrations:</li>
    <pre><code>python manage.py migrate</code></pre>

    <li>Create a superuser for admin access:</li>
    <pre><code>python manage.py createsuperuser</code></pre>

    <li>Run the development server:</li>
    <pre><code>python manage.py runserver</code></pre>

    <li>Access the site at <code>http://127.0.0.1:8000/</code>.</li>
</ol>

<h2>Project Structure</h2>

<p>Here is an overview of the main directories and files in the project:</p>

<ul>
    <li><strong>shopin/</strong>: Main Django application for the eCommerce platform.</li>
    <li><strong>templates/</strong>: Directory containing HTML templates for various views.</li>
    <li><strong>static/</strong>: Directory for static files such as CSS, JavaScript, and images.</li>
    <li><strong>models.py</strong>: Contains the database models for products, orders, users, etc.</li>
    <li><strong>views.py</strong>: Contains the logic for handling requests and rendering templates.</li>
    <li><strong>urls.py</strong>: URL routing for the application.</li>
</ul>

<h2>Technologies Used</h2>
<ul>
    <li>Django (Backend Framework)</li>
    <li>SQLite (Development Database)</li>
    <li>HTML, CSS, JavaScript (Frontend)</li>
    <li>Bootstrap or Tailwind CSS for styling</li>
    <li>Stripe or PayPal for payment integration</li>
</ul>

<h2>Contributing</h2>

<p>Contributions are welcome! Feel free to fork this project, make improvements, and submit a pull request.</p>

<h2>Contact</h2>

<p>If you have any questions or issues, please contact me:</p>
<ul>
    <li>Email: <a href="mailto:gaurav@example.com">gaurav@example.com</a></li>
    <li>GitHub: <a href="https://github.com/gauravj-github">https://github.com/gauravj-github</a></li>
</ul>

</body>
</html>
