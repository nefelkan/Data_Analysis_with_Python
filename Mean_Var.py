import numpy as np

def calculate(list):
    if (len(list) != 9):
        raise ValueError("List must contain nine numbers.")
    
    a = np.array(list)
    b = a.reshape(3,3)
    c = []
    c = [
          [b.mean(axis=0) , b.mean(axis=1) , b.mean()],
          [b.var(axis=0) , b.var(axis=1) , b.var()] , 
          [b.std(axis=0) , b.std(axis=1) , b.std()] , 
          [b.max(axis=0) , b.max(axis=1) , b.max()] , 
          [b.min(axis=0) , b.min(axis=1) , b.min()] , 
          [b.sum(axis=0) , b.sum(axis=1) , b.sum()]
        ]

    calculations = {}
    calculations = {'mean' : [c[0][0].tolist() , c[0][1].tolist() , c[0][2].tolist()] , 
                    'variance' : [c[1][0].tolist() , c[1][1].tolist() , c[1][2].tolist()] , 
                    'standard deviation' : [c[2][0].tolist() , c[2][1].tolist() , c[2][2].tolist()] , 
                    'max' : [c[3][0].tolist() , c[3][1].tolist() , c[3][2].tolist()] , 
                    'min' : [c[4][0].tolist() , c[4][1].tolist() , c[4][2].tolist()] , 
                    'sum' : [c[5][0].tolist() , c[5][1].tolist() , c[5][2].tolist()]
                  }



    return calculations


if __name__ == '__main__' :
    print(calculate([0,1,2,3,4,5,6,7,8]))