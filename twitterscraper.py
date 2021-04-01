import twint
import os

##EDIT LINE 113 OF URL.PY IN TWINT SOURCE CODE TO FIX LANGUAGE BUG

def configure(location):
    c = twint.Config()
    c.Search = "#angry"
    c.Show_hashtags = True
    c.Store_csv = True
    if os.path.exists("Election/" + location + "/tweets.csv"):
        os.remove("Election/" + location + "/tweets.csv")
    c.Output = "Election/" + location
    c.Near = location
    c.Limit = 200
    c.Lang = "en"
    return c

def search(c):
    twint.run.Search(c)

def locations():
    locs = [
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
    "North Dakota",
    "Ohio",
    "Oklahoma",
    "Oregon",
    "Pennsylvania",
    "Rhode Island",
    "South Carolina",
    "South Dakota",
    "Tennessee",
    "Texas",
    "Utah",
    "Vermont",
    "Virginia",
    "Washington",
    "West Virginia",
    "Wisconsin",
    "Wyoming"]
    return locs

# create CSV containing sample data from tiwtter
location = "Houston"
locs = locations()
c = configure(location)
search(c)

