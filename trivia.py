import requests

cont = input('Enter \'Y\' if you want to keep playing: ')
while cont == 'Y':
    # request 1 random question from http://jservice.io
    response = requests.get('http://jservice.io/api/random?count=1')
    if not response.status_code:
        print('Something went wrong!!!')
        break
    
    category = response.json()[0]['category']['title']
    ans = response.json()[0]['answer']
    ques = response.json()[0]['question']
    
    # list for answer
    completing = ['_' if x.isalnum() else x for x in ans]
    count = 0
    for x in completing:
        if x == '_':
            count += 1
    to_discover = {ans[0].lower()}
    for x in ans:
        to_discover.add(x.lower())
    
    while True:
        print('Category: {}'.format(category))
        print('Question: {}'.format(ques))
        print(''.join(completing))
        c = input('Enter a letter: ')
        if c == 'skip':
            print('skipping.....')
        if not c or len(c)>1:
            print('Enter just a letter.')
        if c in to_discover:
            to_discover.discard(c)
            for i in range(len(ans)):
                if ans[i].lower() == c.lower():
                    count -= 1
                    completing[i] = ans[i]
            print('It contains {}'.format(c))
        else:
            print('It not contains {}'.format(c))
        if not count:
            print('Congratulations!!!! The answer is {}'.format(ans))
            break


    # keep playing
    cont = input('Enter \'Y\' if you want to keep playing:')