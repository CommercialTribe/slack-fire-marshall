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

# Names of current CT switches for reference
# dev_switch = env.get_switch('wemo-dev')
# cs_switch = env.get_switch('wemo-cs')

# get Slack API token
slack_api_token = os.environ['SLACK_API_TOKEN']

firestatus = False

print "Starting Slack API check for fire channel! Swtiches:"
env.list_switches()
channels_api_url = 'https://slack.com/api/channels.list?token=%s&pretty=1' % slack_api_token

r = requests.get(channels_api_url)
if r.status_code != 200:
    print "Couldn't get a valid response from Slack api, maybe check API token"
    exit(1)

# get string channel name from encoded response and compare
try:
    for channel in r.json()['channels']:
        if 'fire-' in str(channel['name']) and str(channel['is_archived']) != 'True':
            print "Fire channel found: %s" % channel['name']
            print "Channel archived status: %s " % channel['is_archived']
            firestatus = True
            # Turn on all switches in this lan
            for switch in (env.list_switches()):
                print("Turning On : " + switch)
                env.get_switch(switch).on()
except KeyError:
    print "Couldnt get slack channels; is API token env variable correct?"

if not firestatus:
    # Turn off all switches
    print 'No fires found in slack'
    for switch in (env.list_switches()):
        print("Turning Off: " + switch)
        env.get_switch(switch).off()
