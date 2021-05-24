import numpy as np
import math
import matplotlib.pyplot as plt 
from matplotlib import style
style.use('dark_background')

#arr = ([['0', '0'], ['2', '1'], ['1', '1']],  {1: [('0', '0'), ('1', '1')], 2: [('1', '1'), ('2', '1')]}, {'Fx': ['0', '0','0'], 'Fy': ['0', '0','0'],'M':['0','0','0']}, 
#{'Fs': [0, 0], 'Fa': [0,0], 'Fd': [1000,0], 'Md': [0,-15000]}, {1: 16.0312195418814, 2: 17.029386365926403, 3: 11.045361017187261}, 
 #      {'constx': [['0', '0'], ['2', '1']], 'consty': [['0', '0'], ['2', '1']], 'constangles': [['0', '0'], ['2', '1']]}, {'A': '0.01', 'E': '2e11', 'J': '1e-5'})
#arr = ([['0', '0'], ['1', '0'], ['1', '1']],  {1: [('0', '0'), ('1', '0')], 2: [('1', '0'), ('1', '1')],3: [('0', '0'), ('1', '1')]}, {'Fx': ['0', '0','10000'], 'Fy': ['0', '0','-20000'],'M':['0','0','0']}, 
#{'Fs': [0, 0,0], 'Fa': [0,0,0], 'Fd': [0,0,0], 'Md': [0,0,0]}, {1: 16.0312195418814, 2: 17.029386365926403, 3: 11.045361017187261}, 
#       {'constx': [['0', '0'], ['1', '0']], 'consty': [['0', '0'], ['1', '0']], 'constangles': [['0', '0'], ['1', '0']]}, {'A': '0.01', 'E': '2e11', 'J': '1e-5'})



def Ketqua(arr):
    node = len(arr[0])

    load_X = []
    if 'Fx' in arr[2]:
        for i in range(len(arr[2]['Fx'])):
            load_X.append(float(arr[2]['Fx'][i]))
    elif 'Fx' not in arr[2]:
        for i in range(len(arr[0])):
            load_X.append(0)

    load_Y = []
    if 'Fy' in arr[2]:
        for i in range(len(arr[2]['Fy'])):
            load_Y.append(float(arr[2]['Fy'][i]))
    elif 'Fy' not in arr[2]:
        for i in range(len(arr[0])):
            load_Y.append(0)

    node_moment = []
    if 'M' in arr[2]:
        for i in range(len(arr[2]['M'])):
            node_moment.append(float(arr[2]['M'][i]))
    elif 'M' not in arr[2]:
        for i in range(len(arr[0])):
            node_moment.append(0)

    ele_input = []
    for i in range(len(arr[1])):
        arr1 = []
        for j in range(len(arr[1][i+1])):
            for k in range(len(arr[0])):
                if list(arr[1][i+1][j]) == arr[0][k]:
                    arr1.append(k+1)
        ele_input.append(arr1)

    L = []
    for i in range(len(arr[1])):
        temp = arr[1][i+1]
        ele_position = [(float(temp[1][0])-float(temp[0][0])),(float(temp[1][1])-float(temp[0][1]))]
        L.append(math.sqrt(ele_position[0]**2+ele_position[1]**2))

    goc = []
    for i in range(len(arr[1])):
        temp = arr[1][i+1]
        ele_position = [(float(temp[1][0])-float(temp[0][0])),(float(temp[1][1])-float(temp[0][1]))]
        axisX_position = [(float(temp[1][0])-float(temp[0][0])), 0]
        if temp[0][1] > temp[1][1]:
            goc.append(-round(math.degrees(math.acos(abs(axisX_position[0])/L[i])), 4))
        else:
            goc.append(round(math.degrees(math.acos(abs(axisX_position[0])/L[i])), 4))

    const_X=[]
    if 'constx' in arr[5]:
        for i in range(len(arr[5]['constx'])):
            for j in range(len(arr[0])):
                if list(arr[5]['constx'][i])==arr[0][j]:
                    const_X.append(j+1)
    const_Y=[]
    if 'consty' in arr[5]:
        for i in range(len(arr[5]['consty'])):
            for j in range(len(arr[0])):
                if list(arr[5]['consty'][i])==arr[0][j]:
                    const_Y.append(j+1)
    const_goc=[]
    if 'constangles' in arr[5]:
        for i in range(len(arr[5]['constangles'])):
            for j in range(len(arr[0])):
                if list(arr[5]['constangles'][i])==arr[0][j]:
                    const_goc.append(j+1)

    axial_load=arr[3]['Fd']
    center_load=arr[3]['Fs']
    distributed_load=arr[3]['Fa']
    line_moment=arr[3]['Md']

    A=float(arr[6]['A'])
    E=float(arr[6]['E'])
    J=float(arr[6]['J'])

    ele = np.array(ele_input)-1
    constraint = []
    if all([ x == 0 for x in distributed_load ]) and all([ x == 0 for x in line_moment ]) and all([ x == 0 for x in center_load ]) :
        dof=2
    else:
        dof=3
    total_stiff = np.zeros((node*dof, node*dof), dtype=float)
    node_load_vect = np.zeros((node*dof), dtype=float)
    AxialLoad_vect = np.zeros((node*dof), dtype=float)
    DistibutedLoad_vect = np.zeros((node*dof), dtype=float)
    LineMoment_vect = np.zeros((node*dof), dtype=float)
    CenterLoad_vect = np.zeros((node*dof), dtype=float)
    Displacement_vect = np.zeros((node*dof), dtype=float)
    diagram_Moment = np.zeros((node*dof), dtype=float)
    if dof == 2:
        for i in range(len(goc)):

            a = round(math.cos(math.radians(goc[i]))**2, 4)
            b = round(math.cos(math.radians(goc[i]))*math.sin(math.radians(goc[i])), 4)
            c = round(math.sin(math.radians(goc[i]))**2, 4)
            ele_stiff = (E*A/L[i])*np.array([[a, b, -a, -b], [b, c, -b, -c], [-a, -b, a, b], [-b, -c, b, c]])

            for j in range(2):
                for k in range(2):
                    total_stiff[dof*ele[i][j]:(dof*ele[i][j]+dof), dof*ele[i][k]:(dof*ele[i][k]+dof)] += ele_stiff[dof*j:(dof*j+dof), dof*k:(dof*k+dof)]

            cos = round(math.cos(math.radians(goc[i])), 4)
            sin = round(math.sin(math.radians(goc[i])), 4)
            for j in range(len(ele[i])):
                AxialLoad_vect[(ele_input[i][j]-1) *dof] += axial_load[i]*L[i]*cos/2
                AxialLoad_vect[(ele_input[i][j]-1) *dof+1] += axial_load[i]*L[i]*sin/2

        for i in range(len(const_X)):
            constraint.append(const_X[i]*dof-dof)
        for i in range(len(const_Y)):
            constraint.append(const_Y[i]*dof-1)
        constraint.sort()

        for i in range(len(ele)):
            for j in range(len(ele[i])):
                node_load_vect[ele[i][j]*dof] = load_X[ele[i][j]]
                node_load_vect[ele[i][j]*dof+1] = load_Y[ele[i][j]]
        total_load = node_load_vect+AxialLoad_vect 
    elif dof == 3:
        for i in range(len(goc)):
            cos = round(math.cos(math.radians(goc[i])), 4)
            cs = round(math.cos(math.radians(goc[i]))*math.sin(math.radians(goc[i])), 4)
            sin = round(math.sin(math.radians(goc[i])), 4)
            B=12*J/L[i]**2
            a = A*cos**2+B*sin**2
            b = A*sin**2+B*cos**2
            c = (A-B)*cs
            e = B*L[i]*sin/2
            d = B*L[i]*cos/2
            f = 2*J
            ele_stiff = (E/L[i])*np.array([[a, c, -e, -a, -c, -e], [c, b, d, -c, -b, d], [-e, d, 2*f, e, -d, f], [-a, -c, e, a, c, e], [-c, -b, -d, c, b, -d], [-e, d, f, e, -d, 2*f]])

            for j in range(2):
                for k in range(2):
                    total_stiff[dof*ele[i][j]:(dof*ele[i][j]+dof), dof*ele[i][k]:(dof*ele[i][k]+dof)] += ele_stiff[dof*j:(dof*j+dof), dof*k:(dof*k+dof)]

            for j in range(len(ele[i])):
                AxialLoad_vect[(ele_input[i][j]-1) *dof] += axial_load[i]*L[i]*cos/2
                AxialLoad_vect[(ele_input[i][j]-1) *dof+1] += axial_load[i]*L[i]*sin/2

            T_matrix = np.array([[-sin, 0, 0, 0], [cos, 0, 0, 0], [0, 1, 0, 0], [0, 0, -sin, 0], [0, 0, cos, 0], [0, 0, 0, 1]])

            P = distributed_load[i]
            P_vect = np.array([-P*L[i]/2, (-P*L[i]**2)/12, -P*L[i]/2, (P*L[i]**2)/12])
            line_ele_load = T_matrix.dot(P_vect)
            for j in range(len(ele[i])):
                DistibutedLoad_vect[(ele_input[i][j]-1)*dof] += line_ele_load[j*dof]
                DistibutedLoad_vect[(ele_input[i][j]-1)*dof+1] += line_ele_load[j*dof+1]
                DistibutedLoad_vect[(ele_input[i][j]-1)*dof+2] += line_ele_load[j*dof+2]
                            
            M = line_moment[i]
            M_vect = np.array([-3*M/(2*L[i]), -M/4, 3*M/(2*L[i]), -M/4])
            line_ele_moment = T_matrix.dot(M_vect)
            for j in range(len(ele[i])):
                LineMoment_vect[(ele_input[i][j]-1) * dof] += line_ele_moment[j*dof]
                LineMoment_vect[(ele_input[i][j]-1) * dof+1] += line_ele_moment[j*dof+1]
                LineMoment_vect[(ele_input[i][j]-1) * dof+2] += line_ele_moment[j*dof+2]

            Pc = center_load[i]
            Pc_vect = np.array([-Pc*L[i]/4, (-Pc*L[i]**2)/16, (-Pc*L[i])/4, (Pc*L[i]**2)/16])
            center_ele_load = T_matrix.dot(Pc_vect)
            for j in range(len(ele[i])):
                CenterLoad_vect[(ele_input[i][j]-1)* dof] += center_ele_load[j*dof]
                CenterLoad_vect[(ele_input[i][j]-1)* dof+1] += center_ele_load[j*dof+1]
                CenterLoad_vect[(ele_input[i][j]-1)* dof+2] += center_ele_load[j*dof+2]

        for i in range(len(const_X)):
            constraint.append(const_X[i]*dof-dof)
        for i in range(len(const_Y)):
            constraint.append(const_Y[i]*dof-2)
        for i in range(len(const_goc)):
            constraint.append(const_goc[i]*dof-1)
        constraint.sort()

        for i in range(len(ele)):
            for j in range(len(ele[i])):
                node_load_vect[ele[i][j]*dof] = load_X[ele[i][j]]
                node_load_vect[ele[i][j]*dof+1] = load_Y[ele[i][j]]
                node_load_vect[ele[i][j]*dof+2] = node_moment[ele[i][j]]
        total_load = node_load_vect+AxialLoad_vect + DistibutedLoad_vect+LineMoment_vect+CenterLoad_vect
        
    compact_stiff = total_stiff
    compact_load = total_load
    for i in reversed(range(len(constraint))):
        compact_stiff = np.delete(compact_stiff, constraint[i], 1)
        compact_stiff = np.delete(compact_stiff, constraint[i], 0)
    for i in reversed(range(len(constraint))):
        compact_load = np.delete(compact_load, constraint[i], 0)

    compact_displacement=((np.linalg.inv(compact_stiff)).dot(compact_load.transpose()))
    non_constraint=[x for x in range(0, len(Displacement_vect))  if x not in constraint]
    for i in range(len(non_constraint)):
        Displacement_vect[non_constraint[i]]=compact_displacement[i]

    constraining_focre=[]
    for i in range(len(constraint)):
        constraining_focre.append(total_stiff[constraint[i]].dot(Displacement_vect)-total_load[constraint[i]])
    internal=[]
    stress=[]
    if dof == 2:
        internal_Force=[]
        for i in range(len(goc)):
            cos = round(math.cos(math.radians(goc[i])), 4)
            sin = round(math.sin(math.radians(goc[i])), 4)
            ele_Displacement=[]
            Ls=L[i]*sin
            Lc=L[i]*cos
            S_matrix=(E*A/L[i])*(np.array([-cos,-sin,cos,sin]))
            for j in range(len(ele[i])):
                ele_Displacement.append(Displacement_vect[ele[i][j]*dof])
                ele_Displacement.append(Displacement_vect[ele[i][j]*dof+1])
            internal_Force.append(S_matrix.dot(np.array(ele_Displacement)) )
            stress.append((S_matrix.dot(np.array(ele_Displacement))/A))
        internal=internal_Force
    elif dof == 3:
        internal_Moment=[]
        for i in range(len(goc)):
            ele_Displacement=[]
            Ls=L[i]*sin
            Lc=L[i]*cos
            S_matrix=(E*J/L[i]**3)*(np.array([[6*Ls,-6*Lc,-4*L[i]**2,-6*Ls,6*Lc,-2*L[i]**2],[-6*Ls,6*Lc,2*L[i]**2,6*Ls,-6*Lc,4*L[i]**2]]))
            for j in range(len(ele[i])):
                ele_Displacement.append(Displacement_vect[ele[i][j]*dof])
                ele_Displacement.append(Displacement_vect[ele[i][j]*dof+1])
                ele_Displacement.append(Displacement_vect[ele[i][j]*dof+2])
            temp=list(S_matrix.dot(np.array(ele_Displacement)) )
            if line_moment[i] != 0:
                internal_Moment.append({'Md':[0,line_moment[i]/4-temp[0],-line_moment[i]/2,line_moment[i]/2,-line_moment[i]/4-temp[1],0]})
            elif distributed_load[i] != 0:
                internal_Moment.append({'Fa':[0,(distributed_load[i]*L[i]/12)-temp[0],-distributed_load[i]*L[i]/24,(distributed_load[i]*L[i]/12)-temp[1],0]})
            elif center_load[i] != 0:
                internal_Moment.append({'Fs':[0,(center_load[i]*L[i]/8)-temp[0],-center_load[i]*L[i]/8,(center_load[i]*L[i]/8)-temp[1],0]})
            else:
               internal_Moment.append(temp)
            
        internal=internal_Moment

    return {'ts':total_stiff,'tl':total_load,'dv':Displacement_vect,'cf':constraining_focre,'internal':internal,'stress':stress,'dof':dof,'L':L}

#total_stiff        ma tran do cung k tong
#total_load         vector tong tai
#Displacement_vect  vector chuyen vi tong
#constraining_focre vector phan luc lien ket
#internal_Force     noi luc thanh [nut1, nut2]
#internal_Moment    noi moment [[nut1 nut2],[nut1 nut2]]
def diagram(dist,L,dof):
    if dof==3:
        for i in range(len(dist)):
            text="thanh "+ str(i+1)
            if 'Md' in dist[i]:
                a=plt.subplot(2,2,i+1)
                a.set_title(text)
                plt.plot([0,0,L[i]/2,L[i]/2,L[i],L[i]],dist[i]['Md'])
                plt.axhline(0, color='white')
                
            elif 'Fs' in dist[i]:
                a=plt.subplot(2,2,i+1)
                a.set_title(text)
                plt.plot([0 ,0, L[i]/2, L[i], L[i]] , dist[i]['Fs'])
                plt.axhline(0, color='white')

            elif 'Fa' in dist[i]:
                a=plt.subplot(2,2,i+1)
                a.set_title(text)
                A=np.array([[0,0,1],[(L[i]/2)**2,L[i]/2,1],[(L[i])**2,L[i],1]])
                parabol_fun=(np.linalg.inv(A)).dot(dist[i]['Fa'][1:4])
                x_cords=np.linspace(0,L[i],1000)
                y_cords=[(parabol_fun[0]*x**2+parabol_fun[1]*x+parabol_fun[2]) for x in x_cords]
                plt.plot([0,0],[0,dist[i]['Fa'][1]])
                plt.plot([L[i],L[i]],[dist[i]['Fa'][3],0])
                plt.scatter(x_cords, y_cords)
                plt.axhline(0, color='white')
            else :
                text="thanh "+ str(i+1)
                a=plt.subplot(2,2,i+1)
                a.set_title(text)
                plt.plot([0,0,L[i],L[i]],[0,dist[i][0],dist[i][1],0])
                plt.axhline(0, color='white')
        plt.show()
    elif dof==2:
        for i in range(len(dist)):
            text="thanh "+ str(i+1)
            a=plt.subplot(2,2,i+1)
            a.set_title(text)
            plt.plot([0,0,L[i],L[i]],[0,dist[i],dist[i],0])
            plt.axhline(0, color='white')
            
        plt.show()
    
            
#print(Ketqua(arr)['internal'])
#diagram((Ketqua(arr)['internal']),Ketqua(arr)['L'],Ketqua(arr)['dof'])
#Ketqua(arr)



