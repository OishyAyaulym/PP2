import json 
print("Interface status")
print("================================================================================")
print("DN                                                 Description           Speed    MTU  ")
print("-------------------------------------------------- --------------------  ------  ------")
with open('sample-data.json') as file:
    data=json.load(file)
for item in data["imdata"][:3]:  
    attributes=item["l1PhysIf"]["attributes"]
    dn=attributes["dn"]
    speed=attributes["speed"]
    mtu=attributes["mtu"]
    print(f"{dn}                              {speed} {mtu}")