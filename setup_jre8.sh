# This script will install Java Runtime Environment (JRE) 8 Update 131 on x64 Linux systems
# Tested and verified working on Ubuntu 16.04

curl -L -b "oraclelicense=a" http://download.oracle.com/otn-pub/java/jdk/8u131-b11/d54c1d3a095b4ff2b6607d096fa80163/jre-8u131-linux-x64.tar.gz -O

tar -xvf jre-8u131-linux-x64.tar.gz

rm -rf jjre-8u131-linux-x64.tar.gz

sudo mv jre1.8.0_131 /usr/local

sudo rm -rf /usr/local/bin/java

sudo ln -s /usr/local/jre1.8.0_131/bin/java /usr/local/bin/java
sudo ln -s /usr/local/jre1.8.0_131/bin/javaws /usr/local/bin/javaws
sudo ln -s /usr/local/jre1.8.0_131/bin/jcontrol /usr/local/bin/jcontrol
sudo ln -s /usr/local/jre1.8.0_131/bin/jjs /usr/local/bin/jjs
sudo ln -s /usr/local/jre1.8.0_131/bin/keytool /usr/local/bin/keytool
sudo ln -s /usr/local/jre1.8.0_131/bin/orbd /usr/local/bin/orbd
sudo ln -s /usr/local/jre1.8.0_131/bin/pack200 /usr/local/bin/pack200
sudo ln -s /usr/local/jre1.8.0_131/bin/policytool /usr/local/bin/policytool
sudo ln -s /usr/local/jre1.8.0_131/bin/rmid /usr/local/bin/rmid
sudo ln -s /usr/local/jre1.8.0_131/bin/rmiregistry /usr/local/bin/rmiregistry
sudo ln -s /usr/local/jre1.8.0_131/bin/servertool /usr/local/bin/servertool
sudo ln -s /usr/local/jre1.8.0_131/bin/tnameserv /usr/local/bin/tnameserv
sudo ln -s /usr/local/jre1.8.0_131/bin/unpack200 /usr/local/bin/unpack200
