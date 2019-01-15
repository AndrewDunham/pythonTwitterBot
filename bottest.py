from twython import Twython


class bot:
	
	def __init__(key, secret, token, tokenSecret):
		self.key = key
		self.secret = secret
		self.token = token
		self.tokenSecret = tokenSecret
		
		self.account = Twython(self.key, self.secret, self.token, self.tokenSecret)
		
	def setStatus(status):
		self.account.update_status(status)


def main():
	print('wew')
	t = bot()
	
	
if __name__ == '__main__':
	main()
