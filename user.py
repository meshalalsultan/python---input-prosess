def sentence (phases):
    q = ('how' , 'what' , 'whare' , 'how')
    capitalized = phases.capitalize()
    if phases.startswith(q):
        return f'{capitalized}?'

    else :
        return f'{capitalized}.'

#print (sentence('what are you today'))


result = []
while True :
    user_input = input('Write something here : ')
    if user_input == '\end':
        break
    else :
        result.append(sentence(user_input))

print(" " .join(result))

