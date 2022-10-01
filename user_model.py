from turtle import distance
import mysql.connector
import json


class user_model():
    
    def __init__(self):


        try:
            self.con=mysql.connector.connect(host="adclegacy-large-57.cpvodttlpa7n.us-west-2.rds.amazonaws.com",
                                user="bvJj7t89acgD",
                                password="q4zYwfwssKY2fyQDfnGK",
                                database="adcLegacy")
            self.cur=self.con.cursor(dictionary=True)
            print ("connection succesful")
        
        except:
            print("error")
        
    def user_getall_model(self):
        self.cur.execute("select lat,lng,zipcode from adcLegacy.zip_shapers limit 5 ")
        result=self.cur.fetchall()
        print(type(result))
        for i in range(len(result)):
            result[i]['lat']=float(result[i]['lat'])
            result[i]['lng']=float(result[i]['lng'])
            result[i]['zipcode']=str(result[i]['zipcode'])

        print(result)

        return json.dumps(result)

    def getnearzip_model(self,data):

        pickup_lat=data['lat']
        pickup_lng=data['lng']
        distance=data['radius']
        pickup_zipcode=data['zipcode']
        
        qry=f"SELECT * FROM (SELECT zipcode as delivery_zip, lat as delivery_lat, lng as delivery_lng , (((ACOS(SIN(({pickup_lat} * PI() / 180)) * SIN((lat * PI() / 180)) + \
        COS(({pickup_lat} * PI() / 180)) * COS((lat * PI() / 180)) * COS((({pickup_lng} - lng) * PI() / 180)))) * 180 / PI()) * 60\
        * 1.1515 * 1.609344) AS distance FROM adcLegacy.zip_shapers) zipcode WHERE distance <= {distance} order by distance asc  "
       
        self.cur.execute(qry)
       
        result=self.cur.fetchall()

        if len(result > 0):

            print(type(result))

            for i in range(len(result)):
                result[i]['delivery_lat']=float(result[i]['delivery_lat'])
                result[i]['delivery_lng']=float(result[i]['delivery_lng'])
                result[i]['delivery_zip']=str(result[i]['delivery_zip'])

                result[i]['pickup_lat']=pickup_lat
                result[i]['pickup_lng']=pickup_lng
                result[i]['pickup_zipcode']=pickup_zipcode

            return {"payload":result}


        else:

            return {"message":"NO DATA FOUND"}
        
        
    

