from assistant.system_paths.SystemPaths import paths
from assistant.SpeakFunction import speak
import os
import shutil
import sqlite3
import subprocess

def openChromeTab(pattern, title, url=None):
    if url is None:
        url = getLastVisitedUrl(pattern, title)

    if not url:
        return
    
    try:
        subprocess.Popen([paths['chrome'], url])
        speak(f"Opening Chrome with {title}")
    except Exception as e:
        print(f"An error occurred: {e}")
    

def getLastVisitedUrl(pattern, title):
        login = os.getlogin()

        history_db = f'C:\\Users\\{login}\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History'

        temp_db = f'C:\\Users\\{login}\\AppData\\Local\\Temp\\ChromeHistory.db'
        shutil.copy2(history_db, temp_db)

        con = sqlite3.connect(temp_db)
        cursor = con.cursor()

        cursor.execute("SELECT url FROM urls WHERE url LIKE '%" + pattern + "%' ORDER BY last_visit_time DESC LIMIT 1")
        url = cursor.fetchall()

        if not url:
            speak('I could not find any matching results of' + title +' in your history.')
            return None

        con.close()

        if os.path.exists(temp_db):
            os.remove(temp_db)

        return url[0][0]

def getPatternAndTitle(command, patternSymbol, splitWord):
    start_index = command.find(splitWord)
    end_index = start_index + len(splitWord)
    words = command[end_index:].strip()

    return words.replace(' ', patternSymbol), words
