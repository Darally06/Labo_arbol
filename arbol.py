from typing import Any, List, Optional, Tuple
from images import *
from graphviz import Digraph

# Clase del nodo 
class Node:
    def __init__(self, archivo):
        self.data= archivo
        self.izq = None
        self.der= None
        self.padre = None
        self.altura = 1

# Clase del arbol
class AVL:
    def __init__(self, nodo):
        self.raiz = None

    # REEQUILIBRIO
    # Altura
    def altura_arbol(self, nodo):
        if nodo is None:
            return True
        aizq = self.altura_arbol(nodo.izq)
        ader = self.altura_arbol(nodo.der)
        return 1 + max(aizq, ader)

    # Factor de balanceo 
    def factor (self, nodo):
        if nodo is None:
            return 0
        return  self.altura_arbol(nodo.der) - self.altura_arbol(nodo.izq)

    # Funcion de equilibrio
    
    def equilibrio (self, nodo):
        while nodo is not None:
            factor_equilibrio = self.factor(nodo)

            if factor_equilibrio > 1 and nodo < raiz.izq:
                return self.rotar_derecha(raiz)
            if factor_equilibrio < -1 and nodo > raiz.der:
                return self.rotar_izquierda(raiz)
            if factor_equilibrio > 1 and nodo > raiz.izq:
                raiz.izq = self.rotar_derecha(raiz)
                return self.rotar_derecha(raiz)
            if factor_equilibrio < -1 and nodo > raiz. 
                if self.factor(nodo.der) >= 0:
                    nodo = self.rotar_izquierda(nodo)
                else:
                    None
                    #nodo = rot_doblederizq(nodo)
            elif factor_equilibrio < -1:
                if self.factor(nodo.izq) <= 0:
                    nodo = self.rotar_derecha(nodo)
                else:
                     None
                    #nodo = rot_doblederizq(nodo)
            nodo = nodo.padre
        return nodo
    
    #rotaciones
    def rotar_izquierda(self, nodo):
        hijo = nodo.der
        T2 = hijo.izq
        
        hijo.izq = nodo
        nodo.der = T2
        
        nodo.altura = 1 + max(self.altura_arbol(nodo.izq), self.altura_arbol(nodo.der))
        hijo.altura = 1 + max(self.altura_arbol(hijo.izq), self.altura_arbol(hijo.der))
        return hijo

    def rotar_derecha(self, hijo):
        nodo = hijo.izq
        T2 = nodo.der

        nodo.der = hijo
        hijo.izq= T2

        hijo.altura = 1 + max(self.altura_arbol(hijo.izq), self.altura_arbol(hijo.der))
        nodo.altura = 1 + max(self.altura_arbol(nodo.izq), self.altura_arbol(nodo.der))
        return nodo

    # 

    # Funciones
    # Buscar
def buscar(nodo, dato):
    if nodo is None:
        return "No esta"
    elif dato == nodo.data:
        return True
    elif dato < nodo.data:
        return buscar(nodo.izq, dato)
    else:
        return buscar(nodo.der, dato)





def imprimir_inorden(self, nodo):
        if nodo:
            self.imprimir_inorden(nodo.izquierda)
            print(f"Nombre: {nodo.nombre_archivo}")
            self.imprimir_inorden(nodo.derecha)


