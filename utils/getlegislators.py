from flask import Flask, render_template, request, url_for, session, redirect
import sqlite3, json, requests, urllib, urllib2

# ProPublica Congress Data 
PROPUBLICA_URL = "https://api.propublica.org/congress/v1"
API_KEY = json.loads(open("keys.json").read())["propublica"]["API_KEY"]

def data(endpoint, params, headers):
    params_str = urllib.urlencode(params) if params else ""
    req_str = "{}/?{}".format(endpoint, params_str) if params_str else endpoint
    req = urllib2.Request(req_str, None, headers) if headers else urllib2.Request(req_str)
    return json.loads(urllib2.urlopen(req).read())

def getLegislators(state):
    ret = {}
    house_endpoint = "{}/115/{}/members.json".format(PROPUBLICA_URL, "house")
    senate_endpoint = "{}/115/{}/members.json".format(PROPUBLICA_URL, "senate")
    house_list = data(house_endpoint, None, {"X-API-Key":API_KEY})["results"][0]["members"]   
    senate_list = data(senate_endpoint, None, {"X-API-Key":API_KEY})["results"][0]["members"]

    # Prune dicts
    house = []    
    for member in house_list:
        if member["state"] == state:
            to_add = {}
            to_add["first_name"] = member["first_name"]
            to_add["last_name"] = member["last_name"]
            to_add["current_party"] = member["party"]
            to_add["id"] = member["id"]
            to_add["phone"] = member["phone"]
            to_add["next_election"] = member["next_election"]
            house.append(to_add)
        else:
            pass

    senate = []
    for member in senate_list:
        if member["state"] == state:
            to_add = {}
            to_add["first_name"] = member["first_name"]
            to_add["last_name"] = member["last_name"]
            to_add["current_party"] = member["party"]
            to_add["id"] = member["id"]
            to_add["phone"] = member["phone"]
            to_add["next_election"] = member["next_election"]        
            senate.append(to_add)
        else:
            pass

    ret["house"] = house
    ret["senate"] = senate    
    return ret

def getNumber(legis_id):
    endpoint = "{}/members/{}.json".format(PROPUBLICA_URL, legis_id)
    ret = data(endpoint, None, {"X-API-Key":API_KEY})["results"][0]["roles"][0]["phone"]
    return ret

