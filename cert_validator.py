# python 3.x script
# validates nessus certificate issues
# basically a wrapper around sslscan because laziness ¯\_(ツ)_/¯
# stores all sslscan output in the "output" directory (created if not already present)
# disclaimer: wrote in a few hours - should probably qa a bit more

import argparse
import csv
import os
import subprocess

medium_ciphers = [] 		# medium cipher suites supported list
rc4_ciphers = []		# rc4 cipher suites supported list
self_signed = []		# self-signed certificate list
expired = []			# expired certificate list
weak_rsa_keys = []		# rsa keys less than 2048 bits list
drown = []			# sslv2 drown list
poodle = []			# sslv3 poodle list
logjam = []			# logjam list
signed_weak_alg = []		# signed using weak hashing algorithm list

# validated lists
v_medium_ciphers = []
v_rc4_ciphers = []
v_self_signed = []
v_expired = []
v_weak_rsa_keys = []
v_drown = []
v_poodle = []
v_logjam = []
v_signed_weak_alg = []

if __name__ == '__main__':
	# parses arguments
	parser = argparse.ArgumentParser()
	parser.add_argument('file')
	args = parser.parse_args()

	# opens specified csv file as read-only
	with open(args.file, 'r') as f:
		reader = csv.DictReader(f)

		# loops through each line in the csv file	
		for row in reader:
			# removes none risks
			if row['Risk'] != "None":
				# medium strength cipher suites supported
				if row['Plugin ID'] == '42873':
					medium_ciphers.append(row['Host'] + ':' + row['Port'])

				# rc4 cipher suites supported
				if row['Plugin ID'] == '65821':
					rc4_ciphers.append(row['Host'] + ':' + row['Port'])

				# self-signed certificate
				if row['Plugin ID'] == '57582':
					self_signed.append(row['Host'] + ':' + row['Port'])

				# expired certificate
				if row['Plugin ID'] == '15901':
					expired.append(row['Host'] + ':' + row['Port'])

				# rsa keys less than 2048 bits
				if row['Plugin ID'] == '69551':
					weak_rsa_keys.append(row['Host'] + ':' + row['Port'])

				# sslv2 drown
				if row['Plugin ID'] == '89058':
					drown.append(row['Host'] + ':' + row['Port'])

				# sslv3 poodle
				if row['Plugin ID'] == '78479':
					poodle.append(row['Host'] + ':' + row['Port'])

				# logjam
				if row['Plugin ID'] == '83875':
					logjam.append(row['Host'] + ':' + row['Port'])

				# signed using weak hashing algorithm
				if row['Plugin ID'] == '35291':
					signed_weak_alg.append(row['Host'] + ':' + row['Port'])

	# combines all lists and de-dupes
	all_systems = list(set(medium_ciphers +
		    	       rc4_ciphers +
			       self_signed +
			       expired +
			       weak_rsa_keys +
			       drown +
			       poodle +
			       logjam +
			       signed_weak_alg))
	
	# creates output directory to store sslscan output
	if os.path.exists('output') == False:
		os.makedirs('output')

	# runs sslscan on each de-duped system
	for system in all_systems:
		# creates file if it does not exist
		log = open('output/' + system + '.txt', 'w')
		
		print('validating ' + system)

		# rdp - runs sslscan with --rdp option
		if system.endswith(':3389'):
			p = subprocess.Popen('sslscan --show-certificate --rdp ' + system,
					     stdout=log,
					     stderr=log,
					     shell=True)
			p.wait()

		# ftp - runs sslscan with the --starttls-ftp option
		elif system.endswith(':21'):
			p = subprocess.Popen('sslscan --show-certificate --starttls-ftp ' + system,
					     stdout=log,
					     stderr=log,
					     shell=True)
			p.wait()

		# ftps - runs sslscan with the --starttls-ftp option
		elif system.endswith(':990'):
			p = subprocess.Popen('sslscan --show-certificate --starttls-ftp ' + system,
					     stdout=log,
					     stderr=log,
					     shell=True)
			p.wait()

		# else https
		else:
			p = subprocess.Popen('sslscan --show-certificate ' + system,
					     stdout=log,
					     stderr=log,
					     shell=True)
			p.wait()

		# opens new file handle as read-only
		# not sure why this can't be done in the previous open statement
		with open('output/' + system + '.txt', 'r') as f:
			for line in f:
				if '112' in line:
					print(line)

				if 'RC4' in line:
					print(line)

		# TO DO: append validated systems to new list here

	print('validation complete - full sslscan output saved in "output" directory')
