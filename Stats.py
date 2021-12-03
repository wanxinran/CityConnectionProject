from os import listdir
from os.path import isfile, join
import time
from CityConnections import CityConnections

def filesInDirectory(path):
    return [f for f in listdir(path) if isfile(join(path,f))]

def timeImplementation(V,E,implementation, debug=False):
    start = time.time()
    MST = implementation(V,E, debug)
    delta = time.time() - start
    return (MST, delta)

def compareImplementations(datasetsPath, debug=False):
    files = filesInDirectory(datasetsPath)
    for file in files:
        print('Loading: {}'.format(file))
        V,E = CityConnections.load('./{}/{}'.format(datasetsPath,file))
        print('{} - {} Verticies, {} Edges'.format(file, len(V),len(E)))
        print('Prims Implementation')
        MST,dt = timeImplementation(V,E,CityConnections.implementation1, debug)
        total = CityConnections.totalWeight(MST)
        output = '''\tPrims
\tMST Edges: {}
\tTotal Weight: {}
\tTotal Time: {} seconds'''.format(len(MST), total, dt)
        print(output)

        print('Kruskals Implementation')
        MST,dt = timeImplementation(V,E,CityConnections.implementation2, debug)
        total = CityConnections.totalWeight(MST)
        output = '''\tKruskals
\tMST Edges: {}
\tTotal Weight: {}
\tTotal Time: {} seconds'''.format(len(MST), total, dt)
        print(output)
        
            

    

'''
1) Get files in directory
2) For every file in directory
    2a) Load V,E
    2b) For Each implementation
        - Get Start Time
        - Run Implementation
        - Get End Time
        - Store Results for V,E - Time 
'''

compareImplementations('./datasets', True)