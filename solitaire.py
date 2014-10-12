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
        self.deck = list(self.key)
        # Store indexes of jokers so we don't have to look them up all the time
        self.j0_index = self.deck.index(52)
        self.j1_index = self.deck.index(53)

    def generate_key(self):
        """Uses pseudo random number generator to create inferior keys for the
        lazy, also emits warning recommending the user to go shuffle a pack of
        cards.
        """
        return range(54)

    def _valid_key(self, key):
        """Returns True is key is valid else false."""
        pass

    def input_key(self):
        """A facilitated method of inputing the key, taking each card one at a
        time and fuzzy matching and validating the set in real time.
        """
        pass

    def get_key(self):
        """Returns the key in list form."""
        return self.key

    def get_deck(self):
        """Converts the key to a representation that can be used to easily be
        saved as the order of a standard deck of cards.
        """
        conv = {0: 'AC', 1: '2C', 2: '3C', 3: '4C', 4: '5C', 5: '6C', 6: '7C',
                7: '8C', 8: '9C', 9: '10C', 10: 'JC', 11: 'QC', 12: 'KC',
                13: 'AD', 14: '2D', 15: '3D', 16: '4D', 17: '5D', 18: '6D',
                19: '7D', 20: '8D', 21: '9D', 22: '10D', 23: 'JD', 24: 'QD',
                25: 'KD', 26: 'AH', 27: '2H', 28: '3H', 29: '4H', 30: '5H',
                31: '6H', 32: '7H', 33: '8H', 34: '9H', 35: '10H', 36: 'JH',
                37: 'QH', 38: 'KH', 39: 'AS', 40: '2S', 41: '3S', 42: '4S',
                43: '5S', 44: '6S', 45: '7S', 46: '8S', 47: '9S', 48: '10S',
                49: 'JS', 50: 'QS', 51: 'KS', 52: 'J0', 53: 'J1'}

        result = []
        for i in self.key:
            result.append(conv[i])
        return result

    def _enumerate(self, plain_text):
        """Capitalize and convert a string into a list of numbers,
        A=0, B=1 etc
        """
        char_list = []
        for character in list(plain_text):
            num = ord(character)
            if 65 <= num <= 90:  # This is a capital alpha character
                # (-)65 to normalize so that modulo 26 works.
                char_list.append(num - 65)
            elif 97 <= num <= 122:  # This is a lower alpha character
                # (-)32 for conversion to a capital letter and (-)65 for
                # normailization
                char_list.append(num - 32 - 65)
            # else this is a non alpha and is ignored.
        return char_list

    def _characterize(self, char_list):
        """Convert list of numbers to letters, 1=A, 2=B etc convert to a
        string, stick with 5 character groups.
        """
        plain_text = ''
        for i in char_list:
            # Add back 65 to map into capital alpha characters.
            plain_text += chr(i + 65)
        return plain_text

    def _scramble(self, i, key):
        """"Takes the integer representation of a character of the plaintext
        message {i} and performs the addition modulo 26 step with the keystream
        modifier {key}.
        """
        return (i + key) % 26

    def _clarify(self, i, key):
        """Takes the integer representation of a character of the encoded
        message {i} and performs the subtraction modulo 26 step with the
        keystream modifier {key}.
        """
        return (i - key) % 26

    def _solitaire(self):

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
