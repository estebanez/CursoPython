#Used to make requests
import urllib.request

x = urllib.request.urlopen('https://www.movistar.es/')
print(x.read())

