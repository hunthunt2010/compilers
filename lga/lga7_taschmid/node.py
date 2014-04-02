#! /usr/bin/env python

####################################################################
#abstract class for nodes in AST
class abstractNode:
	def __init__(self, astLevel, parent, rSib, lftMstSib):
		self.astLevel = astLevel
		self.parent = parent
		self.rSib = rSib
		self.lftMstSib = lftMstSib
		
		#index 0 in child list = left most child
		children = []

	def changeParent(newParent):
		self.parent = newParent

	def changeRSib(newRSib):
		self.rSib = newRSib

	def changeLftMstSib(newLftMstSib):
		lftMstSib = newLftMstSib

	def addChild(newChild, index):
		children.insert(index, newChild)

	def nodeFunction:
		print 'Abstract Node: No Function'

####################################################################
#child classes for each type of node in AST
class intNode(abstractNode):
	def nodeFunction:
		#do stuff

class idNode(abstractNode):
	def setId(id):
		self.id = id

	def nodeFunction:
		#do stuff

class assignNode(abstractNode):
	def nodeFunction:
		#do stuff

class numNode(abstractNode):
	def setNum(num):
		self.num = num

	def nodeFunction:
		#do stuff

class ifNode(abstractNode):
	def nodefunction:
		#do stuff

class elseNode(abstractNode):
	def nodeFunction:
		#do stuff

class returnNode(abstractNode):
	def nodeFunction:
		#do stuff

class ltNode(abstractNode):
	def nodeFunction:
		#do stuff

class gtNode(abstractNode):
	def nodeFunction:
		#do stuff

class lteNode(abstractNode):
	def nodefunction:
		#do stuff

class gteNode(abstractNode):
	def nodeFunction:
		#do stuff