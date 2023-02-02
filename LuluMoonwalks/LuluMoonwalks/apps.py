from django.contrib.admin.apps import AdminConfig

class LuluAdminConfig(AdminConfig):
    default_site = "admin.LuluAdminSite"
