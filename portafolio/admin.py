from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin): 
    readonly_fields = ('created', 'datecompleted')
    
admin.site.register(Task, TaskAdmin)

admin.site.registered_models = ['Task']
admin.site.site_title = "Portfolio Admin Portal"
admin.site.site_header = "Portfolio Admin"

# Cambiar colores del admin
admin.site.index_title = "Administración de Tareas"

# Añadir CSS personalizado
admin.AdminSite.enable_nav_sidebar = False

# Estilo personalizado
admin_css = """
<style>
    :root {
        --primary-color: #667eea;
        --secondary-color: #764ba2;
    }
    
    #header {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .module h2, .module caption {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
    }
    
    .submit-row input[type="submit"],
    .submit-row input[type="button"],
    .submit-row input[type="image"] {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
    }
    
    .submit-row input[type="submit"]:hover,
    .submit-row input[type="button"]:hover {
        background: linear-gradient(135deg, #764ba2 0%, #667eea 100%);
    }
    
    a:link, a:visited {
        color: #667eea;
    }
    
    a:hover {
        color: #764ba2;
    }
</style>
"""
