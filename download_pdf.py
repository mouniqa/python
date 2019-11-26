#https://www.istqb.guru/Documents/www.istqb.guru_ISTQB-Question-Paper1.pdf
import requests

number=1
while(True):
    file_name = "ISTQB-Question-Paper"+str(number)+".pdf"
    image_url = "https://www.istqb.guru/Documents/www.istqb.guru_"+file_name

    # URL of the image to be downloaded is defined as image_url
    r = requests.get(image_url) # create HTTP response object

    # send a HTTP request to the server and save
    # the HTTP response in a response object called r
    with open("file_name",'wb') as f:

        # Saving received content as a png file in
        # binary format

        # write the contents of the response (r.content)
        # to a new file in binary mode.
        f.write(r.content)
        print('downloaded  ',file_name)
        number += 1
