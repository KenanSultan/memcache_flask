import xml.etree.ElementTree as ET
from datetime import date
import requests

def getResp():
    today = date.today()
    day = today.strftime("%d.%m.%Y")
    # url = f"https://www.cbar.az/currencies/{day}.xml"
    url = "https://www.cbar.az/currencies/"+day+".xml"

    result = requests.get(url)

    if result.status_code == 200:
        content = ET.fromstring(result.text)

        return content

    return False