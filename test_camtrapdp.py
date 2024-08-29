import requests
from dplib.models import Schema
from dplib.models import Package
from dplib.models import Resource



datapackage = {
   "name": "CamtrapDP",
   "profile": "https://raw.githubusercontent.com/tdwg/camtrap-dp/1.0.1/camtrap-dp-profile.json",
   "resources": [
      {
         "name": "deployments",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/1.0.1/deployments-table-schema.json"
      },
      {
         "name": "media",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/1.0.1/media-table-schema.json"
      },
      {
         "name": "observations",
         "schema": "https://raw.githubusercontent.com/tdwg/camtrap-dp/1.0.1/observations-table-schema.json"
      }
   ]
}

package = Package()
package.from_dict(datapackage)

print(package)
print("=================================================")

package2 = Package()
package2.from_path("test_data/datapackage.json")
print(package2)
print("=================================================")

schemas = {}
for res in datapackage["resources"]:
    req = requests.get(res["schema"], timeout=60)
    res_json = req.json()
    schemas[res["name"]] = Schema.from_dict(res_json)

resources = {}
for key, val in schemas.items():
    resource = Resource()
    resource.name = key
    resource.path = f"test_data/{key}.csv"
    resource.media = schemas[key]
    resources[key] = resource
    package.add_resource(resource)
    package2.add_resource(resource)

print(package)
print("=================================================")
print(package2)
print("=================================================")
