# Bob is a lackadaisical teenager. In conversation, his responses are very limited.
# Bob answers 'Sure.' if you ask him a question, such as "How are you?".
# He answers 'Whoa, chill out!' if you YELL AT HIM (in all capitals).
# He answers 'Calm down, I know what I'm doing!' if you yell a question at him.
# He says 'Fine. Be that way!' if you address him without actually saying anything.
# He answers 'Whatever.' to anything else.
# Bob's conversational partner is a purist when it comes to written communication and
# always follows normal rules regarding sentence punctuation in English.

def is_question(message: str) -> bool:
    return message.endswith('?')

def is_yell(message: str) -> bool:
    return message.isupper()

def is_empty(message: str) -> bool:
    return message == ''

def response(hey_bob: str) -> str:

    hey_bob = hey_bob.strip()

    if is_question(hey_bob):
        if is_yell(hey_bob):
            return 'Calm down, I know what I\'m doing!'
        else:
            return 'Sure.'

    if is_yell(hey_bob):
        return 'Whoa, chill out!'

    if is_empty(hey_bob):
        return 'Fine. Be that way!'
        
    return 'Whatever.'