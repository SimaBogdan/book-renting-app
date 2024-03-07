from repository.carteRepository import CarteRepository
from repository.clientiRepository import ClientiRepository
from repository.inchiriereRepository import InchiriereRepository
from service.cartiService import CartiService
from service.clientiService import ClientiService
from service.inchiriereService import InchiriereService
from ui.ui import UI
from teste.testAll import testAll

def main():

    testAll()

    cartiRepository = CarteRepository()
    clientiRepository = ClientiRepository()

    cartiService = CartiService(cartiRepository)
    clientiService = ClientiService(clientiRepository)
    inchirieriService = InchiriereService(cartiRepository, clientiRepository)
    
    ui = UI(cartiService, clientiService, inchirieriService)

    ui.meniu()
    

main()