import os
import pickle
from MainMenu import Menu
from BusCompany import BestBusCompany

if __name__ == '__main__':
    if not os.path.exists('bus_company.pickle'):
        bus_company = BestBusCompany()
        print("created new company")
    else:
        # this is not the first time - we already have a DB
        # with data from the previous runs
        with open('bus_company.pickle', 'rb') as fh:
            bus_company = pickle.load(fh)
            print("loading from existing bus company...")
    try:
        Menu(bus_company).run()

    except Exception as e:
        print(e)
        with open('bus_company.pickle', 'wb') as fh:
            pickle.dump(bus_company, fh)
            print("saved company data")
