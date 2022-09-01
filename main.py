from CSV.CSVHandler import csvsave
import Users


fields = [ 1, 2, 3 ]
rows = [ [ 'a', 'b', 'c'], ['a2', 'b2', 'c2' ] ]

csvsave("data/users", fields, rows)
