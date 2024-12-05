
read="D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\years.txt"
century="D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\century_years.txt"
leap="D:\\vs code\\Pythonworks\\Datasets_ for_file_Operations\\leap_years.txt"

f_read=open(read,"r")
f_century=open(century,"w")
f_leapyear=open(leap,"w")

for year in f_read:
    year=int(year)
    if year%100==0:
        f_century.write(str(year)+"\n")

    if year%100==0 and year%400==0 or year%4==0 and year%100!=0:
        f_leapyear.write(str(year)+"\n")

f_read.close()
f_century.close()
f_leapyear.close()