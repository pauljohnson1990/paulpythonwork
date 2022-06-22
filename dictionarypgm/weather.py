weather=[
    {"district": "tvm", "temp":30},
    {"district": "ktm","temp":28 },
    {"district": "apy","temp":27},
    {"district": "idk","temp":18 },
    {"district": "ekm","temp":31 },
    {"district": "pta","temp":21},
    {"district": "tsr","temp":24},
    {"district": "kzd","temp":29},
    {"district": "pkd","temp":34},
    {"district": "mpm","temp":31},
    {"district": "tvm", "temp": 31},
    {"district": "ktm", "temp": 29},
    {"district": "apy", "temp": 26},
    {"district": "idk", "temp": 20},
    {"district": "ekm", "temp": 30},
    {"district": "pta", "temp": 22},
    {"district": "tsr", "temp": 27},
    {"district": "kzd", "temp": 28},
    {"district": "pkd", "temp": 30},
    {"district": "mpm", "temp": 29},

]
out={}
for data in weather:
    if data["district"] in out:
        if out[data["district"]]<data["temp"]:
            out[data["district"]]=data["temp"]
    else:
        out[data["district"]] = data["temp"]
print(out)

# sort out based on temparature
sorted_list=sorted(out.items(),key=lambda t:t[1],reverse=True)

print(sorted_list)

# find max tem district
print(sorted_list[0])
# find min tem district
print(sorted_list[len(sorted_list)-1])
# dictionary methods