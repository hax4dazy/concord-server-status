from atproto import Client
import os, random, time

client = Client()
client.login(os.environ['USER_ACCOUNT'], os.environ["APP_PASSWORD"])


while True:
	client.send_post('No')
	time.sleep(21600)