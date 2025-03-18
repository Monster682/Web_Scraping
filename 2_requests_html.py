from requests_html import HTMLSession

session = HTMLSession()

r = session.get('https://python.org/')

print(r.html.json())
