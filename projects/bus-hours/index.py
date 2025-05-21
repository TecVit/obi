# 1º Passo - Linhas de Onibus
# Horários do Onibus X
# Horários do Onibus Y

# 2º Passo - Horário de referência
# Decidir o horário de pegar o onibus e fazer a integração
# (Horário) obrigatóriamente tem que ser maior ou igual ao horário atual
# Escolher um tempo de referência que vai demorar para concluir a linha do Onibus X

# 3º Passo - Horários de integração
# Pegar os horários de integração que estão entre o horário de referência e o horário de chegada do onibus X
# (Horário) obrigatóriamente tem que ser maior ou igual ao horário de referência

def hoursAndMinutes(minutes):
    hours = minutes // 60
    minutes = minutes % 60

    return f'{hours}:{0 if minutes < 10 else ''}{minutes}'

def main():

    # 1º Passo - Linhas de Onibus

    indaia = [
        300, 325, 350, 375, 400, 425, 450, 475, 500, 525,
        550, 582, 614, 646, 678, 710, 742, 774, 806, 838,
        870, 902, 927, 952, 977, 1002, 1027, 1052, 1077, 1102,
        1135, 1185, 1245, 1305, 1365, 1420
    ]

    shopping = [
        334, 359, 384, 409, 434, 464, 499, 519, 539, 571,
        603, 634, 666, 698, 730, 762, 794, 826, 858, 890,
        922, 954, 987, 1012, 1037, 1062, 1087, 1117, 1142, 1177,
        1212, 1247, 1282, 1317, 1354, 1394
    ]

    i = 14
    horario_referencia = indaia[i]

    tempo_referencia = 30

    print(f"Indaia: {hoursAndMinutes(horario_referencia)}")
    
    horario_indaia = horario_referencia

    times = [m - horario_indaia for m in shopping if m >= horario_indaia + tempo_referencia]
    horario_shopping = times[0]

    proximo = hoursAndMinutes(horario_indaia + horario_shopping)
    print(f"Próximo Shopping: {proximo}")

    return 0

if __name__ == "__main__":
    main()