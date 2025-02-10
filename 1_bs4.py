from bs4 import BeautifulSoup

with open("flipkart.html","r") as f:
    html = f.read()
soup = BeautifulSoup(html , 'html.parser')

print("Title of the page is: ", soup.title.text)
print("All Tags: ", soup.find_all("a"))
print("Title string: ", soup.title.string)
print("Title parent name: ", soup.title.parent.name)
print("All links:", soup.find_all("a")) 