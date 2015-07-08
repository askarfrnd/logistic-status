# logistic-status
A simple API built for tracking the orders made through Delhivery, Ecom Express.


The method takes 2 arguments. awb_number and service. 

For delhivery tracking, use service value as "delhivery" and for Ecom Express tracking, user service value as "ecom_exp".

#### Requirements:
<a href="https://pypi.python.org/pypi/beautifulsoup4/4.3.2">BeautifulSoup4</a>


#### Examples:

###### Delhivery:
print get_status(awb_number="000123456789", service="delhivery")

print get_status(awb_number="DELHIVERY - 000123456789", service="delhivery")

###### Ecom Express:
print get_status(awb_number="EM123456789IN", service="ecom_exp")

print get_status(awb_number="123456789", service="ecom_exp")


