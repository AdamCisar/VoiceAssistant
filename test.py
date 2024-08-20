import requests

def send_command_to_rasa(command):
    url = "http://localhost:5005/webhooks/rest/webhook"
    payload = {"message": command}
    response = requests.post(url, json=payload)
    return response.json()

def processCommand(command, activated):
    response = send_command_to_rasa(command)

    print(response)
    if not response:
        return False

    for msg in response:
        if 'text' in msg:
            print(f"Rasa responded: {msg['text']}")
            return True
    
    return False
processCommand("wake up", True)
