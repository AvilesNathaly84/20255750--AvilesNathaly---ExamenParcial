class Recurso:
    def __init__(self, codigo_identificador: str):
        self.codigo_identificador = codigo_identificador
        self.multa = 0

    def calculo_multa(self):
        pass
        
class Bibliotecario:
    def __init__ (self, nombre_empleado: str, codigo_usuario: str):
        self.nombre_empleado = nombre_empleado
        self.codigo_usuario = codigo_usuario

class RegistroAtencion:
    def __init__(self, codigo_unico: str, carnet_alumno: str, nombre_empleado: str, codigo_usuario: str ):
        self.codigo_unico = codigo_unico
        self.carnet_alumno = carnet_alumno
        self._recursos: list[Recurso] = []
        self.bibliotecario = Bibliotecario(nombre_empleado, codigo_usuario)
        self.estado = "NORMAL"

    def cargarRecursos(self, recurso: Recurso):
        if len(self._recursos) >= 4:
            raise ValueError ("Límite de recursos por atención alcanzado")
        self._recursos.append(Recurso)

    def desvincularRecurso(self, codigo_identificador: str):
        if not self._recursos:
            print("La lista de recursos se encuentra vacia")
            return
        for r in self._recursos:
            if codigo_identificador == r.codigo_identificador:
                self._recursos.remove(r)
                return
        print("Codigo identificador no encontrado")

    def ejecutarRevision(self):
        if self.estado == "CUENTA_SUSPENDIDA":
            raise RuntimeError("Activación de protocolo de restriccion")

        if not self._recursos:
            print("No hay registros para ejecutar la revision")
            return

        promedioMulta = 0.0
        existeCodAux = False

        for r in self._recursos:
            r.calculo_multa()
            promedioMulta += r.multa
            if isinstance(r, UsoSaleEstudio):
                existeCodAux = True

        promedioMulta /= len(self._recursos)

        condicion_A = promedioMulta > 15.0
        condicion_B = (existeCodAux and UsoSaleEstudio > 10)

        if condicion_A or condicion_B:
            self.estado = "CUENTA_SUSPENDIDA"

@property
def recursos(self):
    return tuple(self._recursos)

class PrestamoLibro(Recurso):
    def __init__(self, codigo_identificador:str):
        super(self, codigo_identificador)
    
    def calculo_multa(self):
        self.multa += 2.5
        return self.multa

class UsoSaleEstudio(Recurso):
    def __init__(self, codigo_identificador):
        super().__init__(codigo_identificador)
    
    def calculo_multa(self, horas_exceso: int, factor: float):
        self.multa += horas_exceso * factor
        return self.multa