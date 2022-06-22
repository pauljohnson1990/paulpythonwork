frameworks=[
    ["django","python",4],
    ["flask","python",3],
    ["spring","java",5],
    ["express","javascript",4],
    ["angular","javascript",4]
]
# print in python framework details
python_fw=[fw for fw in frameworks if fw[1]=="python"]
print(python_fw)
js_fw=[fw for fw in frameworks if fw[1]=="javascript"]
print(js_fw)