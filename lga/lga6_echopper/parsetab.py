
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = '\x1a5_\x8e\xa1\x8a\xe2&\x08{\x97\xe6\x18B\x951'
    
_lr_action_items = {'DO':([21,],[24,]),'BEGIN':([0,1,10,22,24,27,],[1,1,1,1,1,1,]),'END':([4,7,12,13,14,15,16,18,23,28,29,31,],[-2,12,-7,-3,-11,-9,-10,-1,-8,-5,-6,-4,]),'SEMI':([4,5,7,12,13,14,15,16,18,23,28,29,31,],[-2,10,10,-7,-3,-11,-9,-10,-1,-8,-5,-6,-4,]),'RPAREN':([14,15,16,17,19,23,],[-11,-9,-10,21,22,-8,]),'OD':([12,13,14,15,16,23,26,28,29,31,],[-7,-3,-11,-9,-10,-8,29,-5,-6,-4,]),'ELSE':([12,13,14,15,16,23,25,28,29,31,],[-7,-3,-11,-9,-10,-8,27,-5,-6,-4,]),'ID':([0,1,8,9,10,11,20,22,24,27,],[2,2,16,16,2,16,16,2,2,2,]),'WHILE':([0,1,10,22,24,27,],[3,3,3,3,3,3,]),'NUM':([8,9,11,20,],[14,14,14,14,]),'PLUS':([13,14,15,16,17,19,23,],[20,-11,-9,-10,20,20,-8,]),'LPAREN':([3,6,],[9,11,]),'FI':([12,13,14,15,16,23,25,28,29,30,31,],[-7,-3,-11,-9,-10,-8,28,-5,-6,31,-4,]),'$end':([4,5,12,13,14,15,16,18,23,28,29,31,],[-2,0,-7,-3,-11,-9,-10,-1,-8,-5,-6,-4,]),'ASSIGN':([2,],[8,]),'IF':([0,1,10,22,24,27,],[6,6,6,6,6,6,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'e':([8,9,11,],[13,17,19,]),'statements':([0,1,],[5,7,]),'t':([8,9,11,20,],[15,15,15,23,]),'statement':([0,1,10,22,24,27,],[4,4,18,25,26,30,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements SEMI statement','statements',3,'p_statements','./prob2.py',68),
  ('statements -> statement','statements',1,'p_statements','./prob2.py',69),
  ('statement -> ID ASSIGN e','statement',3,'p_statement','./prob2.py',76),
  ('statement -> IF LPAREN e RPAREN statement ELSE statement FI','statement',8,'p_statement','./prob2.py',77),
  ('statement -> IF LPAREN e RPAREN statement FI','statement',6,'p_statement','./prob2.py',78),
  ('statement -> WHILE LPAREN e RPAREN DO statement OD','statement',7,'p_statement','./prob2.py',79),
  ('statement -> BEGIN statements END','statement',3,'p_statement','./prob2.py',80),
  ('e -> e PLUS t','e',3,'p_e','./prob2.py',83),
  ('e -> t','e',1,'p_e','./prob2.py',84),
  ('t -> ID','t',1,'p_t','./prob2.py',91),
  ('t -> NUM','t',1,'p_t','./prob2.py',92),
]
