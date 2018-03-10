# -*- coding: utf-8 -*-
'''
A state module to manage emoji files
.. code-block:: yaml
    /tmp/happy:
      emoji.present:
        - emotion: happy
    /tmp/sad:
      emoji.present:
        - emotion: sad
'''

def present(name, emotion):
    '''
    Ensure an emoji is present on the file system

    name
        Path to file containing emoji
    emotion
        Name of emotion
    '''
    ret = {
        'changes': {},
        'comment': '',
        'name': name,
        'result': False
    }

    # Validate emotion
    if __salt__['emojify.get_emoji_for_emotion'](emotion) is None:
        valid_emotions = __salt__['emojify.get_valid_emotions']()
        ret['comment'] = '{} is not one of {}'.format(emotion, valid_emotions)
        return ret

    # Get existing resource
    target = __salt__['emojify.get_emoji'](name)

    if target is not None:
        state_emoji = __salt__['emojify.get_emoji_for_emotion'](emotion)
        # Compare desired state with actual state
        if target != state_emoji:
            # Update
            result = __salt__['emojify.write_emoji'](name, emotion)
            if result:
                ret['changes']['old'] = target
                ret['changes']['new'] = state_emoji
                ret['comment'] = '{} updated'.format(name)
                ret['result'] = True
            else:
                ret['comment'] = 'Failed to update'
        else:
            ret['comment'] = "Already up to date"
            ret['result'] = True
    else:
        # Create new emoji
        result = __salt__['emojify.write_emoji'](name, emotion)
        if result:
            ret['changes']['old'] = target
            ret['changes']['new'] = emotion
            ret['comment'] = '{} updated'.format(name)
            ret['result'] = True
        else:
            ret['comment'] = 'Failed to update'
    return ret

def absent(name):
    '''
    Ensure an emoji is removed from the file system

    name
        Path to file containing emoji
    '''
    ret = {
        'changes': {},
        'comment': '',
        'name': name,
        'result': False
    }
    # Get existing resource
    target = __salt__['emojify.get_emoji'](name)

    if target is not None:
        # Delete it
        result = __salt__['emojify.delete_emoji_file'](name)
        if result:
            ret['changes']['old'] = target
            ret['changes']['new'] = None
            ret['comment'] = '{} deleted'.format(name)
            ret['result'] = True
        else:
            ret['comment'] = 'Failed to delete'
    else:
        # Already deleted
        ret['comment'] = '{} already deleted'.format(name)
        ret['result'] = True
    return ret
