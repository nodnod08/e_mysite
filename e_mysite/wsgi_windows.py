# import os
# import sys
# import site
# from django.core.wsgi import get_wsgi_application

# # add python site packages, you can use virtualenvs also
# site.addsitedir("'C:\Users\Dondon\AppData\Local\Programs\Python\Python39\lib\site-packages")

# # Add the app's directory to the PYTHONPATH 
# sys.path.append('C:/xampp/htdocs/e_mysite') 
# sys.path.append('C:/xampp/htdocs/e_mysite/e_mysite')  

# os.environ['DJANGO_SETTINGS_MODULE'] = 'e_mysite.settings' 
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "e_mysite.settings")  
 
# application = get_wsgi_application()

activate_this = "C:/Users/Dondon/.virtualenvs/e_mysite-9RO5hbrO/Scripts/activate_this.py"
# execfile(activate_this, dict(__file__=activate_this))
exec(open(activate_this).read(),dict(__file__=activate_this))

import os
import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('C:/Users/Dondon/.virtualenvs/e_mysite-9RO5hbrO/Lib/site-packages')




# Add the app's directory to the PYTHONPATH
sys.path.append('C:/xampp/htdocs/e_mysite')
sys.path.append('C:/xampp/htdocs/e_mysite/e_mysite')

os.environ['DJANGO_SETTINGS_MODULE'] = 'e_mysite.settings'
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "e_mysite.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()