import openai
import os

openai.api_key  = os.getenv('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-3.5-turbo-16k-0613"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

from bs4 import BeautifulSoup
import urllib.request

fp = urllib.request.urlopen("https://help.klocwork.com/current/en-us/concepts/javacheckerreference.htm")
mybytes = fp.read()
mystr = mybytes.decode("utf8")
fp.close()
soup = BeautifulSoup(mystr, 'html.parser')
rs=soup.find_all("a",class_="xref")
#print(soup.find("a",class_="xref")["href"])
url="https://help.klocwork.com/current/en-us/reference/"
i=1
j=0
checkers=''
for a in rs:
    j=j+1
    checker_url=url+a["href"].replace("../reference/","")
    fpp = urllib.request.urlopen(checker_url)
    mybytes = fpp.read()
    mystr = mybytes.decode("utf8")
    fpp.close()
    soup = BeautifulSoup(mystr, 'html.parser')
    title = soup.title
    #print(soup.find("p",_class="p"))
    paragraphs = soup.find_all('p')
    #checkers = checkers + "{} Checker: {}".format(i, title.text)
    if j%4==0:
        checkers=checkers + str(i)+"."+title.text+":"
        for p in paragraphs:
            checkers = checkers + " " + p.text
        checkers += "\n"
        i=i+1