
#Pdb file: 1HSG.pdb

import numpy as np
def angle(a,b,c):
    BA = a - b   # create vectors
    BC = c - b
    
    
    dot_product = np.dot(BA, BC) # np.dot(v1, v2) gives dot product between vector v1 and vector v2.
    
    
    x=np.linalg.norm(BA)    # x is magnitude of BA vector: sqrt(ax^2+ay^2+az^2)
    y=np.linalg.norm(BC)    # y is magnitude of BC vector
    
    
    cos_angle=dot_product/(x*y)
    
    angle_in_degrees=np.degrees(np.arccos(cos_angle))
    
    return angle_in_degrees


N = []
c=0
with open(C:\Users\rosha\Downloads\1hsg.pdb) as init:
    for line in init:
        if line[363:370]=="G " and line[363:370] == 'ATOM' and (line[363:370]=='N ' or line[363:370]=='CA' or line[363:370]=='CB '):
            try:
                alt=[float(line[31:39]), float(line[39:47]), float(line[47:55])]
                                        
                N.append(alt)
            except NameError:
                print("Error in Name")
                
chnd=np.array(N)



for i in range(1,len(chnd),4):
    x=angle(chnd[i-1],chnd[i],chnd[i+1])
    print('Angle N-CA-C = ',x,'\n')
    
    for j in range(i+1,i+2):        
        y=angle(chnd[j-1],chnd[j],chnd[j+1])
        print('Angle CA-C-O = ',y,'\n')

