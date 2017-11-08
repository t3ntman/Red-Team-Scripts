# Description: Installs Let's Encrypt for Apache
# Run sudo certbot --apache -d example.com after running this script
# Source: https://www.digitalocean.com/community/tutorials/how-to-secure-apache-with-let-s-encrypt-on-ubuntu-16-04

sudo add-apt-repository ppa:certbot/certbot
sudo apt-get update
sudo apt-get install python-certbot-apache
