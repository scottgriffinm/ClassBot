#classBot.py
#python3
# A centralized location for all of my classes' assignment sources.

import webbrowser as wb
import sys
import time


classes = [
    {'name':'Business Communiation and Protocol',
     'links':['placeholder'],
     },
    {'name':'Real Estate Process',
     'links':['placeholder'],
     },
    {'name':'International Finance',
     'links':['placeholder'],
     },
    {'name':'''Dante's Inferno''',
     'links':['placeholder'],
     },
    {'name':'Intro to Marketing Strategy',
     'links':['placeholder'],
     },
    {'name':'Music of Latin America and the Carribean',
     'links':['placeholder'],
     },
    {'name':'University Choir',
     'links':['placeholder'],
     },
    ]

numOfClasses = len(classes)

while True:
    message = '''\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nLets get some work done.

Type the corresponding number and hit enter to launch a classes work source, or type 'all' and hit enter to launch them all.'''
    
    # counter variable for codes
    iii = 0
    for v in classes:   # add classes and their numbers to the message
        iii += 1
        addToMessage = '\n\n' + str(iii) + ': ' + v['name']
        message = message + addToMessage
    message = message + '\n'
    
    print(message)
    choice = input()
    try:
        choice = int(choice)
        if (choice < 1) or (choice > numOfClasses):
            print('Invalid input.')
            time.sleep(1)
        else:
            choice = choice - 1 # adjust to pick class out of list (list indexs begin with 0)
            # launch all links for that class
            for link in classes[choice]['links']:
                wb.open(link)
    except ValueError:
        if choice == 'all':
            #open all class links
            for v in classes:
                for link in v['links']:
                    wb.open(link)
        else:
            print('Invalid input.')
            time.sleep(1)
            
