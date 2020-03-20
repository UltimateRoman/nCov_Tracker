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
    cases = str(data0['cases'])
    recovered = str(data0['recovered'])
    deaths = str(data0['deaths'])
    active = str(int(cases) - int(recovered) - int(deaths))
    print("\nGenerating global report....")
    print("\nTotal cases: " + cases)
    print("Active cases: " + active)
    print("Recovered cases: " + recovered)
    print("Deaths: " + deaths + "\n")


def countryrep():
    country = input("\nEnter name of a country: ")
    f = 0
    for a in data1:
        if country == str(a['country']):
            print("\nGenerating report for " + country + "....")
            cases = str(a['cases'])
            deaths = str(a['deaths'])
            active = str(a['active'])
            recovered = str(a['recovered'])
            critical = str(a['critical'])
            tc = str(a['todayCases'])
            td = str(a['todayDeaths'])
            cpm = str(a['casesPerOneMillion'])
            print("\nTotal cases: " + cases)
            print("Total deaths: " + deaths)
            print("\nActive cases: " + active)
            print("Recovered cases: " + recovered)
            print("Critical cases: " + critical + "\n")
            print("\nCases reported today: " + tc)
            print("Deaths reported today: " + td)
            print("\nCases per million of population: " + cpm)
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
        if state == str(a['loc']):
            print("\nGenerating report for " + state + "....")
            cci = str(a['confirmedCasesIndian'])
            ccf = str(a['confirmedCasesForeign'])
            discharged = str(a['discharged'])
            deaths = str(a['deaths'])
            print("\nConfirmed cases (Indians): " + cci)
            print("Confirmed cases (Foreigners): " + ccf)
            print("Discharged cases: " + discharged)
            print("Deaths: " + deaths)
            f = 1
    if f != 1:
        print("Sorry, requested state could not be found!")


def usstaterep():
    state = input("Enter name of a US state: ")
    f = 0
    for a in data3:
        if state == str(a['state']):
            print("\nGenerating report for " + state + "....")
            cases = str(a['cases'])
            deaths = str(a['deaths'])
            active = str(a['active'])
            recovered = str(a['recovered'])
            tc = str(a['todayCases'])
            td = str(a['todayDeaths'])
            print("\nTotal cases: " + cases)
            print("Total deaths: " + deaths)
            print("\nActive cases: " + active)
            print("Recovered cases: " + recovered)
            print("\nCases reported today: " + tc)
            print("Deaths reported today: " + td)
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
    print("Error occured: " + e)
    time.sleep(10)
