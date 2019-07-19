#!/usr/bin/python
import crypt
from termcolor import colored


def cp(cry):
	salt = cry[0:2]
	dict = open('dict.txt','r')
	for word in dict.readlines():
		word = word.strip('\n')
		cryptPass = crypt.crypt(word,salt)
		if (cry == cryptPass):
			print(colored("Found password: " +word, 'green'))
			return
def main():
	passfile=open('pass.txt','r')
	for line in passfile.readlines():
		if ":" in line:
			user = line.split(":")[0]
			cry = line.split(':')[1].strip(' ').strip('\n')
			print(colored("Cracking passoword for: "+user, 'yellow'))
			cp(cry)
	print(colored("[-] Password not found", "red"))
main()

