import paramiko
import argparse
#import pytest

parser = argparse.ArgumentParser(description="Test of init php script")
parser.add_argument("--server", type=str)
parser.add_argument("--username", type=str)
parser.add_argument("--password", type=str)
parser.add_argument("--command", type=str)
args = parser.parse_args()

def init_test(server, username, password, command):
	"""
		Func takes servername, username and password
		Connects to the server with given creds
		Execute command
	"""
	ssh = paramiko.SSHClient()
	ssh.load_system_host_keys()
	ssh.connect(hostname=args.server, username=args.username, password=args.password)
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(args.command, get_pty=True)
	for line in iter(ssh_stdout.readline, ""):
		print(line, end="")
	print("finish")
	ssh.close()

init_test(args.server, args.username, args.password, args.command)
