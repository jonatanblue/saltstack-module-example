# -*- coding: utf-8 -*-
'''
A state module to manage emoji files
.. code-block:: yaml
    /tmp/happy:
      emojify.present:
        - emotion: happy
    /tmp/sad:
      emojify.present:
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
    # Get emoji
    state_emoji = __salt__['emojify.get_emoji_for_emotion'](emotion)

    # Validate emotion
    if state_emoji is None:
        valid_emotions = __salt__['emojify.get_valid_emotions']()
        ret['comment'] = '{} is not one of {}'.format(emotion, valid_emotions)
        return ret

    # Get existing resource
    target = __salt__['emojify.get_emoji'](name)

    if target is not None:
        # Compare desired state with actual state
        if target != state_emoji:
            # Return if test
            if __opts__['test']:
                ret['comment'] = 'The emoji {} is set to be changed.'.format(name)
                ret['result'] = None
                return ret
            # Update
            result = __salt__['emojify.write_emoji'](name, emotion)
            if result:
                ret['changes']['old'] = target
                ret['changes']['new'] = state_emoji
                ret['comment'] = 'Emoji {} updated'.format(name)
                ret['result'] = True
            else:
                ret['comment'] = 'Failed to update'
        else:
            ret['comment'] = "Already up to date"
            ret['result'] = True
    else:
        # Return here if test
        if __opts__['test']:
            ret['comment'] = 'The emoji {} is set to be created.'.format(name)
            ret['result'] = None
            return ret
        # Create new emoji
        result = __salt__['emojify.write_emoji'](name, emotion)
        if result:
            ret['changes']['diff'] = "New file"
            ret['comment'] = 'Emoji {} created'.format(name)
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
        # Return here if test
        if __opts__['test']:
            ret['comment'] = 'The emoji {} is set to be deleted.'.format(name)
            ret['result'] = None
            return ret
        # Delete it
        result = __salt__['emojify.delete_emoji_file'](name)
        if result:
            ret['changes']['diff'] = "Deleted emoji {}".format(name)
            ret['comment'] = '{} deleted'.format(name)
            ret['result'] = True
        else:
            ret['comment'] = 'Failed to delete'
    else:
        # Already deleted
        ret['comment'] = 'The emoji {} is not present'.format(name)
        ret['result'] = True
    return ret
