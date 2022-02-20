import firebase_admin

import os

import json

from firebase_admin import credentials, firestore

cred = credentials.Certificate("serviceAccountKey.json")

firebase_admin.initialize_app(cred)

db = firestore.client()

for filename in os.listdir('data'):

    if filename.endswith('.json'):

        collectionName = "recipes"

        f = open('data/' + filename, 'r')

        docs = json.loads(f.read())

        for doc in docs:

            id = doc.pop('id', None)

            if id:

                db.collection(collectionName).document(id).set(doc, merge=True)

            else:

                db.collection(collectionName).add(doc)