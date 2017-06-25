from flask import Flask, render_template, request, url_for, session, redirect
import sqlite3, json, requests, urllib, urllib2
from twilio.rest import Client
import getlegislators

# Twilio
TWILIO_URL = "https://api.twilio.com/2010-04-01"
ACCOUNT_SID = json.loads(open("keys.json").read())["twilio"]["ACCOUNT_SID"]
AUTH_TOKEN = json.loads(open("keys.json").read())["twilio"]["AUTH_TOKEN"]

