
### Project Title:

**Inventory Management System (IMS)**

### Objective:

A basic console-based system that manages inventory for a small business. The system allow admins to create, update, view, and delete products in the inventory while keeping track of stock levels and handling multiple users with role-based permissions.

### Main Features:

1. **User Authentication and Role Management**

   - Support different roles like “Admin” and “User.”
   - Admins can add, edit, and delete products, whereas Users can only view inventory details.
   - Implement a basic login system with username and password validation.

2. **Product Management**

   - List of all products.
   - CRUD operations including filters based search.

3. **User Management**

   - List of all users.
   - CRUD operations including filters based search.

## Instructions
- This project is used `Docker` for `containarization` feature. So, these steps must follow:

<code>streamlit run main.py python manage.py runserver</code>
<h2> Step-1: Download docker (Mac/Window/Linux) if you don't have before:  </h2>
<code> https://docs.docker.com/desktop/</code>

<h2> Step-2: Create a docker image:  </h2>
<code> docker build -t inventory-system</code>

<h2> Step-3: Run docker image in container: </h2>
<code> docker run -it inventory-system</code>

<h2> Step-4: Once, container is started successfully then move into the project directory and execute the following command:</h2>
<code> poetry run python main.py</code>

<h2>Project Snapshots</h2>

<h3>Splash Screen</h3>
<div align="center">

![Login Screen](/static/img/screenshots/login-screen.png)

</div>

<h3>Login Screen</h3>
<div align="center">

![Login Screen](/static/img/screenshots/login2-screen.png)

</div>

<h3>Dashboard</h3>
<div align="center">

![Login Screen](/static/img/screenshots/dashboard.png)
</div>

<h3>Product Management</h3>
<div align="center">

![Login Screen](/static/img/screenshots/product-management.png)
</div>

<h3>User Management</h3>
<div align="center">

![Login Screen](/static/img/screenshots/user-management.png)
</div>

<h3>Role & Permission</h3>
<div align="center">

![Login Screen](/static/img/screenshots/Roles-permission.png)
</div>