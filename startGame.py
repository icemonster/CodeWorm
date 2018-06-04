import shutil
import os

def createUser(name):
	try:
		shutil.copytree('templates/user', 'users/'+name)
		print 'Created test user folder'
	except:
		print 'Test user folder already exists'
	
	#os 	#Operating system which will contain some vulnerabilities. It can be modified
	#home	#User' home folder where he can put his/her scripts


print 'Initializing...'
try:
	os.mkdir('users')
	print 'Created users folder'
except:
	print 'Users folder already exists'

createUser('test')