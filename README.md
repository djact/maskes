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
3. Setup database
  * Make sure you have modern version of Postgresql installed locally
  * from the console, run `createdb maskes`
  * next run `createuser -s -P maskes`, it'll prompt you for a new password, use `maskes`
  * run `python manage.py migrate`
4. Runserver
    ```python
        python manage.py runserver
    ```
:+1:
