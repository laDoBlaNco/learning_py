# designing_models.py

# DATABASE DESIGN
# 
# • Database design is an art form of its own with particular skills and
#   experience
# 
# • Our goal is to avoid the really bad mistakes and design clean and easily
#   understood databases
# 
# • Others may performance tune things later
# 
# • Database design starts with a picture...

# BUILDING A DATA MODEL
#
# • Drawing a picture of the data objects for our application and then
#   figuring out how to represent the objects and their relationships
# 
# • Basic Rule: Don't put the same string data in twice - use a relationshp
#   instead (REPLICATED NUMBERS IS OK AND WHAT WE WANT IN THE END)
# 
# • When there is one thing in the 'real world' there should be one copy of
#   that thing in the database.

# FOR EACH PIECE OF INFO ON YOUR UI
# 
# • Is the column an object or an attribute of another object?
# 
# • Once we define objects, we need to define the relationships between
#   objects

# IMPLEMENTING MODELS IN TABLES
# 
# We connect our tables through keys:
# • Primary keys are the endpoints we we connect each table (the reference)
# • Foreign keys are the starting point that will connect to those endpoints
#   (Track table: album_id) ----> (Album table: id) 
#               Foreign key                 Primary key
# • Logical key is that thing that we might use as the look-up from the 
#   outside world. (the Track title in our exmaple). This might be used
#   in a ORDER BY or WHERE clause

# THE JOIN OPERATION
# 
# • The JOIN operation links across several tables as part of a select
#   operation
# 
# • You must tell JOIN how to use the keys that make the connection between
#   the tables using an ON clause

