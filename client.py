import requests

def getName():
    r = requests.get("http://vcm-3569.vm.duke.edu:5000/name")
    r_result = r.json()
    print(r_result)
    
def getHelloMessage():
    r2 = requests.get("http://vcm-3569.vm.duke.edu:5000/hello/Pamla Chace Gore")
    r2_result = r2.json()
    print(r2_result)

def getDistance():
    r3 = requests.post("http://vcm-3569.vm.duke.edu:5000/distance", json={"a": [3,7], "b": [3,9]})
    distance_result = r3.json()
    print(distance_result)

if __name__ == '__main__':
    main()
