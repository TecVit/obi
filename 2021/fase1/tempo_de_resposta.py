# Pontuação = 30 / 100
numbers = int(input())

# Amigos
# Key = Amigo
# Indice 0 do Array = Recebeu a mensagem ou nao (True or False)
# Indice 1 do Array = Segundos Esperados (0, 1, 2, 3...)

friends = {}

# Adiciona 1 segundo para os amigos que estão aguardando a mensagem
def sumTimeFriends(friends):
    for key in friends:
        mensagem = friends[key][0]
        if mensagem == True:
            friends[key][1] += 1
    return friends

for i in range(numbers):
    input_str = str(input())
    type, friend = input_str.split()
    type, friend = str(type), int(friend)

    if (type == 'R'):
        if friend in friends:
            friends[friend][0] = True
        else:
            friends[friend] = [True, 0]
    elif (type == 'E'):
        if friend in friends:
            friends[friend][0] = False
    elif (type == 'T'):
        for key in friends:
            mensagem = friends[key][0]
            if mensagem == True:
                friends[key][1] += friend
        continue
    
    for key in friends:
        mensagem = friends[key][0]
        if mensagem == True and key != friend:
            friends[key][1] += 1

for key in friends:
    if friends[key][0] == True:
        print(key, -1)
    else:
        print(key, friends[key][1])