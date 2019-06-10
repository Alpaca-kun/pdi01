# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 16:26:54 2015

@author: frank
"""

import numpy as np
#import cv2



# ndarray
#a = np.array([2,4,6,8,10])
#print "a:\n", a
#print "a.ndim:\n", a.ndim
#print "a.shape:\n", a.shape
#print "a.dtype:\n", a.dtype
#a.dtype = np.uint8
#print "a.dtype:\n", a.dtype


#a = np.array([[1,2,3,4],[5,6,7,8]])
#print "a:\n", a
#print "a.ndim:\n", a.ndim
#print "a.shape:\n", a.shape
#print "a.dtype:\n", a.dtype

#print np.zeros((3,3))
#print
#print np.ones((2,3))
#print
#print np.empty((2,2))
#print
#print np.empty((2,2),'bool')
#print
#print np.eye(3)

# arange e linspace
#print np.arange(5)
#print
#print np.arange(2,6)
#print
#print np.arange(0,2,0.5)
#print
#print np.linspace(0,2,5)

## Fatiamento (Slicing) (VETOR)
# exemplo
# indice negativo
# passo negativo
# supressao de indices e passo
#a = np.arange(15) * 10
#print a
#print
#print a[2:5]
#print
#print a[::3]
#print
#print a[-1::-1]


## Fatiamento (Slicing) (MATRIZ)
# exemplo
# linhas e colunas
# indices negativos e passo
#a = np.arange(49)
#a = a.reshape(7,7)
#print a
#print
#print a[::2,::2]
#b = np.copy(a)
#b[::2,::2] = 0
#print a
#print
#print b
#print
#print a
#print
#print a[::2,::2]


## Ravel
#a = np.arange(15)
#a = a.reshape(3,5)
#print a
#print
#print a.ravel()

## Copy
#a = np.arange(15)
#b = a.copy()
#c = a
#print a
#print
#print b
#print
#print c
#print
#print
#print
#a[:] = 2 * a
#print a
#print
#print b
#print
#print c

## Operacoes
#a = np.arange(6)
#a = a.reshape(2,3)
#b = np.array([1,3,2,4,2,1])
#b = b.reshape(3,2)
#print a
#print
#print b
#print
#print b.T
#print
#print a + b.T
#print
#print 3 * a
#print
#print a.dot(b)
#print
#print a * b.T

## Mais operacoes
#a = np.array([1,3,4,2])
#print a
#print
#a = np.array([[1,8,9,16],[2,7,10,15],[3,6,11,14],[4,5,12,13]])
#print a
#print
#print a.max()
#print a.min()
#print a.sum()
#print a.prod()
#print a.cumsum()
#print a.cumprod()
#print
#print a.max(0)
#print
#print a.sum(0)
#print
#print a.mean(0)
#print a.cumsum()
#print
#print a.cumsum(0)
#print a.cumprod(0)

## indices
#l,c = np.indices((4,5))
#print l
#print
#print c
#print
#print (l+c)%2
#print
#print l+c

## meshgrid
#a = np.array([-1.5,-1.0,-0.5,0.0,0.5])
#b = np.array([-20,-10,0,10,20,30])
# pode-se usar linspace para gerar os parametros 'a' e 'b'
#l,c = np.meshgrid(a,b,indexing='ij') 
#l,c = np.meshgrid(a,b) 
#print a
#print
#print b
#print
#print l
#print
#print c
#
#a = np.array([1,2,4,8,16,8,4,2,1])
#b = np.array([1,2,4,8,4,2,1])
#l,c = np.meshgrid(a,b,indexing='ij')
#x = l+c 
#print a
#print
#print b
#print
#print l
#print
#print c
#print
#print x

## nonzero
#a = np.array([0,32,0,14,0,0,83,0,110,0,0,21,0,0,0,0])
#(b,) = a.nonzero()
#print
#print a
#print
#print b
#print
#print a[b]
#print
#a = np.array([[0,32,0,14],[0,0,83,0],[110,0,0,21],[0,0,0,0]])
#(b,b2) = a.nonzero()
#print a
#print
#print b
#print
#print b2
#print
#print a[a.nonzero()]

# tile
#a = np.array([1,2,3])
#print a
#print
#print np.tile(a,5)
#print
#print np.tile(a,(2,3))
#print
#a = np.array([[1,2],[3,4]])
#print a
#print
#print np.tile(a,2)
#print
#print np.tile(a,(2,2))

# repeat
#a = np.array([[1,2],[3,4]])
#print a
#print
#print np.repeat(a,3,axis=0)
#print
#print np.repeat((np.repeat(a,3,axis=0)),3,axis=1)

# Falar do vstack, hstack e dstack
#a = np.array([[1,2],[3,4]])
#b = np.array([[5,6],[7,8]])
#
#print a
#print
#print b
#print
#print np.vstack((a,b))
#print
#print np.hstack((a,b))
#print
#print np.dstack((a,b))

## clip
#a = np.arange(20)
#print a
#print
#print np.clip(a,5,12)
#print
#a = a.reshape(4,5)
#print a
#print
#print np.clip(a,5,10)
#print

# sort
#a = np.array([8,5,3,1,7,4,9,2])
#print a
#print
#print np.sort(a)
#a = np.array([[3,15,6,12],[8,10,4,14],[5,1,9,16],[2,7,11,13]])
#print a
#print
#print np.sort(a)
#print
#print np.sort(a,axis=0)
#print
#print np.sort(a,axis=None)

# argsort
#a = np.array([8,5,3,1,6,4,7,2])
#idx = np.arange(8)
#print idx
#print
#print a
#print
#print np.argsort(a)
#print
#print a[np.argsort(a)]

##
