# Civic Watch

## Overview
Civic Watch is a website designed to facilitate an increase in active participation in politics and awareness of congressional/midterm elections by making the process of calling one's Senators/House Representatives simple and seamless. 

## Installation/Running
Note: Not currently deployed, so follow these steps in order to run the flask app.
Use pip to install flask, Jinja2, requests, and twilio.
Run `$ python app.py` from the app's root directory and open http://127.0.0.1:5000/ in your browser.

## Usage
After registering and logging in, the user either provides the state they're from or opts to use their current location (Civic Watch uses a simple geolocation API to get the user's state from their IP address), and the user is given a list of their Senators and House Representatives, color-coded by party, and each of their phone numbers and years of next election (data retrieved from the ProPublica Congress API). The user would then be able to call any of these legislators directly from the site (which uses the Twilio API to do so); note, though, that this feature is not currently working due to the fact that the trial account for Twilio does not allow for calls to be made out to non-verified phone numbers). 

## Sources
https://projects.propublica.org/api-docs/congress-api/
https://www.twilio.com/docs/api/rest/making-calls
http://ip-api.com/docs/api:json/

## Contributors
Sarah Yoon
Olivia Ross
Nalo Turner
Isabella Berry
