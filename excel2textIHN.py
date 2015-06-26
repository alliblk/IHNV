import xlrd #remember to have all xlrd scripts in pwd
book = xlrd.open_workbook("Ugrp1971-2013FirstDets.xlsx")
print "The number of worksheets is", book.nsheets
print "Worksheet name(s):", book.sheet_names()
sh = book.sheet_by_index(0)
print sh.name, sh.nrows, sh.ncols

for i in range(1, sh.nrows):
	row = ">" + str(int(sh.cell_value(i, 16))) #sample isolation year
	row += "_" + str(sh.cell_value(i, 27)) #mGUSD
	row += "_" + str(sh.cell_value(i, 28)) #U subgroup designation
	row += "\n" + str(sh.cell_value(i, 30)).strip() #mid G sequence
	print row
