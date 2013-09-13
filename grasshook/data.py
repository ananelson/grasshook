from tables import *

class Data(IsDescription):
    name = StringCol(64)
    value = Float64Col()
    collected_at = Time64Col()
