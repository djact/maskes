**LIVE:** https://skcema-live.herokuapp.com/

**HOME PAGE**
<img width="1428" alt="demo" src="https://user-images.githubusercontent.com/61364158/132037359-94b43497-9536-48b0-a2b0-9b0fdf512728.png">

**ADMIN DASHBOARD**
<img width="1428" alt="admin" src="https://user-images.githubusercontent.com/61364158/132035487-347c9b39-025d-437d-85d2-5f6d20a5d855.png">



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
        
        #AMAZON S3 in production
        if not DEBUG:
            AWS_ACCESS_KEY_ID = 'your-aws-access-key'
            AWS_SECRET_ACCESS_KEY = 'you-aws-secret-access-key'
            AWS_STORAGE_BUCKET_NAME = 'aws-s3-bucket-name'
            AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME
            AWS_S3_OBJECT_PARAMETERS = {
                'CacheControl': 'max-age=86400',
            }
            AWS_LOCATION = 'static'
            STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
            DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
            STATIC_URL = 'https://%s/%s/' % (AWS_S3_CUSTOM_DOMAIN, AWS_LOCATION)

        STRIPE_PUBLISHABLE_KEY='your-stripe-public-key'
        STRIPE_SECRET_KEY='yourt-stripe-secret-key'
        STRIPE_WEBHOOK_SECRET='your-stripe-webhook-secret'
    ```
    *<font size="1">Set Google App Passwords info: https://support.google.com/accounts/answer/185833?hl=en</font>*
      
:+1:
