import requests
r = requests.get("http://vcm-3569.vm.duke.edu:5000/name")
print(r)
r2 = requests.get("http://vcm-3569.vm.duke.edu:5000/hello/Pamla Chace Gore")
print(r2)
r3 = requests.post("http://vcm-3569.vm.duke.edu:5000/distance", json={"a": [3,7], "b": [3,9]})
distance_result = r3.json()
print(distance_result)
