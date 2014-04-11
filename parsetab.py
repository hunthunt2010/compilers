
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\xde}P\x8e\xb98\xacOD\xe5{{Cg\xf1\x06'
    
_lr_action_items = {'const':([0,],[1,]),'identifier':([3,4,11,],[8,-6,-5,]),'$end':([2,6,10,],[0,-1,-2,]),'int':([0,1,7,],[4,-7,11,]),'semi':([5,8,9,],[10,-4,-3,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'START':([0,],[2,]),'DECL':([0,],[5,]),'TYPE':([0,],[3,]),'VARIABLE':([3,],[9,]),'STMT':([0,],[6,]),'MODIFIER':([0,],[7,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> START","S'",1,None,None,None),
  ('START -> STMT','START',1,'p_START','./scanner.py',42),
  ('STMT -> DECL semi','STMT',2,'p_STMT','./scanner.py',47),
  ('DECL -> TYPE VARIABLE','DECL',2,'p_DECL','./scanner.py',51),
  ('VARIABLE -> identifier','VARIABLE',1,'p_VARIABLE','./scanner.py',58),
  ('TYPE -> MODIFIER int','TYPE',2,'p_TYPE','./scanner.py',63),
  ('TYPE -> int','TYPE',1,'p_TYPE_INT','./scanner.py',68),
  ('MODIFIER -> const','MODIFIER',1,'p_MODIFIER','./scanner.py',73),
]
