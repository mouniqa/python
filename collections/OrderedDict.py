from collections import OrderedDict

# create a regular unsorted dictionary

d = {'banana':3,'apple':4,'orange':1,'pear':2}

print(d)

for a,b in d.items():
    print(a,':',b)

od = OrderedDict(sorted(d.items(),key=lambda t:len(t[0])))

print(od)

od2 = OrderedDict([('name','Jagadeesh'),('age',32),('address','Stockholm')])
print(od2)
