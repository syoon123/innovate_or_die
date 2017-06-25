from flask import Flask, render_template, request, url_for, session, redirect
import sqlite3, json, requests, urllib, urllib2
from twilio.rest import Client
import getlegislators

# Twilio
ACCOUNT_SID = json.loads(open("keys.json").read())["twilio"]["ACCOUNT_SID"]
AUTH_TOKEN = json.loads(open("keys.json").read())["twilio"]["AUTH_TOKEN"]

def callLegislator(legis_id):
    politician = "+1" + getlegislators.getNumber(legis_id).replace("-","")
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    
    numbers = client.available_phone_numbers("US") \
                    .local \
                    .list(area_code="646")
    
    number = client.incoming_phone_numbers \
                   .create(phone_number=numbers[0].phone_number)
    
    client.calls.create(to = politician, from_ = number, url = "http://demo.twilio.com/docs/voice.xml")

    
