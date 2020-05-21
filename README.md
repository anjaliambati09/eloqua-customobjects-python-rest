# eloqua-customobjects-python-rest


## you put in the below information in get_customObjects.py
        1.site: Replace with Eloqua instance name
        2.user: Replace with Eloqua username
        3.password: Replace with Eloqua password
        
        request = EloquaRequest('site', 'user', 'password')
        
        replace the above line with 
        
        request = EloquaRequest('your-site-name', 'your-user-name', 'your-password')
        
## you put in the below information in get_customObjects.py
        
        Also replace the below line with {id}

        response = request.get('/data/customObject/{id}', None)
        
        replace with
        
        response = request.get('/data/customObject/2073', None)
