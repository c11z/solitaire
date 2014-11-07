# Solitaire

Solitaire is an output-feedback mode stream cipher. Invented by Bruce Schneier
and popularized by Neal Stephenson. Described in Schneiers words:
https://www.schneier.com/solitaire.html

This library has the basic functionality that Schneier describes in his article. It allows you to specify a key or generate a key from a passphrase, then provides encode and decode methods. The encode method can include non-alpha characters which are stripped out but obviously the decode method will only be able to output the messages in five character groups. If the passphrase is less than 64 characters it will print a warning message.

"Warning: There are only 1.4 bits of randomness per character in standard English. Please use at least a 64 character passphrase."

## Usage:

```
passphrase = 'cryptonomicon'
solitaire = Solitaire(passphrase=passphrase)
print(solitaire.get_key())
print(solitaire.get_deck())
msg = 'Oh Mary had a little lambabcde'
enc\_msg = solitaire.encode(msg)
dec\_msg = solitaire.decode(enc_msg)
assert ''.join(msg.upper().split()) == ''.join(dec_msg.split())
```

## Hello Hacker School
This library was written as an example of programming prowess for my Hacker School application. In that regard I had to walk a fine line between effort, charm and performance. You should not use this for real spycraft. It is simply not tested rigorously enough.

## Testing
Run tests in command line by:
```
? py.test solitaire.py
```
