violator_songs = [
    ['World in My Eyes', 4.86],
    ['Sweetest Perfection', 4.43],
    ['Personal Jesus', 4.56],
    ['Halo', 4.9],
    ['Waiting for the Night', 6.07],
    ['Enjoy the Silence', 4.20],
    ['Policy of Truth', 4.76],
    ['Blue Dress', 4.29],
    ['Clean', 5.83]
]
time_songs = 0
count_sons = int(input('Сколько песен выбрать? '))

# TODO, как реализовать range таким образом, чтобы не производить в цикле вычисления (+1) с переменной цикла?
#  В таком случае, вычисление произойдёт только 1 раз в range, вместо вычислений каждую итерацию цикла.
for i in range(count_sons):
    print('Название', i + 1, ' песни ')
    songs_title = input()
    for i_songs in violator_songs:
        if i_songs[0] == songs_title:
            time_songs += i_songs[1]
            # TODO, если песня найдена, из вложенного цикла стоит выйти,
            #  таким образом, сократим количество лишних итераций. Что позволит ускорить код.

print('Общее время звучания песен: ', time_songs)
