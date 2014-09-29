#!/usr/bin/env python3

"""
Solitaire is an output-feedback mode stream cipher. Invented by Bruce Schneier
and popularized by Neal Stephenson. Described in Schneiers words
https://www.schneier.com/solitaire.html

Commandline usage:

$ python3 solitaire.py -e message.txt key.txt

$ python3 solitaire.py -d message.txt key.txt

-e == --encrypt
-d == --decrypt

key.txt file optional but recommended, it ommitted it will be generated using a
weak pseudo random number generator.

Library usage:

solitaire = Solitaire() # Key is automatically generated
print solitaire.get_key()
msg = 'Mary had a little lamb'
enc_msg = solitaire.encrypt(msg)
dec_msg = solitaire.decrypt(enc_msg)
assert ''.join.split(msg.upper()) == ''.join.split(dec_msg)
"""
import argparse


class Solitaire():
    """Output-feedback mode stream cypher designed around a deck of cards."""
    def __init__(self, key=None):
        if key and self._valid_key(key):
            self.key = tuple(key)
        else:
            self.key = self.generate_key()
        self.deck = self.key

    def generate_key(self):
        """Uses pseudo random number generator to create inferior keys for the
        lazy, also emits warning recommending the user to go shuffle a pack of
        cards.
        """
        pass

    def _valid_key(self):
        """Returns True is key is valid else false."""
        pass

    def input_key():
        """A facilitated method of inputing the key, taking each card one at a
        time and fuzzy matching and validating the set in real time.
        """
        pass

    def get_key(self):
        """Returns the key in list form."""
        return self.key

    def _enumerate(self, st):
        """Capitalize and convert a string into a list of numbers,
        A=1, B=2 etc
        """
        pass

    def _characterize(self, li):
        """Contert list of numbers to letters, 1=A, 2=B etc convert to a
        string, stick with 5 character groups.
        """
        pass

    def _solitaire(self):
        pass

    def encode(self, msg):
        pass

    def decode(self, msg):
        pass


class TestSolitaire():
    def test_generate_key():
        pass

    def test_get_key():
        pass

    def test_encode():
        pass

    def test_decode():
        pass

if __name__ == '__main__':
    # parse arguments for command line usage
    parser = argparse.ArgumentParser()
    parser.parse_args()
