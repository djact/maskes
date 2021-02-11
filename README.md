# Installation
1. Database Setup 
    * Install latest PostgreSQL:
        ```
        MacOSX: https://www.postgresql.org/download/macosx/
        EDB: https://www.enterprisedb.com/downloads/postgres-postgresql-downloads
    * export ph_config path:
        ```
        ### for macOSX postgresql v13.1 using EDB installer ###
        $ export PATH="/Library/PostgreSQL/13/bin:$PATH"
    * from the console, run 
        ```
        createdb -U postgres maskes
        createuser -U postgres -s -P maskes
        ```
        it'll prompt you for a password for new role, use `maskes`
2. Clone Project:    
    ```
    git clone https://github.com/djact/maskes.git
    ```
3. Python Setup:
    * Download/Install Python
        ```
        https://www.python.org/downloads/
    * Create/Activate python virtual environment
        ```
        python3 -m venv env
        source env/bin/activate
    * Install dependencies:
        ```
        pip install -r requirements.txt
    * Migration:
        ```
        python manage.py migrate 
    * Create a superuser:
        ```
        python manage.py createsuperuser
        ```
    * Add some seed data with 
        ```
        python generate_faker.py
        ```
4. Runserver
    ```
        python manage.py runserver
    ```
5. You can then log in to the admin portal with your superuser account at 
    ```
    http://localhost:8000/admin/
    ```
6. Email Setup (optional): using your email to send email, create local_settings.py next to settings.py:
    <font size="1" style="color:gray">-> make sure local_settings.py is in .gitingore</font>
    ```python
        SECRET_KEY = 'yoursecretkey'
        DEBUG = True
        EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
        EMAIL_HOST = '<your-email-host>' 
        EMAIL_PORT = '<email-port>' # eg: 587
        EMAIL_HOST_USER = 'youremail@example.com'
        EMAIL_HOST_PASSWORD = 'your-password' #not support 2-Step Verification
        EMAIL_USE_TLS = True
    ```
    *<font size="1">Set Google App Passwords info: https://support.google.com/accounts/answer/185833?hl=en</font>*
      
:+1: