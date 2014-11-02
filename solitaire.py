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
import pytest


class Solitaire():
    """Output-feedback mode stream cypher designed around a deck of cards."""

    def __init__(self, key=None):
        if key and self._valid_key(key):
            self.key = tuple(key)
        else:
            self.key = self.generate_key()
        self.deck = list(self.key)
        self.J0 = 53
        self.J1 = 54

    def generate_key(self):
        """Uses pseudo random number generator to create inferior keys for the
        lazy, also emits warning recommending the user to go shuffle a pack of
        cards.
        """
        return range(1, 55)

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
        conv = {1: 'AC', 2: '2C', 3: '3C', 4: '4C', 5: '5C', 6: '6C', 7: '7C',
                8: '8C', 9: '9C', 10: '10C', 11: 'JC', 12: 'QC', 13: 'KC',
                14: 'AD', 15: '2D', 16: '3D', 17: '4D', 18: '5D', 19: '6D',
                20: '7D', 21: '8D', 22: '9D', 23: '10D', 24: 'JD', 25: 'QD',
                26: 'KD', 27: 'AH', 28: '2H', 29: '3H', 30: '4H', 31: '5H',
                32: '6H', 33: '7H', 34: '8H', 35: '9H', 36: '10H', 37: 'JH',
                38: 'QH', 39: 'KH', 40: 'AS', 41: '2S', 42: '3S', 43: '4S',
                44: '5S', 45: '6S', 46: '7S', 47: '8S', 48: '9S', 49: '10S',
                50: 'JS', 51: 'QS', 52: 'KS', 53: 'J0', 54: 'J1'}

        result = []
        for i in self.key:
            result.append(conv[i])
        return result

    def _enumerate(self, plain_text):
        """Capitalize and convert a string into a list of numbers,
        A=1, B=2 etc
        """
        char_list = []
        for character in list(plain_text):
            num = ord(character)
            if 65 <= num <= 90:  # This is a capital alpha character
                # (-)65 to normalize so that modulo 26 works.
                char_list.append(num - 64)
            elif 97 <= num <= 122:  # This is a lower alpha character
                # (-)32 for conversion to a capital letter and (-)65 for
                # normailization
                char_list.append(num - 32 - 64)
            # else this is a non alpha and is ignored.
        # Pad message with X's (23) for groups of 5
        if (len(char_list) % 5) != 0:
           char_list += [23] * (5 - (len(plain_text) % 5))
        return char_list

    def _characterize(self, char_list):
        """Convert list of numbers to letters, 1=A, 2=B etc convert to a
        string, stick with 5 character groups.
        """
        plain_text = ''
        for i in char_list:
            # Add back 65 to map into capital alpha characters.
            plain_text += chr(i + 64)
        plain_text = ' '.join(plain_text[i:i + 5] for i in range(0, len(plain_text), 5))
        return plain_text

    def _scramble(self, i, key):
        """"Takes the integer representation of a character of the plaintext
        message {i} and performs the addition modulo 26 step with the keystream
        modifier {key}.
        """
        if key > 26:
            key -= 26
        value = i + key
        if value > 26:
            value -= 26
        return value

    def _clarify(self, i, key):
        """Takes the integer representation of a character of the encoded
        message {i} and performs the subtraction modulo 26 step with the
        keystream modifier {key}.
        """
        if key > 26:
            key -= 26
        value = i - key
        if value < 1:
            value += 26
        return value

    def _move_card(self, card, places):
        """Moves card in deck a certain number of places, card wraps around
        deck if it goes past the end.
        """
        index = self.deck.index(card)
        new_index = index + places
        if new_index > 53:
            new_index -= 53
        self.deck.insert(new_index, self.deck.pop(index))

    def _triple_cut(self):
        """Determine cutpoints by isolating cards before the first joken and
        after the second find top, middle and bottom of deck. Then swap top
        and bottom.
        """
        #Determine cut points
        j0_index = self.deck.index(self.J0)
        j1_index = self.deck.index(self.J1)
        cut_point1 = min(j0_index, j1_index)
        cut_point2 = max(j0_index, j1_index) + 1
        top = self.deck[:cut_point1]
        middle = self.deck[cut_point1:cut_point2]
        bottom = self.deck[cut_point2:]
        self.deck = bottom + middle + top

    def _count_cut(self):
        """Look at the bottom card cound down from the top card that number,
        cut after that card leaving the bottom card on the bottom. If the
        bottom card is a joker do nothing.
        """
        if self.deck[-1] == self.J0 or self.deck[-1] == self.J1:
            return
        else:
            bottom_card = self.deck.pop()
            # Nobody likes an out of range index; treat J1 like J0.
            if bottom_card == self.J1:
                cut_point = self.J0
            else:
                cut_point = bottom_card
            # Count down from bottom card but cut after that point.
            top, bottom = self.deck[:cut_point], self.deck[cut_point:]
            self.deck = bottom + top + [bottom_card]

    def _solitaire(self):
        """Plays the game of solitaire, generating one keystream character."""
        self._move_card(self.J0, 1)
        self._move_card(self.J1, 2)
        self._triple_cut()
        self._count_cut()
        top_card = self.deck[0]
        # Nobody likes an out of range index; treat J1 like J0.
        if top_card == self.J1:
            top_card = self.J0
        key = self.deck[top_card]
        # If the keystream card is a joker then start over from step one.
        if key == self.J0 or key == self.J1:
            return self._solitaire()
        else:
            return key

    def encode(self, msg):
        """Takes a string message and encodes it."""
        enc = []
        for element in self._enumerate(msg):
            key = self._solitaire()
            enc.append(self._scramble(element, key))
        return self._characterize(enc)

    def decode(self, enc):
        """Take a string encoded message and decodes it."""
        msg = []
        for element in self._enumerate(enc):
            key = self._solitaire()
            msg.append(self._clarify(element, key))
        return self._characterize(msg)


class TestSolitaire():
    """Test Class for solitaire program."""

    def test_encode(self):
        """Tests encode method."""
        solitaire = Solitaire()
        msg = 'AAAAA AAAAA'
        enc = solitaire.encode(msg)
        assert enc == 'EXKYI ZSGEH'

    def test_decode(self):
        """Tests Generate key method."""
        solitaire = Solitaire()
        msg = 'EXKYI ZSGEH'
        enc = solitaire.decode(msg)
        assert enc == 'AAAAA AAAAA'

    def test_get_key(self):
        """Tests get key method."""
        solitaire = Solitaire()
        assert range(1, 55) == solitaire.get_key()

    def test_generate_key(self):
        """Tests decode method."""
        pass

if __name__ == '__main__':
    # parse arguments for command line usage
    parser = argparse.ArgumentParser()
    parser.parse_args()
