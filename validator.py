import requests

class Validator:
    API_BASE_URL = "https://api.cpfcnpj.com.br"

    # Inicializando os requests
    def __init__(self):
        self.api = requests.Session()

    # Função que valida o CNPJ
    def validate(self, query: int = 12, cnpj: str = "00000000000000"):
        # Tratamento do CNPJ
        cnpj = cnpj.replace(".", "").replace("-", "").replace("/", "") 

        # Tratamento de erros
        try:
            # Request à API
            response = self.api.get(f"{self.API_BASE_URL}/{self.API_BASE_TOKEN}/{query}/{cnpj}") 
            response.raise_for_status()
            
            return response.json() # Retorno do JSON
        
        # Tratando os erros HTTPs
        except requests.exceptions.HTTPError as err:
            error_msg = err.response.json()

            # Output do erro
            print("Erro na Requisição:")
            print(f"Código: {error_msg['erroCodigo']}")
            print(f"Mensagem: {error_msg['erro']}")

        # Tratando os erros de requisição
        except requests.exceptions.RequestException as err:
            # Output do erro
            print("Erro ao processar operação:")
            print(err)