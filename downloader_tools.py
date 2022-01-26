import webbrowser

def font_downloader():
    font = ""
    wfont = ""
    company = ""
    company = input('please enter company aaa/fm \n')
    font = input('please enter font \n')
    wfont = input('please enter weight font \n')
    if company == "aaa":
        webbrowser.open("https://alefalefalef.co.il/wp-content/fonts/" + font + "/" + font + "-" + wfont + "-aaa.woff2")
    elif company == "fm":
        webbrowser.open("https://fontimonim.co.il/wp-content/fonts/" + font + "/" + font + "-" + wfont + "-fm.woff2")

def game_downloader():
    steamunlocked = "https://steamunlocked.net/?s="
    gamestorrents = "https://www.gamestorrents.fm/?s="
    agfy = "https://agfy.co/?s="
    game = ""
    google = "https://www.google.com/search?q="
    game = input('enter name of game \n')
    steamunlocked += game
    gamestorrents += game
    agfy += game
    google += game

    webbrowser.open(steamunlocked)
    webbrowser.open(gamestorrents)
    webbrowser.open(agfy)
    webbrowser.open(google)

def app_downloader():
    allsoftwares = "https://allsoftwares.co/?s="
    igetintopc = "https://igetintopc.com/?s="
    app = ""
    google = "https://www.google.com/search?q="
    app = input('enter name of app \n')
    igetintopc += app
    allsoftwares += app
    google += app

    webbrowser.open(igetintopc)
    webbrowser.open(allsoftwares)
    webbrowser.open(google)

def media_downloader():
    def movies():
        base="https://torrentgalaxy.to/torrents.php?search="
        movies=input('please enter name of movie\n')
        webbrowser.open(base+movies+"#results")
    def series():
        # galaxy="https://torrentgalaxy.to/torrents.php?search="
        sdarotv="https://sdarot.tv/search?term="
        series=input('please enter name of series\n')
        webbrowser.open(sdarotv+series)
        # webbrowser.open(galaxy+series+"#results")
    print("[1] movies")
    print("[2] series")
    str1 = input('enter num of  project  \n')
    if str1 == "1":
        movies()
    if str1 == "2":
        series()

print("[1] font_downloader")
print("[2] game_downloader")
print("[3] app_downloader")
print("[4] media_downloader")
str1 = input('enter num of  project  \n')
if str1=="1":
    font_downloader()
if str1=="2":
    game_downloader()
if str1=="3":
    app_downloader()
if str1=="4":
    media_downloader()
