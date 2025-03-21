numbers = int(input())
time = 0

# Amigos
friends = {}

# -1 não exite o amigo
# 0 ou mais: existe o amigo e ele esta esperando x segundos
time_friends = [-1 for _ in range(100)]

# 0 ele não recebeu
# 1 ele recebeu
type_friends = [0 for _ in range(100)]

# editar depois
def sumTime(friends):
    return 0

for i in range(numbers):
    input_str = str(input())
    type, friend = input_str.split()
    type, friend = str(type), int(friend)
    
    
    
    if (type == 'R'):
        type_friends[friend] = 1
        time_friends[friend] = 0
    elif (type == 'E'):
        type_friends[friend] = 0
        
    # continuacao...
        
    
    if (time_friends[friend] == -1):
        time_friends[friend] = 0
    else:
        time_friends[friend] += 1
    
    
