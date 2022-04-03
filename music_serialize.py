import pickle, json

# Сериализация
sound = {
    'name':'AC/DC',
    'album':'The Razors Edge',
    'year':'1990',
    'tracks':['Thunderstruck', 'Moneytalks'],
    }
with open('new_sound','wb') as f:
    pickle.dump(sound,f)
    
    print('pickle good!')
    
    
with open('new_sound2','w',encoding = 'utf-8') as f:
    new_sound2 = json.dump(sound, f)
    json.dump(sound,f)
    print('json good!') 
