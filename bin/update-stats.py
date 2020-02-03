#!/usr/bin/env python

import json
import os

import requests
from requests.exceptions import HTTPError


INDIGO_API_TOKEN = os.environ.get('INDIGO_API_TOKEN')
INDIGO_URL = 'https://api.laws.africa/v2'


session = requests.Session()
session.headers['Authorization'] = f'Token {INDIGO_API_TOKEN}'


def fetch_all(path):
    res = []
    url = INDIGO_URL + path

    while url:
        print(f"Fetching {url}")
        resp = session.get(url)
        resp.raise_for_status()
        data = resp.json()
        res.extend(data['results'])
        url = data['next']

    return res


def update_country_stats(place_code, stats):
    works = fetch_all(f'/akn/{place_code}/.json')
    stats['n_principal'] = sum(1 for w in works if not w['stub'] and not w['parent_work'])
    stats['n_stubs'] = sum(1 for w in works if w['stub'])
    stats['as_at_date'] = max(w['as_at_date'] for w in works if w['as_at_date'])


def update_bylaw_stats(country_code, stats):
    countries = {c['code']: c for c in fetch_all('/countries.json')}
    localities = countries[country_code]['localities']

    works = []
    munis = 0

    for loc in localities:
        try:
            works.extend(fetch_all(f"/akn/{loc['frbr_uri_code']}/.json"))
            munis += 1
        except HTTPError as e:
            if e.response.status_code != 404:
                raise

    stats['n_bylaws'] = sum(1 for w in works if w['subtype'] == 'by-law' and not w['stub'])
    stats['n_municipalities'] = munis
    stats['as_at_date'] = max(w['as_at_date'] for w in works if w['as_at_date'])


def update_stats():
    with open("_data/commons.json") as f:
        stats = json.load(f)

    #update_country_stats('na', stats['na'])
    update_bylaw_stats('za', stats['za'])

    with open("_data/commons.json", "w") as f:
        f.write(json.dumps(stats, indent=2, sort_keys=True))


if __name__ == '__main__':
    update_stats()
