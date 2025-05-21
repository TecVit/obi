def hoursAndMinutes(minutes):
    hours = minutes // 60
    minutes = minutes % 60

    return f'{hours}:{minutes}'

def main():
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

    i = int(input())

    # Tempos (minutos) que se leva para chegar do Indaia para o Terminal / Centro
    tempo_ate_o_terminal = 30

    print(f"Indaia: {hoursAndMinutes(indaia[i])}")
    indaia = indaia[i]
    times = [m - indaia for m in shopping if m >= indaia + tempo_ate_o_terminal]
    terminal = times[0]

    proximo = hoursAndMinutes(indaia + terminal)
    print(f"Próximo Shopping: {proximo}")

    return 0

if __name__ == "__main__":
    main()