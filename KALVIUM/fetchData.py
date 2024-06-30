import requests
from bs4 import BeautifulSoup


def fetchAndSaveToFile(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)


maiUrl = "https://results.eci.gov.in/"
APnSKurl = "https://results.eci.gov.in/AcResultGen2ndJune2024/index.htm"
ByeUrl = "https://results.eci.gov.in/AcResultByeJune2024/index.htm"
PCurl = "https://results.eci.gov.in/PcResultGenJune2024/index.htm"
APnODurl = "https://results.eci.gov.in/AcResultGenJune2024/index.htm"
fetchAndSaveToFile(APnODurl, "data/AndhraNOdisha.html")
fetchAndSaveToFile(PCurl, "data/Constituencies.html")
fetchAndSaveToFile(ByeUrl, "data/ByeElectionResults.html")
fetchAndSaveToFile(APnSKurl, "data/APnSK.html")
fetchAndSaveToFile(maiUrl, "data/ecoi.html")