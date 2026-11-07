class Reserva:

    def __init__(self, request):

        self.request = request

        self.session = request.session

        reserva = self.session.get("reserva")

        if not reserva:
            reserva = self.session["reserva"] = {}

        self.reserva = reserva

    def guardar(self):
        self.session.modified = True

    def agregar(self, material):

        id = str(material.id)

        if id not in self.reserva:

            self.reserva[id] = {
                "cantidad": 1,
                "precio": float(material.precio_referencia)
            }

        else:
            self.reserva[id]["cantidad"] += 1

            self.guardar()

    def eliminar(self, material):

        id = str(material.id)

        if id in self.reserva:

            del self.reserva[id]

            self.guardar()

    def limpiar(self):

        self.session["reserva"] = {}

        self.guardar()