import argparse
import csv
import os
import subprocess
import sys
from datetime import datetime

rc4_ciphers = []			  # "RC4 Cipher Suites Supported" (65821)
medium_strength_ciphers = []  # "Medium Strength Cipher Suites" (42873)
self_signed_cert = []		  # "Self-Signed Certificate" (57582)
expired_cert = []			  # "Expired Certificate" (15901)
weak_rsa_keys = []			  # "RSA Keys Less Than 2048 Bits" (69551)
ssl_drown = []				  # "SSLv2 DROWN" (83733)
ssl_poodle = []				  # "SSLv3 POODLE" (70574)
signed_weak_algorithm = []	  # "Signed Using Weak Hashing Algorithm" (35291)
logjam = []					  # "Logjam" (83875)


# gets certificate expiration date in datetime format
def parse_expiration_date(log):
    with open(log, 'r') as f:
        lines = f.readlines()

        for line in lines:
            if 'Not valid after:' in line:
                exp = line.replace('Not valid after:', '')
                exp = exp.replace(' GMT', '')
                exp = exp.strip()  # strips out whitespace
                exp = datetime.strptime(exp, '%b %d %X %Y')
                return exp


# determines if certificate is expired
def is_expired(expiration_date):
    current_date = datetime.now()

    if current_date > expiration_date:
        return True

    else:
        return False


# parses csv file and adds to associated lists
def parse_csv(file):
    # opens specified csv file as read-only
    with open(file, 'r') as f:
        reader = csv.DictReader(f)

        # loops through each line in the csv file
        for row in reader:
            if row['Plugin ID'] == '42873':
                medium_strength_ciphers.append(row['Host'] + ':' + row['Port'])

            if row['Plugin ID'] == '65821':
                rc4_ciphers.append(row['Host'] + ':' + row['Port'])

            if row['Plugin ID'] == '57582':
                self_signed_cert.append(row['Host'] + ':' + row['Port'])

            if row['Plugin ID'] == '15901':
                expired_cert.append(row['Host'] + ':' + row['Port'])

            if row['Plugin ID'] == '69551':
                weak_rsa_keys.append(row['Host'] + ':' + row['Port'])

            if row['Plugin ID'] == '89058':
                ssl_drown.append(row['Host'] + ':' + row['Port'])

            if row['Plugin ID'] == '78479':
                ssl_poodle.append(row['Host'] + ':' + row['Port'])

            if row['Plugin ID'] == '35291':
                signed_weak_algorithm.append(row['Host'] + ':' + row['Port'])

            if row['Plugin ID'] == '83875':
                logjam.append(row['Host'] + ':' + row['Port'])

# main
if __name__ == '__main__':
    # parses arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('file')
    args = parser.parse_args()

    # parses specified csv file and adds each finding to their associated list
    parse_csv(args.file)

    # creates output directory to store sslscan output
    if os.path.exists('output') is False:
        os.makedirs('output')

    # combines all lists and de-dupes
    all_systems = list(set(medium_strength_ciphers +
                           rc4_ciphers +
                           self_signed_cert +
                           expired_cert +
                           weak_rsa_keys +
                           ssl_drown +
                           ssl_poodle +
                           logjam +
                           signed_weak_algorithm))

    # runs sslscan on each de-duped system
    for system in all_systems:
        print("Running sslscan on: ", system)

        # creates sslscan log file if it does not exist
        log = open('output/' + system + '.txt', 'w')

        # rdp - runs sslscan with --rdp option
        if system.endswith(':3389'):
            p = subprocess.Popen('sslscan --show-certificate --rdp ' + system,
                                 stdout=log,
                                 stderr=log,
                                 shell=True)
            p.wait()

        # ftp - runs sslscan with the --starttls-ftp option
        elif system.endswith(':21'):
            command = 'sslscan --show-certificate --starttls-ftp ' + system

            p = subprocess.Popen(command,
                                 stdout=log,
                                 stderr=log,
                                 shell=True)
            p.wait()

        # ftps - runs sslscan with the --starttls-ftp option
        elif system.endswith(':990'):
            command = 'sslscan --show-certificate --starttls-ftp ' + system

            p = subprocess.Popen(command,
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

        log.close()  # closes initial write file handle
