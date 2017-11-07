# This script will install Java Runtime Environment (JRE) 8 Update 151 on x64 Linux systems
# Tested and verified working on Ubuntu 16.04

wget --no-cookies --no-check-certificate --header "Cookie: gpw_e24=http://www.oracle.com; oraclelicense=accept-securebackup-cookie" "http://download.oracle.com/otn-pub/java/jdk/8u151-b12/e758a0de34e24606bca991d704f6dcbf/jre-8u151-linux-x64.tar.gz"

tar -xvf jre-8u151-linux-x64.tar.gz

rm -rf jre-8u151-linux-x64.tar.gz

sudo mv jre1.8.0_151 /usr/local

sudo rm -rf /usr/local/bin/java

sudo ln -s /usr/local/jre1.8.0_151/bin/java /usr/local/bin/java
sudo ln -s /usr/local/jre1.8.0_151/bin/javaws /usr/local/bin/javaws
sudo ln -s /usr/local/jre1.8.0_151/bin/jcontrol /usr/local/bin/jcontrol
sudo ln -s /usr/local/jre1.8.0_151/bin/jjs /usr/local/bin/jjs
sudo ln -s /usr/local/jre1.8.0_151/bin/keytool /usr/local/bin/keytool
sudo ln -s /usr/local/jre1.8.0_151/bin/orbd /usr/local/bin/orbd
sudo ln -s /usr/local/jre1.8.0_151/bin/pack200 /usr/local/bin/pack200
sudo ln -s /usr/local/jre1.8.0_151/bin/policytool /usr/local/bin/policytool
sudo ln -s /usr/local/jre1.8.0_151/bin/rmid /usr/local/bin/rmid
sudo ln -s /usr/local/jre1.8.0_151/bin/rmiregistry /usr/local/bin/rmiregistry
sudo ln -s /usr/local/jre1.8.0_151/bin/servertool /usr/local/bin/servertool
sudo ln -s /usr/local/jre1.8.0_151/bin/tnameserv /usr/local/bin/tnameserv
sudo ln -s /usr/local/jre1.8.0_151/bin/unpack200 /usr/local/bin/unpack200
