from datetime import datetime
import subprocess
import sys

# gets certificate expiration date in datetime format
def parse_expiration_date(log):
	with open(log, 'r') as f:
		lines = f.readlines()

		for line in lines:
			if 'Not valid after:' in line:
				exp = line.replace('Not valid after:', '')
				exp = exp.replace(' GMT', '')
				exp = exp.strip() # strips out whitespace
				exp = datetime.strptime(exp, '%b %d %X %Y')
				return exp

# determines if certificate is expired
def is_expired(expiration_date):
	current_date = datetime.now()

	if current_date > expiration_date:
		return True

	else:
		return False

if __name__ == '__main__':
	# opens write file handle
	with open(sys.argv[1], 'w+') as log:
		p = subprocess.Popen('sslscan --show-certificate ' + sys.argv[1],
			 	     stdout=log,
			 	     stderr=log,
			 	     shell=True)
		p.wait()

	expiration_date = parse_expiration_date(sys.argv[1])

	print(is_expired(expiration_date))

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
