# for.else.py


class DriverException(Exception): ...


people = [("James", 17), ("Kirk", 9), ("Lars", 13), ("Robert", 8)]
driver = None

for person, age in people:
    if age >= 18:
        driver = (person, age)
        break
else:
    raise DriverException("Driver not found.")

"""
We no longer have to user the flag pattern. The exception is raised
as part of the loop logic, which makes good sense because the loop checks
for some condition. All we need to to do is set up a driver object i n case
we find one; this way the rest of the code uses the driver object for further
processing. Shorter and more elegant. 
"""
