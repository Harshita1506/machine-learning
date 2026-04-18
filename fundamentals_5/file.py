#opening file, reading data, writing data,closing, opening etc 

f=open("PrimeClasses\\fundamentals_5\\sample.txt","r")
data=f.read()
print(data)
data=f.readline()
f.write("text to overwrite ")# to make this work we will open file in write mode 
f.close()
#possible modes are "r","w"(truncates the file first and then overwrites )
#
# "a" appends add data to the end of already written text 
# "x " when we want to create a new file and then write 
# w bhi nayi file bna skta hai if that file doesnt exist and x bhi 
# the diff is that x alr existing file mein error show krdeta hai
# rt ( read a text file) , rb (read a binary file)
# wt ( write in text), wb( write in binary ) by default text hota hai w r mein
# + is used for updation like r+, w+,a+
# r+ can perform read and wirte both, w+ mein bhi dono, a+ bhi sab
# difference ??
# read mode - the pointer is at the beginning from the start
# append mein the pointer is at the end 
# write + mein the file becomes empty then starting se read 
f=open("sample.txt","r+")
f.write("123")# this will overwrite the first 3 with 123
print(f.read())
f.close()



