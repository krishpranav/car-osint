#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# imports
import requests
from bs4 import BeautifulSoup as bs
try: 
 print("""
 
 \033[94m     CAR OSINT  \033[0m
                                   
 """)
 
 oplate = input("\033[1mLicense Plate: \033[0m")
 dplate = oplate.upper()
 plate = "".join(oplate.split(" "))
 state = input("\033[1mState: \033[0m")
 state = state.upper()
 
 print("\n\033[93mSearching...\033[0m")
 
 URL = "https://findbyplate.com/US/"+state+"/"+plate+"/"
 
 page = requests.get(URL, verify=True)
 soupPage = bs(page.content, 'html.parser')
 mayresults = soupPage.find("h2", {"class": "vehicle-modal"})
 mayraw = mayresults.prettify().split("\n")[1]
 may = mayraw[1:len(mayraw)]
 
 year = may[0:4]
 model = may[5:len(may)]
 
 countryResults = soupPage.find("div", {"data-title": "PlantCountry"})
 countryResultsraw = countryResults.prettify().split("\n")[1]
 
 country = countryResultsraw[1:len(countryResultsraw)]
 
 countryResults = soupPage.find("div", {"data-title": "PlantCity"})
 countryResultsraw = countryResults.prettify().split("\n")[1]
 city = countryResultsraw[1:len(countryResultsraw)]
 
 vtypeResults = soupPage.find("div", {"data-title": "VehicleType"})
 vtyperaw = vtypeResults.prettify().split("\n")[1]
 type = vtyperaw[1:len(vtyperaw)]
 location = city + ", " + country
 
 print("\033[92mDone!\033[0m\n")
 
 print("\033[1mModel:\033[0m              \033[1mYear:\033[0m" + " " * 7 + "\033[1mVehicle Type:\033[0m")
 print(model + " " * (20 - len(model)) + year + "        " + type)
 print("\n\033[1mPlate Number:\033[0m       \033[1mState:\033[0m      \033[1mPlant Location:\033[0m")
 print(dplate + " " * (20 - len(dplate)) + state + "          " + location)
except KeyboardInterrupt:
  print("\n\033[91mExiting...\033[0m")
except AttributeError:
  print("\033[91mVehicle Not Found\033[0m")
except:
  print("\033[91mError Found, please contact developer\033[0m")
  raise;
