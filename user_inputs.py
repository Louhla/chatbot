def check_inputs(user_message):
    if user_message.find('?') is not -1:
        boto_message = 'this is an interesting question'
        return json.dumps({"animation": "dancing", "msg": boto_message})
    elif any(word in user_message for word in ['hate', 'ass', 'shit', 'fuck']):
        boto_message = 'We dont use this kind of words here. This should be a safe space.'
        return json.dumps({"animation": "confused", "msg": boto_message})