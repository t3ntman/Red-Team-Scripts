from datetime import datetime
import subprocess
import sys

# gets the expiration date from the certificate information
# converts that string into a datetime object
# returns converted datetime object
def parse_expiration_date():
	with open(sys.argv[1], 'r') as f:
		lines = f.readlines()

		for line in lines:
			if 'Not valid after:' in line:
				expiration = line.replace('Not valid after:', '')
				expiration = expiration.replace(' GMT', '')
				expiration = expiration.strip() # strips out tab
				expiration = datetime.strptime(expiration, '%b %d %X %Y')
				return expiration

if __name__ == '__main__':
	# opens write file handle
	with open(sys.argv[1], 'w+') as log:
		p = subprocess.Popen('sslscan --show-certificate ' + sys.argv[1],
			 	     stdout=log,
			 	     stderr=log,
			 	     shell=True)
		p.wait()

	expiration_date = parse_expiration_date()
	current_date = datetime.now()

	if current_date > expiration_date:
		print("Expired")

	else:
		print("Not Expired")

'''
	# opens read file handle
	with open(sys.argv[1], 'r') as f:
		log = f.read()

		if 'SSLv2' in log:
			print('SSLv2 Supported')
			print('SSLv2 DROWN')

		if 'SSLv3' in log:
			print('SSLv3 Supported')
			print('SSLv3 POODLE')

		if 'RC4' in log:
			print('RC4 Cipher Suites Supported')
'''
