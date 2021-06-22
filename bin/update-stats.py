# NB: this is run on Travis with python 2.7

import json
import os

import requests
from requests.exceptions import HTTPError


INDIGO_API_TOKEN = os.environ.get('INDIGO_API_TOKEN')
INDIGO_URL = 'https://api.laws.africa/v2'


session = requests.Session()
session.headers['Authorization'] = 'Token ' + INDIGO_API_TOKEN


COVID19_COUNTRIES = ['bw', 'gh', 'na', 'za', 'ug', 'zm', 'zw', 'ls', 'mw']


def fetch_all(path, params={}):
    res = []
    url = INDIGO_URL + path

    while url:
        print("Fetching " + url)
        resp = session.get(url, params=params)
        resp.raise_for_status()
        data = resp.json()
        res.extend(data['results'])
        url = data['next']

    return res


def update_country_stats(place_code, stats):
    works = fetch_all('/akn/' + place_code + '/.json')
    stats['n_principal'] = sum(1 for w in works if not w['stub'] and not w['parent_work'])
    stats['n_stubs'] = sum(1 for w in works if w['stub'])
    stats['as_at_date'] = max(w['as_at_date'] for w in works if w['as_at_date'])


def update_covid19_stats(stats):
    works = []
    for country in COVID19_COUNTRIES:
        works.extend(fetch_all('/akn/' + country + '/.json', {'taxonomy': 'lawsafrica-special:COVID-19'}))

    stats['n_principal'] = sum(1 for w in works if not w['stub'])
    stats['as_at_date'] = max(w['as_at_date'] for w in works if w['as_at_date'])
    stats['n_countries'] = len(COVID19_COUNTRIES)


def update_bylaw_stats(country_code, stats):
    countries = {c['code']: c for c in fetch_all('/countries.json')}
    localities = countries[country_code]['localities']

    works = []
    n_munis = 0

    # this will also include provinces, so only look for by-laws
    for loc in localities:
        try:
            bylaws = [w
                      for w in fetch_all("/akn/" + loc['frbr_uri_code'] + "/.json")
                      if w['subtype'] == 'by-law' and not w['stub']]
            works.extend(bylaws)
            if bylaws:
                n_munis += 1
        except HTTPError as e:
            if e.response.status_code != 404:
                raise

    stats['n_bylaws'] = len(works)
    stats['n_municipalities'] = n_munis
    stats['as_at_date'] = max(w['as_at_date'] for w in works if w['as_at_date'])


def update_stats():
    with open("_data/commons.json") as f:
        stats = json.load(f)

    for code in ['na', 'ug']:
        update_country_stats(code, stats.setdefault(code, {}))

    update_bylaw_stats('za', stats.setdefault('za_bylaws', {}))
    update_covid19_stats(stats['covid19'])

    with open("_data/commons.json", "w") as f:
        f.write(json.dumps(stats, indent=2, sort_keys=True))


if __name__ == '__main__':
    update_stats()
