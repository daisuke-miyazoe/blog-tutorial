# 手順書
```
$ pip3 install -r requirements.txt
$ mysql.server start
$ mysql -u root
mysql> create database blog_tutorial;
mysql> CREATE USER user@localhost IDENTIFIED BY 'password';
mysql> SELECT user, host FROM mysql.user;
mysql> SHOW GRANTS FOR user@localhost;
mysql> grant all on *.* to user@localhost;
$ python3 manage.py makemigrations
$ python3 manage.py migrate
python3 manage.py createsuperuser
```
