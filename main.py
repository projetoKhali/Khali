
# 
from CSV.CSVHandler import save_csv
import Users

fields = [ 1, 2, 3 ]
rows = [ [ 'a', 'b', 'c'], ['a2', 'b2', 'c2' ] ]

save_csv("data/users", fields, rows)
