import paramiko
import argparse

init_test(server, username, password, command)

def init_test(server, username, password, command):
	"""
		Func takes servername, username and password
		Connects to the server with given creds
		Execute command
	"""
	ssh = paramiko.SSHClient()
	ssh.connect(server, username, password)
	ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command(command)
	assert(true)