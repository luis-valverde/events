import datetime
import os

my_test = os.getenv('WEB_TEST')

print(f"Hello! Current time: {datetime.datetime.now()}")
print(f"Env test is: {my_test}")
