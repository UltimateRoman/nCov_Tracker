import requests, json, time
import config as c


response = requests.get(c.url)
data0 = json.loads(response.text)
response1 = requests.get(c.url1)
data1 = json.loads(response1.text)
response2 = requests.get(c.url2)
data2 = json.loads(response2.text)
response3 = requests.get(c.url3)
data3 = json.loads(response3.text)


def globalrep():
    cases = int(data0['cases'])
    recovered = int(data0['recovered'])
    deaths = int(data0['deaths'])
    active = (cases - recovered - deaths)
    mr = deaths /(recovered + deaths) * 100
    print("\nGenerating global report....")
    print("\nTotal cases:" , cases)
    print("Active cases:" , active)
    print("Recovered cases:" , recovered)
    print("Deaths:" , deaths )
    print("Vague Mortality Rate(among reported cases):" , mr , "\n")


def countryrep():
    country = input("\nEnter name of a country: ")
    f = 0
    for a in data1:
        if country in a.values():
            print("\nGenerating report for " + country + "....")
            cases = int(a['cases'])
            deaths = int(a['deaths'])
            active = int(a['active'])
            recovered = int(a['recovered'])
            critical = int(a['critical'])
            mr = deaths /(recovered + deaths) * 100
            tc = int(a['todayCases'])
            td = int(a['todayDeaths'])
            cpm = int(a['casesPerOneMillion'])
            print("\nTotal cases:" , cases)
            print("Total deaths:" , deaths)
            print("\nActive cases:" , active)
            print("Recovered cases:" , recovered)
            print("Critical cases:" , critical , "\n")
            print("Vague Mortality Rate(among reported cases):" , mr)
            print("\nCases reported today:" , tc)
            print("Deaths reported today:" , td)
            print("\nCases per million of population:" , cpm)
            f = 1
    if f != 1:
        print("Sorry, requested country could not be found!")


def instaterep():
    d2a = data2['data']
    d2b = d2a['regional']
    print("\n*For Union Territories, please include 'Union Territory of' with name*")
    state = input("\nEnter name of a Indian state/UT: ")
    f = 0
    for a in d2b:
        if state in a.values():
            print("\nGenerating report for " + state + "....")
            cci = int(a['confirmedCasesIndian'])
            ccf = int(a['confirmedCasesForeign'])
            discharged = int(a['discharged'])
            deaths = int(a['deaths'])
            mr = deaths / (deaths + discharged) * 100
            print("\nConfirmed cases (Indians):" , cci)
            print("Confirmed cases (Foreigners):" , ccf)
            print("Discharged cases:" , discharged)
            print("Deaths:" , deaths)
            print("\nVague Mortality Rate(among reported cases):" , mr)
            f = 1
    if f != 1:
        print("Sorry, requested state could not be found!")


def usstaterep():
    state = input("\nEnter name of a US state: ")
    f = 0
    for a in data3:
        if state in a.values():
            print("\nGenerating report for " + state + "....")
            cases = int(a['cases'])
            deaths = int(a['deaths'])
            active = int(a['active'])
            recovered = int(a['recovered'])
            mr = deaths / (deaths + recovered) * 100
            tc = int(a['todayCases'])
            td = int(a['todayDeaths'])
            print("\nTotal cases:" , cases)
            print("Total deaths:" , deaths)
            print("\nActive cases:" , active)
            print("Recovered cases:" , recovered)
            print("\nVague Mortality Rate(among reported cases):" , mr)
            print("\nCases reported today:" , tc)
            print("Deaths reported today:" , td)
            f = 1
    if f != 1:
        print("Sorry, requested state could not be found!")
            
    

try:
    execute = True
    while execute:
        print("Real-time COVID-19 Tracker")
        print("\nOptions:")
        print("1.Global report")
        print("2.Country-specific report")
        print("3.State-specific report for India")
        print("4.State-specific report for USA")
        ch = input("\nEnter option: ")
        if ch == '1':
            globalrep()
        elif ch == '2':
            countryrep()
        elif ch == '3':
            instaterep()
        elif ch == '4':
            usstaterep()
        else:
            print("\nInvalid option entered!")
        con = input("\nDo u want to continue?(y to continue): ")
        if con == 'y':
            execute = True
        else:
            execute = False


except Exception as e:
    print("Error occured: ")
    print(e)
    time.sleep(5)
