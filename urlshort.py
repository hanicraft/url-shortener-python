import pyshorteners
url = input("your site here : ")
shortener = pyshorteners.Shortener()
run = shortener.tinyurl.Short(url)
print(run)