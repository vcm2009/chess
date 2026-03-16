
class P():
  def __init__(self,color,type,coord):
    self.color=color
    self.type=type
    self.coord=coord
    if self.type=="Roi":
      self.move,self.max=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)],1
#      self.sym=
    elif self.type=="Reine":
      self.move,self.max=[(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,-1),(1,-1),(-1,1)],8
      self.value=9
#      self.sym=
    elif self.type=="Cavalier":
      self.move,self.max=[(2,1),(2,-1),(-2,1),(-2,-1),(1,2),(1,-2),(-1,2),(-1,-2)],1
      self.value=3
#      self.sym=
    elif self.type=="Fou":
      self.move,self.max=[(1,1),(-1,-1),(1,-1),(-1,1)],8
      self.value=3
#      self.sym=
    else:
      self.move,self.max=[(1,0),(-1,0),(0,1),(0,-1)],8
      self.value=5
  def __str__(self):return self.type+" "+str(self.color)  
  def __repr__(self): return self.__str__()
  def legal_move(self,check):
    M,D,A=[],[],[]
    for dx,dy in self.move:
      for i in range(1,self.max+1):
        x=self.coord[0]+(i*dx)
        y=self.coord[1]+(i*dy)
        if not (1<=x<=8 and 1<=y<=8):break
        if check==0:
          if testsiechec(self,[x,y])==True:break
        piece=testifpiece([x,y])
        if piece==None:
          M.append([x,y])
        elif piece.color==self.color:
          D.append([x,y])
          break
        else:
          A.append([x,y])
          break      
    return cleareturn(M,D,A) 

class color():
  def __init__(self,l1,l2,name):
    self.color=name
    self.R,self.D=P(self,"Roi",[5,l1]),P(self,"Reine",[5,l2])
    self.C1,self.C2=P(self,"Cavalier",[2,l1]),P(self,"Cavalier",[7,l1])
    self.F1,self.F2=P(self,"Fou",[3,l1]),P(self,"Fou",[6,l1])
    self.T1,self.T2=P(self,"Tour",[1,l1]),P(self,"Tour",[8,l1])
#  P1 = P(self,"Pion",[1,l2])
#  P2 = P(self,"Pion",[2,l2])
#  P3 = P(self,"Pion",[3,l2])
#  P4 = P(self,"Pion",[4,l2])
#  P5 = P(self,"Pion",[5,l2])
#  P6 = P(self,"Pion",[6,l2])
#  P7 = P(self,"Pion",[7,l2])
#  P8 = P(self,"Pion",[8,l2])
#  B=[BR,BD,BC1,BC2,BF1,BF2,BT1,BT2,BP1,BP2,BP3,BP4,BP5,BP6,BP7,BP8]
    self.L=[self.R,self.D,self.C1,self.C2,self.F1,self.F2,self.T1,self.T2]
  def __iter__(self):return iter(self.L)
  def __add__(self,other):return other.L + self.L
  def __getitem__(self,index):return self.L[index]
  def __str__(self):return str(self.color)  
  def __repr__(self): return self.__str__()

def testifpiece(coord):
  for pieces in B + N:
    if pieces.coord==coord:
      return pieces    

def analyserdynamiques(color):
  pass
  
def testsiendanger(victime,check):
  A=[]
  for attaquant in inversercolor(victime.color):
    if victime.coord in attaquant.legal_move(check)[2]:
      A.append(attaquant)
  return A

def testsidefendue(victime):
  D=[]
  for defenseur in victime.color:
    if victime.coord in defenseur.legal_move(0)[1]:
      D.append(defenseur)
  return D

def testsiechec(self, coord):
    BACKUP = self.coord
    self.coord = coord
    attaquants = testsiendanger(self.color.R, 1)
    self.coord = BACKUP
    if not attaquants:return False
    else:return True
    
def inversercolor(color):
  if color==B:return N
  else: return B

def cleareturn(M,D,A):
  M = [item for item in M if item != []]
  D = [item for item in D if item != []]
  A = [item for item in A if item != []]
  return M, D, A
  
B=color(1,2,"Blanc")
N=color(8,7,"Noir")


