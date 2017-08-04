# Shell script to setup a WordPress instance on Ubuntu 16.04 systems
# Author: Hunter Hardman @t3ntman
apt-get update
apt-get -y upgrade
apt-get install -y apache2
apt-get install -y mysql-server
apt-get install -y php libapache2-mod-php php-mcrypt php-mysql
wget https://wordpress.org/latest.tar.gz
tar -xvf latest.tar.gz
mv wordpress/* /var/www/html
rm -rf wordpress
chown -R www-data:www-data /var/www/html
rm -rf latest.tar.gz
rm -rf /var/www/html/index.html
mysql -u root -e "create database wordpress;" -p
service apache2 restart
