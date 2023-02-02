"""
The admin configuration in this file will allow us to modify the default Administration interface
to better fit what we need.
"""
from django.contrib import admin

class LuluAdminSite(admin.AdminSite):
    """
    Documentation can be found at: https://docs.djangoproject.com/en/4.1/ref/contrib/admin/
    Variables that can be modified for the Admin Site:
    title_header             "Django site admin Populates the <title> tag on each page of the admin interface
    site_header              "Django administration"   Sets the header on the login form
    index_title              "Site administration"
    index_template           None   Path to find the admin index template. If unset, admin/index.html is used
    app_index_template       None   Path to find the app admin index template. If unset, admin/app_index.html is used
    login_template           None   Path to find the login template. If unset, the admin/login.html is used
    logout_template          None   Path to find the logout template. If unset, the registration/logged_out.html is used
    password_change_template None   Path to find the password change template. If unset, registration/password_change_form.html is used
    password_change_done_template  None Path to find the password change done template. If unset, registration/password_change_done.html template is used
    """

    title_header = 'Lulu Admin'
    site_header  = 'Lulu Administration'
    index_title  = 'Lulu Site Admin'