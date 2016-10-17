#!/usr/bin/python
import requests
import os
from ouimeaux.environment import Environment

# fire-watch.py
# Get a response from slack API that includes channels info
# Using ouimeaux package
# https://ouimeaux.readthedocs.io/en/latest/api.html

# wemo setup via ouimeax package
env = Environment()
env.start()
env.discover()
switch = env.get_switch('wemo-dev')

# get Slack API token
slack_api_token = os.environ['SLACK_API_TOKEN']

firestatus = False

print "Starting Slack API check for fire channel!"
channels_api_url = 'https://slack.com/api/channels.list?token=%s&pretty=1' % slack_api_token

r = requests.get(channels_api_url)
if r.status_code != 200:
    print "Couldn't get a valid response from Slack api, maybe check API token"
    exit(1)

# get string channel name from encoded response and compare
for channel in r.json()['channels']:
    if 'fire-' in str(channel['name']) and str(channel['is_archived']) != 'True':
        print "Fire channel found: %s" % channel['name']
        print "Channel Status: %s " % channel['is_archived']
        firestatus = True
        switch.on()

if not firestatus:
    print 'No fires found in slack'
    switch.off()
