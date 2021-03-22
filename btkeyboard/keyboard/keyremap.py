from keymap import keytable

KEY_LEFTSHIFT = 2
KEY_RIGHTSHIFT = 32
KEY_BOTHSHIFT = KEY_LEFTSHIFT | KEY_RIGHTSHIFT
SHIFT_POSTFIX = ' S'
KEY_LEFTALT = 4
KEY_RIGHTALT = 64
KEY_BOTHALT = KEY_LEFTALT | KEY_RIGHTALT
ALT_POSTFIX = ' A'

remaptable = {
    # ROW 1
    "KEY_GRAVE": "KEY_LEFTBRACE S",     # `
    "KEY_EQUAL": "KEY_MINUS S",         # =
    # ROW 1 ALT
    "KEY_GRAVE A": "KEY_GRAVE",         # `+ALT
    # ROW 1 SHIFT
    "KEY_GRAVE S": "KEY_EQUAL S",       # ~
    "KEY_2 S": "KEY_LEFTBRACE",         # @
    "KEY_6 S": "KEY_EQUAL",             # ^
    "KEY_7 S": "KEY_6 S",               # &
    "KEY_8 S": "KEY_APOSTROPHE S",      # *
    "KEY_9 S": "KEY_8 S",               # (
    "KEY_0 S": "KEY_9 S",               # )
    "KEY_MINUS S": "KEY_RO S",          # _
    "KEY_EQUAL S": "KEY_SEMICOLON S",   # +
    # ROW 2
    "KEY_LEFTBRACE": "KEY_RIGHTBRACE",  # [ 
    "KEY_RIGHTBRACE": "KEY_BACKSLASH",  # ]
    "KEY_BACKSLASH": "KEY_RO",          # \ 
    # ROW 2 SHIFT
    "KEY_LEFTBRACE S": "KEY_RIGHTBRACE S",  # { 
    "KEY_RIGHTBRACE S": "KEY_BACKSLASH S",  # }
    "KEY_BACKSLASH S": "KEY_YEN S",         # |
    # ROW 2
    "KEY_APOSTROPHE": "KEY_7 S",            # '
    # ROW 3 SHIFT
    "KEY_SEMICOLON S": "KEY_APOSTROPHE",    # :
    "KEY_APOSTROPHE S": "KEY_2 S",          # '
}


def remap(mod_keys, pressed_keys):

    shift = SHIFT_POSTFIX if (mod_keys & KEY_BOTHSHIFT) else ''
    alt = ALT_POSTFIX if (mod_keys & KEY_BOTHALT) else ''
    # print('rmap', mod_keys, pressed_keys)
    pressed_key = pressed_keys[0]
    key = reverse_key_list[pressed_key]
    keyshift = key + alt + shift
    if keyshift not in remaptable:
        return mod_keys, [pressed_key, 0, 0, 0, 0, 0]
    else:
        rkey = remaptable[keyshift]
        print('rmap-keyshift', keyshift, 'rkey', rkey)
        if rkey.endswith(SHIFT_POSTFIX):
            mod_keys |= KEY_LEFTSHIFT
            pressed_rkey = keytable[rkey[:-2]]
        else:
            mod_keys &= ~KEY_BOTHSHIFT
            pressed_rkey = keytable[rkey]
        #print('rmap-rkey', pressed_rkey)
        return mod_keys, [pressed_rkey, 0, 0, 0, 0, 0]


reverse_key_list = [0] * 256


def initialize_reverse_key_list():
    global keytable
    for key in keytable:
        reverse_key_list[keytable[key]] = key


initialize_reverse_key_list()

