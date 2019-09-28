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
        self.fire_base = pyrebase.initialize_app(fire_base_config)
        # result = fire_base.get('/users', None)
        print(self.fire_base)

        # Get a reference to the database service
        # db = self.fire_base.database()
        # companies = db.child("companies").get()
        # print(companies.val())

    def get_companies(self):
        db = self.fire_base.database()
        # companies = db.child("companies").child("company_name").get()

        # print()
        # print(companies.val())
        # print(companies.key())
        # print()

        companies = db.child("companies").get()

        lstCompanies = list()
        for company in companies.each():
            # print(company.key())
            # print(company.val())
            for key, value in dict(company.val()).items():
                if key != "company_name":
                    continue
                lstCompanies.append(value.lower())
                # print(key)
                # print(value)

        # print(companies.child("company_name").get().val())
        # print(companies.child("company_name").get().key())
        return lstCompanies
