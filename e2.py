import requests
from bs4 import BeautifulSoup as bs

for line in open("ELECTION_ID"):
    year=line.split()
    addr = "http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/".format(year[1])
    resp = requests.get(addr)
    soup = bs(resp.content, "html.parser")
    name = year[0] +".csv"
    with open(name, "w") as out:
        out.write(resp.text)
