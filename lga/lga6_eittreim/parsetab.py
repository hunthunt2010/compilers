
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '4\xb3\x97,A\xac\t\xeb\xf9\xd8\x8f!\t\xb8\xa2\xf6'
    
_lr_action_items = {'rparen':([14,15,16,17,19,25,],[-12,-10,21,-11,23,-9,]),'begin':([0,1,13,23,24,28,],[1,1,1,1,1,1,]),'end':([7,8,12,14,15,17,18,20,25,29,30,32,],[12,-8,-6,-12,-10,-11,-2,-7,-9,-4,-5,-3,]),'semi':([7,8,12,14,15,17,18,20,25,29,30,32,],[13,-8,-6,-12,-10,-11,-2,-7,-9,-4,-5,-3,]),'do':([21,],[24,]),'else':([12,14,15,17,18,25,26,29,30,32,],[-6,-12,-10,-11,-2,-9,28,-4,-5,-3,]),'od':([12,14,15,17,18,25,27,29,30,32,],[-6,-12,-10,-11,-2,-9,30,-4,-5,-3,]),'assign':([5,],[10,]),'while':([0,1,13,23,24,28,],[4,4,4,4,4,4,]),'num':([9,10,11,22,],[14,14,14,14,]),'plus':([14,15,16,17,18,19,25,],[-12,-10,22,-11,22,22,-9,]),'lparen':([4,6,],[9,11,]),'fi':([12,14,15,17,18,25,26,29,30,31,32,],[-6,-12,-10,-11,-2,-9,29,-4,-5,32,-3,]),'if':([0,1,13,23,24,28,],[6,6,6,6,6,6,]),'id':([0,1,9,10,11,13,22,23,24,28,],[5,5,17,17,17,5,17,5,5,5,]),'$end':([2,3,12,14,15,17,18,25,29,30,32,],[-1,0,-6,-12,-10,-11,-2,-9,-4,-5,-3,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'Stmts':([1,],[7,]),'Start':([0,],[3,]),'E':([9,10,11,],[16,18,19,]),'T':([9,10,11,22,],[15,15,15,25,]),'Stmt':([0,1,13,23,24,28,],[2,8,20,26,27,31,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> Start","S'",1,None,None,None),
  ('Start -> Stmt','Start',1,'p_Start','p273-2.py',27),
  ('Stmt -> id assign E','Stmt',3,'p_Stmt','p273-2.py',31),
  ('Stmt -> if lparen E rparen Stmt else Stmt fi','Stmt',8,'p_Stmt','p273-2.py',32),
  ('Stmt -> if lparen E rparen Stmt fi','Stmt',6,'p_Stmt','p273-2.py',33),
  ('Stmt -> while lparen E rparen do Stmt od','Stmt',7,'p_Stmt','p273-2.py',34),
  ('Stmt -> begin Stmts end','Stmt',3,'p_Stmt','p273-2.py',35),
  ('Stmts -> Stmts semi Stmt','Stmts',3,'p_Stmts','p273-2.py',38),
  ('Stmts -> Stmt','Stmts',1,'p_Stmts','p273-2.py',39),
  ('E -> E plus T','E',3,'p_E','p273-2.py',42),
  ('E -> T','E',1,'p_E','p273-2.py',43),
  ('T -> id','T',1,'p_T','p273-2.py',46),
  ('T -> num','T',1,'p_T','p273-2.py',47),
]
