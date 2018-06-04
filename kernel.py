#Excutes main loop

def evalL(line):
	if line.startswith('print'):
		return eval(line)

class Job:
	def __init__(self, user, path):
		self.user = user
		self.script = open('users/{}/{}'.format(user.name,path)).read().split('\n')
		self.currentLine = 0
	def executeNextLine(self):
		if self.currentLine == len(self.script):
			return 1

		print(evalL(self.script[self.currentLine]))
		self.currentLine += 1

class User:
	def __init__(self, username):
		self.name = username
		self.jobs = []
		self.cpu = (1,1) #1 core, 1 hertz
						#number of cores = number of tasks its possible to do at the same time
						#number of hertz = number of lines of code executed at once
	def addJob(self, path):
		job = Job(self, path)
		self.jobs.append(job)
	def tick(self):
		toRemove = []
		for cpu in range(self.cpu[0]):
			if cpu >= len(self.jobs):
				break
			for i in range(self.cpu[1]):
				if self.jobs[cpu].executeNextLine():
					toRemove.append(self.jobs[cpu])
					break
		for job in toRemove:
			self.jobs.remove(job)

class Worker:
	def __init__(self):
		self.users = [] #FIXME change to Hashmap?
	def addJob(self, user, path):
		for u in self.users:
			if u.name == user:
				u.addJob(path)
	def addUser(self, user):
		self.users.append(User(user))
	def tick(self):
		for user in self.users:
			user.tick()
			if len(user.jobs) == 0:
				return 0
		return 1

worker = Worker()
worker.addUser('test')
worker.addJob('test','os/startup.wo')

while worker.tick(): pass