<br>

<!-- Logo + Título + Descritivo -->
<div align="center">
  <img alt="Logo" src="logo.png" height="60">
   <h1>API MetaTrader 5</h1>
   <h6>Obtenha facilmente os valores de fechamento de ativos financeiros.</h6>
</div>

<!-- Links de navegação (centralizados) -->
<div align="center">
   <a href="#introducao">Introdução</a> •
   <a href="#funcionalidades">Funcionalidades</a> •
   <a href="#status">Status</a> •
   <a href="#exemplos">Exemplos de Uso </a> •
   <a href="#capturas">Capturas de Tela</a> •
   <a href="#instalacao">Instalação e Uso</a> •
   <a href="#contribuicoes">Contribuições</a> 
</div>
<br>
<!-- Badges de Gameficação -->
<div align="center">
    <img src="https://img.shields.io/badge/Nível-Expert-brightgreen" alt="Nível: Expert">
    <img src="https://img.shields.io/badge/XP-5000-yellow" alt="XP: 5000">
<img src="https://img.shields.io/badge/Investimento-Inteligente-blue" alt="Investimento: Inteligente">
    <img src="https://img.shields.io/badge/Traders-%20Profissionais-red" alt="Traders: Profissionais">
</div>


### Introdução <a id="introducao"></a>
Desenvolvi a "<b>API MetaTrader 5</b>", com o objetivo de fornecer informações atualizadas sobre os últimos valores de fechamento de ativos financeiros, com foco principal no mercado de câmbio. Com a API, você pode facilmente obter o valor mais recente de fechamento de ativos específicos, como moedas, e integrar esses dados em seus próprios aplicativos ou sistemas.

### Funcionalidades <a id="funcionalidades"></a>
A API oferece as seguintes funcionalidades principais:

- **📊 Obter Informações da API:** Você pode receber informações gerais sobre a API, incluindo seu nome, versão e detalhes do criador.

- **📈 Obter Último Fechamento de um Ativo Específico:** A API permite que você obtenha o valor mais recente de fechamento de um ativo específico, como EURUSD.

- **📉Obter Último Fechamento de Qualquer Ativo:** Além disso, você pode consultar o último valor de fechamento de qualquer ativo de sua escolha, passando o nome do ativo como parâmetro.

### Status <a id="status"></a>
O projeto está atualmente na <b>versão 1.0</b> e está em pleno funcionamento. Você pode usá-lo para obter informações sobre valores de fechamento de ativos financeiros.

### Exemplos de Uso <a id="exemplos"><img src="https://img.shields.io/badge/GET-brightgreen" alt="Método: GET"></a> 
Aqui estão alguns exemplos de como você pode usar esta API:

- Para obter informações gerais sobre a API
  ```
  /
  ```

- Para obter informações sobre a documentação da API:
  ```
  /docs#/
  ```

- Para obter o último valor de fechamento de <b>EURUSD</b>:
  ```
  /eur-usd
  ```

- Para obter o último valor de fechamento de qualquer ativo (<i>por exemplo, AUDCHF</i>):
  ```
  /ultimo_fechamento/?ativo=AUDCHF
  ```

### Capturas de Tela <a id="capturas"></a>

#### GIF demonstrativo
<img alt="Captura de tela" src="video_demo.gif" height="400">


#### Documentação
<img alt="Captura de tela" src="images/documentacao.png" height="400">


#### Em execução
<img alt="Captura de tela" src="images/api_execucao.png" height="200">


### Instalação <a id="instalacao"></a>
Para instalar e executar a API, siga os seguintes passos:

**Passo 1: Download e Instalação do Software**
- Acesse o [site oficial](https://www.metatrader5.com/pt/download) do MetaTrader 5, escolha <b>a versão adequada</b> para o seu sistema operacional, realize o download e faça a instalação.

**Passo 2: Instalação das Dependências**
```bash
pip install "fastapi[all]"
```

**Passo 3: Executar a API**
```bash
uvicorn main:app --reload
```

> Observe que o nome do seu arquivo deve ser 'main.py', e o nome da sua pasta deve ser diferente de 'app'. Para obter mais informações, consulte a [referência oficial](https://fastapi.tiangolo.com/tutorial/) ou outras [referências](https://www.hashtagtreinamentos.com/criar-api-com-fastapi-em-python).

### Contribuições <a id="contribuicoes"></a>
Se você deseja contribuir para o projeto, sinta-se à vontade para fazer isso. Você pode enviar pull requests com melhorias ou relatar problemas encontrados. Sua contribuição é valiosa para a melhoria contínua desta API.

### Licença
Este projeto é licenciado sob a Licença MIT. Para obter mais detalhes, consulte o arquivo [LICENSE](LICENSE.txt).

### Contato
Se você precisar de uma API personalizada, tiver dúvidas ou desejar entrar em contato para discutir o projeto, sinta-se à vontade para entrar em contato comigo através deste [e-mail](gustavoalerosas@.com).