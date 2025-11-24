
# FrutaCheck - Detector de Maturação de Frutas

**FrutaCheck** é um aplicativo web progressivo (PWA) que permite aos usuários analisarem o estágio de maturação de frutas (especificamente morangos, neste exemplo) através de uma foto. O aplicativo utiliza uma API em Flask (Python) com OpenCV para processar a imagem e um frontend responsivo para interação com o usuário.

## ✨ Funcionalidades

- **PWA (Progressive Web App):** Pode ser "instalado" na tela inicial de dispositivos móveis e funciona offline (cache de assets).
- **Captura de Imagem Dupla:** Permite tirar uma foto na hora com a câmera do dispositivo ou fazer upload de uma imagem da galeria.
- **Análise em Tempo Real:** Envia a imagem para um backend Python que utiliza OpenCV para processamento.
- **Análise de Cor (HSV):** Foca na região central da imagem e calcula a média de cor no espaço HSV para uma análise mais robusta sob diferentes iluminações.
- **Classificação de Maturação:** Classifica a fruta em três estágios: `Imaturo`, `Ideal` e `Maduro`.
- **Resultados Detalhados:**
    - Status textual e percentual de maturação.
    - Recomendação de ação (ex: "Colher agora", "Aguardar").
    - Detecção da cor RGB dominante com uma amostra visual.
- **Interface Responsiva:** Design mobile-first que se adapta a desktops e celulares.
- **Feedback Visual:** A cor do card de resultado muda de acordo com o status da maturação (Amarelo, Verde, Vermelho).

## 📂 Estrutura de Arquivos

```
/
|-- app.py               # Backend Flask com a lógica de análise
|-- static/              # Pasta para arquivos estáticos
|   |-- index.html       # Frontend da aplicação
|   |-- styles.css       # Folha de estilos
|   |-- app.js           # Lógica do frontend em JavaScript
|   |-- manifest.json    # Arquivo de manifesto do PWA
|   |-- icons/           # Ícones do PWA
|       |-- icon-192x192.png
|       |-- icon-512x512.png
|-- README.md            # Este arquivo
```

## 🚀 Instalação e Execução

### Pré-requisitos

- Python 3.x
- `pip` (gerenciador de pacotes do Python)

### 1. Instalação das Dependências

Navegue até o diretório raiz do projeto e execute o seguinte comando para instalar as bibliotecas Python necessárias:

```bash
pip install flask flask-cors opencv-python numpy
```

*(Observação: A biblioteca `Pillow` foi usada para gerar os ícones, mas não é necessária para a execução do aplicativo principal).*

### 2. Executando o Servidor

Após instalar as dependências, inicie o servidor Flask com o comando:

```bash
python app.py
```

O servidor estará rodando em `http://0.0.0.0:5000/`. Isso significa que ele está acessível por qualquer dispositivo na sua rede local.

### 3. Acessando o Aplicativo

1.  **No Computador:** Abra seu navegador e acesse `http://localhost:5000/static/index.html`.
2.  **No Celular (para testar a câmera):**
    a. Encontre o endereço IP local da sua máquina (ex: `192.168.1.10`).
    b. No navegador do seu celular, acesse `http://SEU_IP_LOCAL:5000/static/index.html` (substitua `SEU_IP_LOCAL` pelo seu IP).

### ❗️ Nota Importante sobre HTTPS e Câmera

Para que a funcionalidade de `Tirar Foto` (`capture="environment"`) funcione corretamente em dispositivos móveis, **o site precisa ser servido via HTTPS**. Durante o desenvolvimento local via HTTP, alguns navegadores móveis podem bloquear o acesso à câmera por questões de segurança.

Para produção, é essencial fazer o deploy da aplicação em um servidor com um certificado SSL/TLS configurado.

## 🔧 Como Usar

1.  Abra o aplicativo no seu navegador ou como um PWA instalado.
2.  Clique em **"📷 Tirar Foto"** para abrir a câmera do seu dispositivo ou em **"📁 Anexar Arquivo"** para selecionar uma imagem da sua galeria.
3.  Após selecionar a imagem, uma pré-visualização será exibida.
4.  Aguarde o processamento. Um ícone de carregamento aparecerá.
5.  O card de resultados será exibido com o status, percentual de maturação, recomendação e a cor dominante detectada.
6.  Você pode enviar uma nova foto a qualquer momento para uma nova análise.
