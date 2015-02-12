'''
Created on Feb 12, 2015

@author: vivek
'''
 # import celery
import celery

# import our send_email task
from mytask import send_email
from mytask import add

#call function 
add_result = add(3,8)

#print add_result.status()

# call our email function
#result = send_email.delay('', 'all your smtp are belong to us', 'somebody set up us the bomb')
