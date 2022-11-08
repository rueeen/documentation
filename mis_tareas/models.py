from django.db import models

# Create your models here.


class Tarea:
    def __init__(self, titulo, descr, importancia):
        self.titulo = titulo
        self.descr = descr
        self.importancia = importancia


class Listado:
    def __init__(self):
        t1 = Tarea('Tarea 1', 'asdlhadh ahdoisa hdias', 10)
        t2 = Tarea('Tarea 2', 'asdlhadh ahdoisa hdias', 2)

        self.mi_lista = [t1, t2]

    def agregar(self, tarea):
        """
        If the list contains a task with the same title as the one being added, return a message saying
        that the task already exists. Otherwise, add the task to the list and return a message saying
        that the task was added
        
        :param tarea: is the task that is going to be added to the list
        :return: The return value is a string.
        """
        for t in self.mi_lista:
            if isinstance(t, Tarea) and isinstance(tarea, Tarea):
                if t.titulo == tarea.titulo:
                    return 'Tarea ya existe'
        self.mi_lista.append(tarea)
        return 'Tarea agregada'

    def eliminar(self, titulo):
        """
        It removes the first instance of a task with the given title from the list of tasks
        
        :param titulo: The title of the task
        :return: The return value is a string.
        """
        for t in self.mi_lista:
            if isinstance(t, Tarea):
                if t.titulo == titulo:
                    self.mi_lista.remove(t)
                    return 'Tarea eliminada'
        return 'Tarea no existe'

    def listar(self):
        return self.mi_lista

    def ordenarTareas(self):
        """
        It sorts the list of tasks by importance, in descending order
        :return: The sorted list of tasks.
        """
        return sorted(self.mi_lista, key=lambda x: x.importancia, reverse=True)
