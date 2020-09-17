from abc import abstractmethod


class Printer:
    def __init__(self, message):
        self._message = message

    abstractmethod

    def welcome(self):
        pass
