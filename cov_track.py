import requests, json, time
import config as c


response = requests.get(c.url)
data = json.loads(response.text)
response1 = requests.get(c.url1)
data1 = json.loads(response1.text)


def globalrep():
    cases = str(data['cases'])
    recovered = str(data['recovered'])
    deaths = str(data['deaths'])
    active = str(int(cases) - int(recovered) - int(deaths))
    print("\nGenerating global report....")
    print("\nTotal cases: " + cases)
    print("Active cases: " + active)
    print("Recovered cases: " + recovered)
    print("Deaths: " + deaths + "\n")


def countryrep():
    country = input("Enter name of a country: ")
    f = 0
    for a in data1:
        if country == str(a['country']):
            print("Generating report for " + country + "....")
            print("\nTotal cases: " + str(a['cases']))
            print("Cases reported today: " + str(a['todayCases']))
            print("\nTotal deaths: " + str(a['deaths']))
            print("Deaths reported today: " + str(a['todayDeaths']))
            print("\nRecovered cases: " + str(a['recovered']))
            print("Critical cases: " + str(a['critical']) + "\n")
            f = 1
    if f != 1:
        print("Sorry, country could not be found!")

try:
    execute = True
    while execute:
        print("Real-time COVID-19 Tracker")
        print("\nOptions:")
        print("1.Global report")
        print("2.Country-specific report")
        ch = input("\nEnter option: ")
        if ch == '1':
            globalrep()
        elif ch == '2':
            countryrep()
        else:
            print("\nInvalid option entered!")
        con = input("Do u want to continue? ")
        if con == 'y':
            execute = True
        else:
            execute = False


except Exception as e:
    print("Error occured: " + e)
    time.sleep(10)
