
# parsetab.py
# This file is automatically generated. Do not edit.
_tabversion = '3.2'

_lr_method = 'LALR'

_lr_signature = b'\xf0\xc6q\xfe\x84mz\xa6\xc3\xe4\xd7\xcc\xbeK\xf4a'
    
_lr_action_items = {'num':([3,9,12,14,17,20,],[8,8,8,8,8,8,]),'lp':([3,6,9,12,14,17,20,],[9,14,9,9,9,9,9,]),'lb':([26,31,],[28,32,]),'$end':([1,2,7,16,19,24,27,30,34,],[-1,0,-8,-7,-2,-4,-3,-5,-6,]),'sc':([8,10,11,13,18,22,23,25,],[-11,16,-10,19,24,-12,-9,27,]),'OP':([8,10,11,15,18,21,22,23,25,],[-11,17,-10,17,17,17,-12,17,17,]),'rb':([7,16,19,24,27,29,30,33,34,],[-8,-7,-2,-4,-3,30,-5,34,-6,]),'else':([30,],[31,]),'id':([0,1,3,5,7,9,12,14,16,17,19,20,24,27,28,29,30,32,33,34,],[4,4,11,13,4,11,11,11,-7,11,-2,11,-4,-3,4,4,-5,4,4,-6,]),'return':([0,1,7,16,19,24,27,28,29,30,32,33,34,],[3,3,3,-7,-2,-4,-3,3,3,-5,3,3,-6,]),'rp':([8,11,15,21,22,23,],[-11,-10,22,26,-12,-9,]),'if':([0,1,7,16,19,24,27,28,29,30,32,33,34,],[6,6,6,-7,-2,-4,-3,6,6,-5,6,6,-6,]),'assign':([4,13,],[12,20,]),'TYPE':([0,1,7,16,19,24,27,28,29,30,32,33,34,],[5,5,5,-7,-2,-4,-3,5,5,-5,5,5,-6,]),}

_lr_action = { }
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = { }
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'START':([0,],[2,]),'STMTS':([0,1,7,28,29,32,33,],[1,7,7,29,7,33,7,]),'EXPR':([3,9,12,14,17,20,],[10,15,18,21,23,25,]),}

_lr_goto = { }
for _k, _v in _lr_goto_items.items():
   for _x,_y in zip(_v[0],_v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = { }
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> START","S'",1,None,None,None),
  ('START -> STMTS','START',1,'p_START','C:/PyWorkspace/LGA7/LGA7.py',72),
  ('STMTS -> TYPE id sc','STMTS',3,'p_STMTS_VAR_DCL','C:/PyWorkspace/LGA7/LGA7.py',79),
  ('STMTS -> TYPE id assign EXPR sc','STMTS',5,'p_STMTS_VAR_DCL','C:/PyWorkspace/LGA7/LGA7.py',80),
  ('STMTS -> id assign EXPR sc','STMTS',4,'p_STMTS_ASSIGN','C:/PyWorkspace/LGA7/LGA7.py',89),
  ('STMTS -> if lp EXPR rp lb STMTS rb','STMTS',7,'p_STMTS_IF','C:/PyWorkspace/LGA7/LGA7.py',95),
  ('STMTS -> if lp EXPR rp lb STMTS rb else lb STMTS rb','STMTS',11,'p_STMTS_IF_ELSE','C:/PyWorkspace/LGA7/LGA7.py',101),
  ('STMTS -> return EXPR sc','STMTS',3,'p_STMTS_RETURN','C:/PyWorkspace/LGA7/LGA7.py',107),
  ('STMTS -> STMTS STMTS','STMTS',2,'p_STMTS_STMTS','C:/PyWorkspace/LGA7/LGA7.py',113),
  ('EXPR -> EXPR OP EXPR','EXPR',3,'p_EXPR_OP','C:/PyWorkspace/LGA7/LGA7.py',119),
  ('EXPR -> id','EXPR',1,'p_EXPR_ID_NUM','C:/PyWorkspace/LGA7/LGA7.py',125),
  ('EXPR -> num','EXPR',1,'p_EXPR_ID_NUM','C:/PyWorkspace/LGA7/LGA7.py',126),
  ('EXPR -> lp EXPR rp','EXPR',3,'p_EXPR_PAREN','C:/PyWorkspace/LGA7/LGA7.py',132),
]