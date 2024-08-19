from assistant.internalCommands.internalCommands import *
import os

def processCommand(command, activated):

    if command:

        command = correctMisrecognitions(command)

        if 'wake up' in command or 'jarvis' in command:
            return executeCommand(
                command, 
                'Hello Sir, how can I help you?', 
                lambda: True,
                activated = True
            )
        
        elif 'go sleep' in command:
            return executeCommand(
                command, 
                'If you need anything, just call me!', 
                lambda: False,
                activated
            )
        
        elif 'exit' in command:
            return executeCommand(
                command, 
                'I am exiting the program!', 
                lambda: os._exit(0),
                activated
            )
            
        elif 'hello' in command:
            return executeCommand(
                command, 
                'Hello! How can I assist you today', 
                lambda: None,
                activated
            )
        
        elif 'what is your name' in command:
            return executeCommand(
                command, 
                'My name is Jarvis.', 
                lambda: None,
                activated
            )
            
        elif 'open' in command:
            pattern, title = getPatternAndTitle(command, '', 'open')
            
            return executeCommand(
                command, 
                'I am opening ' + title + '!', 
                lambda: os.system(f"start {pattern}"),
                activated
            )
        
        elif 'close' in command:
            pattern, title = getPatternAndTitle(command, '', 'close')

            return executeCommand(
                command, 
                'I am closing ' + title + '!', 
                lambda: os.system(f"taskkill /f /im {pattern}.exe"),
                activated
            )
        
        elif 'search in history' in command:
            pattern, title = getPatternAndTitle(command, '%', 'search in history')

            return executeCommand(
                command, 
                'I am searching in history for ' + title + '!', 
                lambda: openChromeTab(pattern, title),
                activated
            )
        
        elif 'search on you tube' in command:
            pattern, title = getPatternAndTitle(command, ' ', 'search on you tube')

            return executeCommand(
                command, 
                'I am searching on youtube for ' + title + '!', 
                lambda: openChromeTab(pattern, title, 'https://www.youtube.com/results?search_query=' + title),
                activated
            )
        
        elif 'search on google' in command:
            pattern, title = getPatternAndTitle(command, ' ', 'search')

            return executeCommand(
                command, 
                'I am searching on google for ' + title + '!', 
                lambda: openChromeTab(pattern, title, 'https://www.google.com/search?q=' + title),
                activated
            )
        
        else:
            return executeCommand(
                command, 
                'Can you repeat that, please?', 
                lambda: None,
                activated
            )
        