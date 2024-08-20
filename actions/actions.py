# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher
from assistant.SpeakFunction import speak
import os

class ActionWakeUp(Action):
    def name(self):
        return "action_wake_up"

    def run(self, dispatcher, tracker, domain):

        speak("I am awake! How can I assist you today?")
        # dispatcher.utter_message(text="I’m awake! How can I assist you today?")
        return [SlotSet("activated", True)]
