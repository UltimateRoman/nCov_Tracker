import requests, json, time
import config as c


try:
    response = requests.get(c.url)
    data = json.loads(response.text)
    url1 = "https://corona.lmao.ninja/countries"
    response1 = requests.get(url1)
    data1 = json.loads(response1.text)
    cases = str(data['cases'])
    recovered = str(data['recovered'])
    deaths = str(data['deaths'])
    active = str(int(cases) - int(recovered) - int(deaths))
    print("\nReal time COVID-19 updates")
    print("\nGlobal updates")
    print("\nTotal cases: " + cases)
    print("Active cases: " + active)
    print("Recovered cases: " + recovered)
    print("Deaths: " + deaths + "\n")
    country = input("Enter name of a country: ")
    f = 0
    for a in data1:
        if country == str(a['country']):
            print("\nTotal cases: " + str(a['cases']))
            print("Cases reported today: " + str(a['todayCases']))
            print("\nTotal deaths: " + str(a['deaths']))
            print("Deaths reported today: " + str(a['todayDeaths']))
            print("\nRecovered cases: " + str(a['recovered']))
            print("Critical cases: " + str(a['critical']) + "\n")
            f = 1
    if f != 1:
        print("Sorry, country could not be found!")
    time.sleep(15)


except Exception as e:
    print("Error occured: " + e)
    time.sleep(10)
