# Simulador de Balança Incremental

Este aplicativo simula o envio de dados de peso para uma porta serial, útil para testar sistemas que leem pesos de balanças digitais. Ele utiliza a biblioteca Tkinter para criar uma interface gráfica e a biblioteca pySerial para comunicação serial.

## Funcionalidades

- Envia valores de peso incrementais para uma porta serial especificada.
- Suporta diferentes tipos de balanças (configuráveis via interface).
- Interface gráfica amigável para configuração e envio de dados.

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/seu-usuario/simulador-balanca-incremental.git
    cd simulador-balanca-incremental
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências necessárias:

    ```bash
    pip install pyserial
    ```

## Uso

1. É necessário ter ao menos uma porta COM disponível. Se a máquina que estiver rodando não possuir portas COM, podem ser utilizados sistemas de criam portas COM virtuais, como o Free Virtual Serial Ports, por exemplo.


2. Execute o script:

    ```bash
    python simulador_balanca.py
    ```

3. Na interface gráfica:
    - Selecione a porta serial.
    - Escolha o tipo de balança.
    - Ajuste o valor de peso conforme necessário.
    - Clique em "Enviar" para começar a enviar dados.
    - Clique em "Parar" para interromper o envio.


## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
