from flask import Flask, render_template, request, url_for, session, redirect
import hashlib, sqlite3, json

db = "data/database.db"

app = Flask(__name__)
app.secret_key = 

