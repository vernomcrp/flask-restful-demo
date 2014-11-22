flask-restful-demo
==================

Yeh, just demo, probably prod later :)

Installation
------------

I assume that you already have a virtualenv installed!, so activate it then

    pip install -r requirements.txt

Run api1.py
-----------

Activated virtualenv required!!

    python api1.py

Try this on your browser

    http://localhost:5000/

Run api2.py
-----------

Activated virtualenv required!!

    python api2.py

You should get vehicle.db, after run above command!
Try this on your browser
    
    http://localhost:5000/api/vehicle

You can insert by ( find some chrome or firefox extension that can deal with restful )

    use POST request with http://localhost:5000/api/vehicle

    and with content

    {"license_id" : "BAHBAH-123", "owner_name" : "Jim"}

    then use GET request to see what stuff from same url


