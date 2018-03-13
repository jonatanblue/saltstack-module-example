# -*- coding: utf-8 -*-
'''
Execution module for creating and deleting emoji files
'''
import os



EMOJIS = {
    "happy": ":D",
    "upset": "D:",
    "crying_laughing": ":'D",
    "speechless": ":|",
    "sad": ":("
}

def get_emoji_for_emotion(emotion):
    '''
    Get the emoji for an emotion

    emotion
        Name of emotion
    '''
    if emotion not in EMOJIS.keys():
        return None
    return EMOJIS[emotion]

def get_valid_emotions():
    '''
    Get list of valid emotions
    '''
    return EMOJIS.keys()

def write_emoji(path, emotion):
    '''
    Write an emoji to file

    path
        Full path to file
    emotion
        Name of emotion
    '''
    with open(path, 'w') as handle:
        handle.write(EMOJIS[emotion])
    return True

def get_emoji(path):
    '''
    Get emoji from file

    path
        Full path to file
    '''
    if os.path.isfile(path):
        with open(path, 'r') as handle:
            return handle.read()
    return None

def delete_emoji_file(path):
    '''
    Delete an emoji file

    path
        Full path to file
    '''
    os.remove(path)
    return True
