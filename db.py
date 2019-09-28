# This file is for all DB connections and DB logic

import pyrebase

class FireBaseConnection:
    def connect_to_db(self):
        fire_base_config = {
            "apiKey": "AIzaSyAwC4JLIC_hS_ODvHr_2oaw7e__P_-PzLY",
            "authDomain": "hackuta19-notoday.firebaseapp.com",
            "databaseURL": "https://hackuta19-notoday.firebaseio.com",
            "projectId": "hackuta19-notoday",
            "storageBucket": "hackuta19-notoday.appspot.com",
            "messagingSenderId": "63356394783",
            "appId": "1:63356394783:web:9e653b492c50427c14e42a",
            "serviceAccount": "config.json"
        }
        fire_base = pyrebase.initialize_app(fire_base_config)
        # result = fire_base.get('/users', None)
        print(fire_base)
