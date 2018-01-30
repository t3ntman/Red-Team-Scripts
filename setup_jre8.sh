# This script will install Java Runtime Environment (JRE) 8 Update 162 on x64 Linux systems
# Tested and verified working on Ubuntu 16.04

wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http://www.oracle.com; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u162-b12/0da788060d494f5095bf8624735fa2f1/jre-8u162-linux-x64.tar.gz"
tar -xvf jre-8u162-linux-x64.tar.gz

rm -rf jre-8u162-linux-x64.tar.gz

sudo mv jre1.8.0_162 /usr/local

sudo rm -rf /usr/local/bin/java

sudo ln -s /usr/local/jre1.8.0_162/bin/java /usr/local/bin/java
sudo ln -s /usr/local/jre1.8.0_162/bin/javaws /usr/local/bin/javaws
sudo ln -s /usr/local/jre1.8.0_162/bin/jcontrol /usr/local/bin/jcontrol
sudo ln -s /usr/local/jre1.8.0_162/bin/jjs /usr/local/bin/jjs
sudo ln -s /usr/local/jre1.8.0_162/bin/keytool /usr/local/bin/keytool
sudo ln -s /usr/local/jre1.8.0_162/bin/orbd /usr/local/bin/orbd
sudo ln -s /usr/local/jre1.8.0_162/bin/pack200 /usr/local/bin/pack200
sudo ln -s /usr/local/jre1.8.0_162/bin/policytool /usr/local/bin/policytool
sudo ln -s /usr/local/jre1.8.0_162/bin/rmid /usr/local/bin/rmid
sudo ln -s /usr/local/jre1.8.0_162/bin/rmiregistry /usr/local/bin/rmiregistry
sudo ln -s /usr/local/jre1.8.0_162/bin/servertool /usr/local/bin/servertool
sudo ln -s /usr/local/jre1.8.0_162/bin/tnameserv /usr/local/bin/tnameserv
sudo ln -s /usr/local/jre1.8.0_162/bin/unpack200 /usr/local/bin/unpack200
