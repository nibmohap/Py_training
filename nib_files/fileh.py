data='''this is jus a data.
...kjjhfgfdfd.
...kjjhghghg.
....jhjhjhjh'''
f=open('test.txt','w')
f.write(data)
f.close()
f=open('test.txt')
print f.tell()


fil=f.readlines()
print list(enumerate(fil,1))
fil.insert(2,"nibedita***")
print fil
f.close()
f=open('test.txt','w+')
f.writelines(fil)





