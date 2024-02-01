# DRF_Mixins_CRUD
DjangoRestFramework CRUD by mixins

## Loyiha ketma-ketligi
1. virtual muhit yaratib uni sozlash
```shell
virtualenv env
source env/bin/activate
```
2. Kerakli packagelarni o'rnatib olamiz
```shell
pip install djangorestframework
pip install pillow  # media fayllar bilan ishlash uchun
pip install psycopg2-binary
pip freeze > requirements.txt
```
3. Django project va applarni yaratib olish
```shell
django-admin startproject config .
django-admin startapp library
```
4. PostgreSQLda database yaratib olish
```shell
sudo -u postgres psql  #linux terminalda yoziladi
CREATE DATABASE database name;
CREATE USER username WITH PASSWORD 'your password';
GRANT ALL PRIVILEGES ON DATABASE database TO username;
ALTER ROLE username WITH superuser;
```
5. Configurationlarni to'g'irlash, ya'ni settings va urls fayllarni.
6. Dastur kodlarini yozish