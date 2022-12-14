import random

import numpy as np

c = 0.001
epoci = 80
patters = np.array([np.array([45, 85]),
                    np.array([50, 43]),
                    np.array([40, 80]),
                    np.array([55, 42]),
                    np.array([200, 43]),
                    np.array([48, 40]),
                    np.array([195, 41]),
                    np.array([43, 87]),
                    np.array([190, 40])])

w1 = np.array([random.uniform(np.min(patters[:, 0]), np.max(patters[:, 0])),
               random.uniform(np.min(patters[0, :]), np.max(patters[0, :]))])

w2 = np.array([random.uniform(np.min(patters[:, 0]), np.max(patters[:, 0])),
               random.uniform(np.min(patters[0, :]), np.max(patters[0, :]))])

w3 = np.array([random.uniform(np.min(patters[:, 0]), np.max(patters[:, 0])),
               random.uniform(np.min(patters[0, :]), np.max(patters[0, :]))])

prototypes = np.array([w1, w2, w3])
initial_prototipes = np.copy(prototypes)
# Initializare patterns/ generare prototipuri w/ afisarea valorilor initiale de prototipui
print("#####################\nCASTIGATORUL IA TOT\n#####################")
while epoci > 0: # parcurgem un nr fix de epoci
    print(f"Epoca nr{abs(81-epoci)}")
    wm = 0
    for pattern in patters:
        mins = []
        min_val = 999
        for prototype in prototypes:
            val = np.linalg.norm(pattern - prototype) #calculam norma vectorului ||xi - wm||
            mins.append(val)

        for minV in mins:
            if minV < min_val:
                min_val = minV # aflam valoarea minima dintre cele 3 normele celor 3 diferente
            
            # if min(abs(np.subtract(pattern, prototype))) < min1:
            #       min1 = min(abs(np.subtract(pattern, prototype)))
            #       wm = prototype
            #       print(f"prototip:{prototype} -> pattern:{pattern}")
        
        index = 0
        for w in prototypes:
            if np.linalg.norm(pattern - w) == min_val: #cautam diferenta care ne a dat norma minima
                w = w + c*(pattern - w) #actualizarea prototipului
                prototypes[index] = w #actualizarea prototipului in lista de prototipuri
                print(f"prototip:{w} -> pattern:{pattern}") #printarea prototipului si a patternului de instruire
                break
            else:
                index += 1

    epoci -= 1


print("#####################\nPROTOTIPURILE INITIALE\n#####################")
for initial_prototype in initial_prototipes:
      print(initial_prototype)
print("#####################\nPROTOTIPURILE FINALE\n#####################")
for prototype in prototypes:
    print(prototype)
    