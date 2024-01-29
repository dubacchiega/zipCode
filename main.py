import requests

class CepFinder:
    def __init__(self, cep) -> None:
        self.cep = cep
        

    def getCep(self):
        self.response = requests.get(f'https://cep.awesomeapi.com.br/json/{self.cep}')
        return self.response.json()

    def error(self):
        resp = self.getCep()
        if 'invalid' in resp.values():
            return 'Erro. -> Cep Inválido'

    def address_type(self):
        try:
            resp = self.getCep()
            self.addressType = resp['address_type']
            return f'O tipo do endereço do CEP pesquisado é: {self.addressType}'
        except KeyError:
            return self.error()

    def address(self):
        try:
            resp = self.getCep()
            self._address = resp['address']
            return f'O endereço correspondente ao CEP pesquisado é: {self._address}'
        except KeyError:
            return self.error()
        
    
    def district(self):
        try:
            resp = self.getCep()
            self._district = resp['district']
            return f'O distrito correspondente ao CEP pesquisado é: {self._district}'
        except KeyError:
            return self.error()


    def latLng(self):
        try:
            resp = self.getCep()
            self.lat = resp['lat']
            self.lng = resp['lng']
            return f'A latitude correspondente ao CEP pesquisado é: {self.lat}, e sua longitude é: {self.lng}'
        except KeyError:
            return self.error()


    def city(self):
        try:
            resp = self.getCep()
            self._city = resp['city']
            return f'A cidade correspondente ao CEP é: {self._city}'
        except KeyError:
            return self.error()


    def ibge(self):
        try:
            resp = self.getCep()
            self.city_ibge = resp['city_ibge']
            return f'O IBGE da cidade correspondente ao CEP é: {self.city_ibge}'
        except KeyError:
            return self.error()

    def ddd(self):
        try:
            resp = self.getCep()
            self._ddd = resp['ddd']
            return f'O DDD da cidade correspondente ao CEP é: {self._ddd}'
        except KeyError:
            return self.error()

def choiceOption(option_):
    match option_:
        case 1:
            op = cep1.address_type()
            print(op)
        case 2:
            op = cep1.address()
            print(op)
        case 3:
            op = cep1.district()
            print(op)
        case 4:
            op = cep1.latLng()
            print(op)
        case 5:
            op = cep1.city()
            print(op)
        case 6:
            op = cep1.ibge()
            print(op)
        case 7:
            op = cep1.ddd()
            print(op)
        case _ :
            print('Opção Inválida')

if __name__ == '__main__':
    cep = input('Digite o cep que você deseja buscar: ')
    cep1 = CepFinder(cep)

    print('O que você deseja saber sobre esse CEP?')
    option = int(input(
        '1 - Tipo de Endereço\n'
        '2 - Endereço\n'
        '3 - Distrito\n'
        '4 - Latitude e Longitude\n'
        '5 - Cidade\n'
        '6 - IBGE da cidade\n'
        '7 - DDD da cidade\n'
        '-> '
        ))
    choiceOption(option)
