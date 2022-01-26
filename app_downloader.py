import webbrowser

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