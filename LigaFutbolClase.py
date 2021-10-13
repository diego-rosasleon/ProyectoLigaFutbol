# -*- coding: utf-8 -*-

from _typeshed import SupportsReadline
from EquipoClase import Equipo
class LigaFutbol:
    
    def __init_(self):
        """
        Inicializa una lista vacía
        Parameters:
        none
        """
        self.__equipos = []
        self.__total_equipo = 0
    
    def agregarEquipo(self,equipo):
        """
        Agrega a la lista a un equipo
        Parameters:
        equipo: Equipo -- objeto de la clase equipo
        """
        if not (self.__existe(equipo)):
            print("Existe...")
            self.__equipos.append(equipo)
            self.__total_equipo+=1
        else:
            print("Ya existe el equipo en la lista");
    
    def __existe(self, equipo):
        """
        Checa si el equipo existe
        Parameters:
        equipo: Equipo -- objeto de la clase equipo
        """
        for item in self.__equipos:
            if equipo.getNombre()== item.getNombre()and equipo.getEntrenador()== item.getEntrenador() and equipo.getEstadio()== item.getEstadio() and equipo.getPuntos()== item.getPuntos():
                return True
        return False
    
    def tam(self):
        """
        Arroja el número de equipos en la liga
        Parameters:
        none
        """
        return self.__total_equipo

    def mayor(self):
        """
        Devuelve el equipo con más puntos en la liga
        Parameters:
        none
        """
        mas_grande = self.__equipos[0]
        mas_grandes = []
        for item in self.__equipos:
            if mas_grande.getPuntos()<= item.getPuntos():
                if mas_grande.getPuntos()< item.getPuntos():
                    mas_grande = item
                    mas_grandes = []
                else:
                    mas_grandes.append(item)
        if len(mas_grandes) > 0:
            resultado = mas_grandes.append(mas_grande)
        else:
            resultado = mas_grande
        return resultado

    def menor(self):
        """
        Devuelve el equipo con menos puntos en la liga
        Parameters:
        none
        """
        mas_peque = self.__equipos[0]
        mas_peques = []
        for item in self.__equipos:
            if mas_peque.getPuntos()>= item.getPuntos():
                if mas_peque.getPuntos()> item.getPuntos():
                    mas_peque = item
                    mas_peques = []
                else:
                    mas_peques.append(item)
        if len(mas_peques) > 0:
            resultado = mas_peques.append(mas_peque)
        else:
            resultado = mas_peque
        return resultado

    def entrenadores(self):
        """
        Devuelve el equipo con menos puntos en la liga
        Parameters:
        none
        """
        self.entrenadores_lista = []
        for item in self.__equipos:
            self.entrenadores_lista.append(item.getEntrenador())
        return self.entrenadores_lista

    def puntuacion(self, equipo):
        """
        Devuelve el número de puntos de un equipo
        Parameters:
        equipo: Equipo -- objeto de la clase equipo
        """
        if (self.__existe(equipo)):
            return equipo.getPuntos()
        else:
            print("No existe el equipo en la lista.")
     
    def estadio(self, equipo):
        """
        Devuelve el estadio de un equipo
        Parameters:
        equipo: Equipo -- objeto de la clase equipo
        """
        if (self.__existe(equipo)):
            return equipo.getEstadio()
        else:
            print("No existe el equipo en la lista.")

    def entrenador(self, equipo):
        """
        Devuelve el entrenador de un equipo
        Parameters:
        equipo: Equipo -- objeto de la clase equipo
        """
        if (self.__existe(equipo)):
            return equipo.getEntrenador()
        else:
            print("No existe el equipo en la lista.")



    def eq_por_puntos(self,puntos):
        """
        Devuelve el equipo dado los puntos
        Parameters:
        puntos: int -- número de puntos dado
        """
        self.lista_por_puntos = []
        for item in self.__equipos:
            if puntos == item.getPuntos():
                self.lista_por_puntos.append(item)
        if len(self.lista_por_puntos) > 0:
            return self.lista_por_puntos
        else:
            print("No existe un equipo con ese puntaje en la lista.")


        

        


    














 
        
