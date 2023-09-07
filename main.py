import urllib
import http.cookiejar

URL = 'https://online.ukrsibbank.com/ibank/'
def extract_cookies():
        cookie_jar = http.cookiejar.CookieJar()

        url_opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cookie_jar))
        url_opener.open(URL)
        for cookie in cookie_jar:
            print("[Cookie Name = %s] -- [Cookie_Value = %s]" %(cookie.name , cookie.value))

if __name__== '__main__':
    extract_cookies()
