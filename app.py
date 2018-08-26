from flask import Flask, render_template
from random import random
import pandas as pd
import numpy as np

merged = pd.read_csv('data/affordability_data.csv')
app = Flask(__name__)

@app.route('/')
def index():
    industry_names = merged['industry'].unique()
    years = merged['year'].unique()
    return render_template('index.html', years=years, industry_names=industry_names)

@app.route('/table/<industry_name>/<year>')
def table(industry_name, year):
    zips = retrieve_affordable_zips(merged, industry_name, int(year))
    #n = len(zips)
    x = zips
    #y = zips
    return render_template('table.html', data=x)

def retrieve_affordable_zips(merged, industry_name, year):
    aff = merged.loc[:, merged.columns.str.startswith('98')].loc[(merged['industry'] == industry_name)&(merged['year'] == year)].values[0]
    zips = merged.loc[:, merged.columns.str.startswith('98')].columns
    return zips[aff]

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)