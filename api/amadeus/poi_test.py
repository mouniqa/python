from amadeus import Client, ResponseError
import json
import jsonpath


amadeus = Client(
    client_id='UESXb1o6t5MFv7OONash0yF3mSvgI5vX',
    client_secret='gBjQrwH7OWA1yMPo'
)

try:
    response = amadeus.reference_data.locations.points_of_interest.get(latitude=41.397158,longitude=2.160873,radius=2)
    print(response.data)
except ResponseError as error:
    print(error)


json_output = response.data[0]

ids = jsonpath.jsonpath(json_output,'self')
print(len(ids))
