import webbrowser


def movies():
    base = "https://torrentgalaxy.to/torrents.php?search="
    movies = input('please enter name of movie\n')
    webbrowser.open(base + movies + "#results")


def series():
    # galaxy="https://torrentgalaxy.to/torrents.php?search="
    sdarotv = "https://sdarot.tv/search?term="
    series = input('please enter name of series\n')
    webbrowser.open(sdarotv + series)
    # webbrowser.open(galaxy+series+"#results")


print("[1] movies")
print("[2] series")
str1 = input('enter num of  project  \n')
if str1 == "1":
    movies()
if str1 == "2":
    series()