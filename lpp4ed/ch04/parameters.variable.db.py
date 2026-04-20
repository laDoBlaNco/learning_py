# parameters.variable.db.py

# here we have a function that needs to connect to a database by simply
# calling this function with no parameters. We also want to connect to any
# other database by passing to the function the appropriate parameters.


def connect(**options):
    conn_params = {
        "host": options.get("host", "127.0.0.1"),
        "port": options.get("port", 5432),
        "user": options.get("user", ""),
        "pwd": options.get("pwd", ""),
    }
    print(conn_params)


connect()
connect(host='127.0.0.42',port=5433)
connect(port=5431,user='fab',pwd='gandalf')

# this way we can prepare a dict of connection parameters (conn_params) in 
# the function using default values as fallbacks, allowing them to be
# overwritten if they are provided in the function call. There are better ways
# to do this with fewer lines of code, but we are not concerned with that right
# now. This was to show why this is at times necessary


