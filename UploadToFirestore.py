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
        size = len(docs)

        minVal = 19500
        maxVal = 39000

        for idx, doc in enumerate(docs):

            if (idx > minVal and idx <= maxVal):

                id = doc.pop('id', None)

                index = idx + 1

                print( "Uploaded " + str(index) + " out of " + str(maxVal), end="\r")

                if id:

                    db.collection(collectionName).document(id).set(doc, merge=True)

                else:

                    db.collection(collectionName).add(doc)