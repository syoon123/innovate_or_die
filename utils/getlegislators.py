from flask import Flask, render_template, request, url_for, session, redirect
import sqlite3, json, requests, urllib, urllib2

# ProPublica Congress Data URL
PROPUBLICA_URL = "https://api.propublica.org/congress/v1"
API_KEY = "brEmpnztKf2ITVHkIqcXPaC5WZhbsN025JDoPSl7"

def data(endpoint, params, headers):
    params_str = urllib.urlencode(params) if params else ""
    req_str = "{}/?{}".format(endpoint, params_str) if params_str else endpoint
    req = urllib2.Request(req_str, None, headers) if headers else urllib2.Request(req_str)
    return json.loads(urllib2.urlopen(req).read())

def getLegislators(state):
    ret = {}
    house_endpoint = "{}/115/{}/members.json".format(PROPUBLICA_URL, "house")
    senate_endpoint = "{}/115/{}/members.json".format(PROPUBLICA_URL, "senate")
    house_dict = data(house_endpoint, None, {"X-API-Key":API_KEY})    
    senate_dict = data(senate_endpoint, None, {"X-API-Key":API_KEY})

    # Prune dicts
    
    
    ret["house"] = house_dict
    ret["senate"] = senate_dict    
    return ret


