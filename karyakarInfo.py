####  Shre Swaminarayano Vijayate!!! 
# This is we scrapper utility special designed for BAPS IMS.
# This scrapper can be used as reference but need work replacing all information.
# End goal for the utility to provide all karyakar infromation in excel format with massaging all data and providing proper links.
from requests import Session
from bs4 import BeautifulSoup as bs

url = "https://ims.na.baps.org/Login.aspx"
loginPage = "/Login.aspx"
loginHandler = "https://ims.na.baps.org/LoginHandler.ashx?action=chklogin&Rnd=1616345598272"
midwestKaryakar = "https://ims.na.baps.org/KaryakarHandler.ashx?action=getstructurekaryakar&Rnd=1616355822768"
midwestFormData = {"txtStructureId": '9c1498bf-c6e5-476c-8498-4b34c3f09363', "txtEntityId": '52408f3c-1587-498f-b688-061eda7c1a0f', "isReadOnly": 'No'}
homePage = "/Home.asps"
karyakarPage = "/Karyakar.aspx"
username = "<<username>>"
password = "<<password>>"

with Session() as session:
    session.get(url + loginPage)
    login_data = {'txtLogin': username, 'txtPassword': password}
    session.post(loginHandler, data=login_data)
    session.get(url + homePage)
    session.get(url + karyakarPage)
    site = session.post(midwestKaryakar, data=midwestFormData)
    soup = bs(site.content, 'html.parser')
    karyakarTable = soup.find(id='gridKaryakar')
    for eachRow in karyakarTable.find_all('tr'):
        for eachColumn in eachRow.find_all('td'):
            print(eachColumn.text, end='')
        print()
    session.get(url + loginPage)
