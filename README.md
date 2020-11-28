# Installation
1. Create venv
    ```python
        python3 -m venv env
    ```
2. Install packages:
    ```python
        source env/bin/activate
        pip install -r requirements.txt
    ```
3. optional: using your email to send email, create local_settings.py next to settings.py:
    <font size="1" style="color:gray">-> make sure local_settings.py is in .gitingore</font>
    ```python
        SECRET_KEY = 'yoursecretkey' # eg:n!+$0%qf#$ldt7t5^7@a*%jo7s)yxe468av72z#hq)bx^+qu9d
        DEBUG = True
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = '<your-email-host>' 
        EMAIL_PORT = '<email-port>' # eg: 587
        EMAIL_HOST_USER = 'youremail@example.com'
        EMAIL_HOST_PASSWORD = 'your-password' #not support 2-Step Verification
        EMAIL_USE_TLS = True
    ```
    *<font size="1">Set Google App Passwords info: https://support.google.com/accounts/answer/185833?hl=en</font>*
    
4. Setup database
    * Make sure you have modern version of Postgresql installed locally
    * from the console, run `createdb maskes`
    * next run `createuser -s -P maskes`    
    it'll prompt you for a password, use `maskes`
5. To migrate, run:
    ```python
        python manage.py migrate
    ```
6. Create a superuser:
    ```python
        python manage.py createsuperuser
    ```
    
7. Add some seed data with `python generate_faker.py`
8. Runserver
    ```python
        python manage.py runserver
    ```
9. You can then log in to the admin portal with your superuser account at http://localhost:8000/admin/

:+1: