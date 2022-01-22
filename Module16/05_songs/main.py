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

for i in range(1, count_sons + 1):
    print('Название', i, ' песни ')
    songs_title = input()
    for i_songs in violator_songs:
        if i_songs[0] == songs_title:
            time_songs += i_songs[1]
            break

print('Общее время звучания песен: ', time_songs)

# зачёт!
