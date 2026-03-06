diff --git a//Users/tarunsingh/django-learning/readme.md b//Users/tarunsingh/django-learning/readme.md
--- a//Users/tarunsingh/django-learning/readme.md
+++ b//Users/tarunsingh/django-learning/readme.md
@@ -0,0 +1,41 @@
+# Django Setup (macOS/Homebrew Python)
+
+## Why your command failed
+
+1. `source .venv/bin/activate` failed because `.venv` does not exist in that folder.
+2. `pip3 install vern` used system Python and also has a typo:
+   - `vern` is not `venv`.
+   - `venv` is built-in; you do not install it with `pip`.
+3. `externally-managed-environment` is expected on Homebrew Python when installing globally.
+
+## Correct commands (run inside your project folder)
+
+```bash
+cd DJANGO_TUTORIAL
+python3 -m venv .venv
+source .venv/bin/activate
+python -m pip install --upgrade pip
+pip install django
+```
+
+Verify:
+
+```bash
+which python
+python --version
+django-admin --version
+```
+
+Expected `which python` output should include:
+
+`.../DJANGO_TUTORIAL/.venv/bin/python`
+
+## Start a Django project
+
+```bash
+django-admin startproject config .
+python manage.py migrate
+python manage.py runserver
+```
+
+Open `http://127.0.0.1:8000/`.
