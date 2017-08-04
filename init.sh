sudo rm /etc/nginx/sites-enabled/*
sudo ln -s /home/box/web/etc/nginx.conf  /etc/nginx/sites-enabled/test.conf
sudo /etc/init.d/nginx restart
sudo rm /etc/gunicorn.d/test
sudo rm /etc/gunicorn.d/ask
sudo ln -s /home/box/web/etc/gunicorn.conf   /etc/gunicorn.d/test
sudo ln -s /home/box/web/etc/guni_ask.conf   /etc/gunicorn.d/ask
sudo /etc/init.d/gunicorn restart
sudo /etc/init.d/mysql start

