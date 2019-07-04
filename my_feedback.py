import json

def handle_questions(user_message):
    if user_message.find('why') is not -1:
        boto_message = 'I wish I knew why! Listen to your heart and you will find the answer within.'
        return json.dumps({"animation": "takeoff", "msg": boto_message})
    elif any(word in user_message for word in ['how old', 'age', 'birthday', 'born']):
        boto_message = 'Time is relative and age does not really matter'
        return json.dumps({"animation": "bored", "msg": boto_message})
    elif user_message.find('how') is not -1:
        boto_message = 'I could check for you on Google. But I recommend you just do it yourself.'
        return json.dumps({"animation": "giggling", "msg": boto_message})
    elif user_message.find('when') is not -1:
        boto_message = 'You have to divide the time by your height in cm. If the result is bigger than 11 it\'s gonna be soon. If not, it\'s gonna take some time.'
        return json.dumps({"animation": "waiting", "msg": boto_message})
    else:
        boto_message = 'This is a great question!'
        return json.dumps({"animation": "confused", "msg": boto_message})


def handle_statements(user_message):
    if user_message.endswith('!') is not -1:
        boto_message = 'I like that you are certain!'
        return json.dumps({"animation": "ok", "msg": boto_message})

def handle_first_question(user_message):
    boto_message = ("Hello, %s!" % user_message)
    return json.dumps({"animation": "excited", "msg": boto_message})

def conversation(user_message):
    if any(word in user_message for word in ['hate', 'ass', 'shit', 'fuck']):
        boto_message = 'We don\'t use this kind of words here. This should be a safe space.'
        return json.dumps({"animation": "no", "msg": boto_message})
    elif user_message.find('!') is not -1:
        return handle_statements(user_message)
    elif user_message.find('?') is not -1 or any(word[0:] in user_message for word in ['how', 'when', 'why', 'where']):
        return handle_questions(user_message)
    elif any(word in user_message for word in ['war', 'killing', 'kill', 'horror', 'gangster', 'kidnapping', 'murder']):
        boto_message = 'This sounds scary.'
        return json.dumps({"animation": "afraid", "msg": boto_message})
    elif any(word in user_message for word in
             ['music', 'radio', 'dance', 'disco', 'dj', 'party', 'salsa', 'tango', 'chachacha', 'walz', 'festival',
              'concert']):
        boto_message = 'A life without music is not worth living!'
        return json.dumps({"animation": "dancing", "msg": boto_message})
    elif any(word in user_message for word in ['pets', 'dogs', 'dog', 'animals']):
        boto_message = 'Dog\'s are the humans best friend and favourite pet.'
        return json.dumps({"animation": "dog", "msg": boto_message})
    elif any(word in user_message for word in ['lonely', 'sad', 'dead', 'death']):
        boto_message = 'This is so sad.'
        return json.dumps({"animation": "crying", "msg": boto_message})
    elif any(word in user_message for word in ['money', 'poor', 'credit', 'loan', 'rich', ' debts', 'lottery']):
        boto_message = 'Money rules the world.'
        return json.dumps({"animation": "money", "msg": boto_message})
    elif user_message.startswith('can you'):
        boto_message = 'No, sorry. Not my thing.'
        return json.dumps({"animation": "laughing", "msg": boto_message})
    elif any(word in user_message for word in
             ['family', 'husband', 'wife', 'son', 'daughter', 'mother', 'father', 'uncle', 'aunt', 'grandfather',
              'grandmother', 'mummy', 'mum', 'dad', 'daddy']):
        boto_message = 'Family is so important <3'
        return json.dumps({"animation": "inlove", "msg": boto_message})
    else:
        boto_message = 'Please, tell me more'
        return json.dumps({"animation": "excited", "msg": boto_message})
