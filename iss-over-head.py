import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 50.064651
MY_LONG = 19.944981 

def above_head(iss_latitude, iss_longitude, my_lat, my_long, sunrise, sunset, time_now):
    time_now_plus = time_now.hour - 2
    if my_lat-5 <= iss_latitude <= my_lat+5 and my_long-5 <= iss_longitude <= my_long+5:
        if time_now_plus > sunset or time_now_plus < sunrise:
            my_email =  "kamil.tylka84@gmail.com"
            password = "mkpjjwiikaxusqqw"

            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user= my_email, password=password)
                connection.sendmail(
                    from_addr=my_email, 
                    to_addrs="kamil.tylka@yahoo.com", 
                    msg=f"Subject:LOOK ABOVE\nLook Above!."
                    )
    else:
        return

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

while True:
    above_head(iss_latitude,iss_longitude,MY_LAT,MY_LONG,sunrise,sunset,time_now)
    time.sleep(60)



