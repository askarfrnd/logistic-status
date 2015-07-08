""" The method takes 2 arguments. awb_number and service. 
For delhivery tracking, use service as "delhivery" and 
For Ecom Express tracking, user service as "ecom_exp".
The method filters numbers alone from the given awb_number.
Example : get_status(awb_number="EM123456789IN", service="ecom_exp")
"""

from bs4 import BeautifulSoup
import urllib2
import re


def get_status(awb_number=None, service=None):
    awb_number = re.sub('[^0-9]', '', awb_number)
    if service == "ecom_exp":
        try:
            resp = urllib2.urlopen("http://billing.ecomexpress.in/track_me/multipleawb_open/?awb="+str(awb_number)+"&order=&news_go=track+now")
            response = resp.read()
        except:
            response = None
        if response:
            soup = BeautifulSoup(response)
            table = soup.find('table', attrs={'class': 'table'})
            try:
                table_body = table.find('tbody')
                rows = table_body.find_all('tr')
                delivery_status = rows[0].findAll('td')[1].text.strip()
                return {'result': delivery_status, 'status': 1}
            except:
                pass
        return {"result": "Error : No response", "status": 0}
    elif service == "delhivery":
        try:
            resp = urllib2.urlopen("http://track.delhivery.com/p/"+str(awb_number))
            response = resp.read()
        except:
            response = None
        if response:
            soup = BeautifulSoup(response)
            table = soup.find('table', attrs={'class': 'small'})
            table_body = table.find('tbody')
            rows = table_body.find_all('tr')
            delivery_status = rows[0].findAll('td')[0].text
            if delivery_status != "":
                return {'result': delivery_status, 'status': 1}
        return {"result": "Error : No response", "status": 0}

    else:
        return {"result": "Error : No response", "status": 0}
