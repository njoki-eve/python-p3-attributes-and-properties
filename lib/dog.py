#!/usr/bin/env python3

class Dog:
    APPROVED_BREEDS = [
        "Mastiff",
        "Chihuahua",
        "Corgi",
        "Shar Pei",
        "Beagle",
        "French Bulldog",
        "Pug",
        "Pointer"
    ]

    def __init__(self, name=None, breed=None):
        self._name = None
        self._breed = None
        if name is not None:  # Only validate if name was provided
            self.name = name
        if breed is not None:  # Only validate if breed was provided
            self.breed = breed

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not (1 <= len(value) <= 25):
            print("Name must be string between 1 and 25 characters.")
        else:
            self._name = value

    @property
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, value):
        if value not in self.APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = value