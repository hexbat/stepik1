sudo apt-get install python-django mysql-server-5.5
sudo rm /etc/nginx/sites-enabled/*
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo rm /etc/gunicorn.d/test
sudo rm /etc/gunicorn.d/ask
#sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/guni_ask.conf   /etc/gunicorn.d/ask
#sudo gunicorn -c /home/box/web/etc/guni_ask.conf ask.wsgi:application
cd ~/web/ask
#gunicorn --bind=0.0.0.0:8000 ask.wsgi:application
#sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start
mysql -u root < ~/web/ask.sql
python ~/web/ask/manage.py makemigrations qa
python ~/web/ask/manage.py migrate
chmod +x manage.py

