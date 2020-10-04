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
3. Ask Duc or one of the other developers for the `.env` file and place it in the root of the project
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
    
5. Add some seed data with `python generate_faker.py`
5. Runserver
    ```python
        python manage.py runserver
    ```
:+1: