import numpy as np

class Stress:
    def __init__(self):
        pass
    
    def dump2stress(self,atom_id,radius_input,dumpforce):
        id_max=max(atom_id)
        atom=[0]*id_max
        radius=[0]*id_max
        stress=np.zeros([id_max,6])
        for i in range(len(atom_id)):
            atom[atom_id[i]]=atom_id[i]
            radius[atom_id[i]]=radius_input[i]
        for i in range(len(dumpforce)):
            m=int(dumpforce[i,7])
            n=int(dumpforce[i,8])
            ri=radius(m)
            rj=radius(n)
            L=ri+rj
            dxm=(dumpforce[i,1]-dumpforce[i,4])*ri/L
            dym=(dumpforce[i,2]-dumpforce[i,5])*ri/L
            dzm=(dumpforce[i,3]-dumpforce[i,6])*ri/L
            dxn=-(dumpforce[i,1]-dumpforce[i,4])*rj/L
            dyn=-(dumpforce[i,2]-dumpforce[i,5])*rj/L
            dzn=-(dumpforce[i,3]-dumpforce[i,6])*rj/L
            stress[m,1]+=dxm*dumpforce[i,10]
            stress[m,2]+=dym*dumpforce[i,11]
            stress[m,3]+=dzm*dumpforce[i,12]
            stress[m,4]+=dxm*dumpforce[i,11]
            stress[m,5]+=dxm*dumpforce[i,12]
            stress[m,6]+=dym*dumpforce[i,12]
            stress[n,1]+=dxn*dumpforce[i,10]
            stress[n,2]+=dyn*dumpforce[i,11]
            stress[n,3]+=dzn*dumpforce[i,12]
            stress[n,4]+=dxn*dumpforce[i,11]
            stress[n,5]+=dxn*dumpforce[i,12]
            stress[n,6]+=dyn*dumpforce[i,12]
        delete_list=list()
        for i in range(len(atom)):
            delete_list.append(i)
        atom.pop(0)
        radius.pop(0)
        np.delete(stress,delete_list,axis=0)
        return atom,radius,stress
