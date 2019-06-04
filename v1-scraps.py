import requests
import string
import time

def echo(toRepeate):
    print("CMD Call: Echo ")
    ret(toRepeate[toRepeate.find("echo"):])
    return;


#Controls the out flow message
def ret(msg):
    post_params = {'bot_id': 'BOTID', 'text': msg}
    requests.post('https://api.groupme.com/v3/bots/post', params=post_params)
    return;

request_params = {'token': 'USERID'}
ender = 0
target = 'Aidan'
fc = []

while True:
    response = requests.get('https://api.groupme.com/v3/groups/47728196/messages', params=request_params)

    # If there are new messages, check whether any of them are making queries to the bot
    if (response.status_code == 200):
        print("fffffffffff")
        response_messages = response.json()['response']['messages']

            # Iterate through each message, checking its text
        for message in response_messages:
            print(message['text'])

            if('echo' in message['text']):
                echo(message['text'][5:])

            # resume normal actions
            if (message['text'] == 'resume' and message['name'] == 'Aidan' and message['id'] not in fc):
                fc.append(message['id'])
                ender = 0
                print('resume')

            # emergency stop
            if (message['text'] == 'pause' and message['name'] == 'Aidan' and message['id'] not in fc):
                fc.append(message['id'])
                print('ended')
                exit()

            if (('?' in message['text'] or 'should' in message['text']) and message['id'] not in fc):
                to_r = 'Nah man'
                fc.append(message['id'])
                post_params = {'bot_id': 'BOTID', 'text': to_r}
                requests.post('https://api.groupme.com/v3/bots/post', params=post_params)
                request_params['since_id'] = message['id']

    time.sleep(5)



