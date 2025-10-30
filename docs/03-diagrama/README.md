# 🐔 Sistema Inteligente de Controle Climático para Aviários (IoT Avicultura)

## ⚙️ Workflow do Sistema

O diagrama de fluxo de trabalho detalha a arquitetura operacional do sistema, que é dividida em quatro fases principais após a instalação:

### 1. Etapa de Configuração Inicial

Esta fase é realizada para preparar o ambiente e a infraestrutura de sensores:

* Início do Projeto (Levantamento de Requisitos).
* Definir Sensores Necessários.
* Selecionar Localização dos Sensores.
* Instalar Sensor de Umidade e Sensor de Temperatura.
* Instalar Circuitos para Monitoramento.
* Testar Funcionamento dos Sensores.

### 2. Etapa de Coleta e Monitoramento de Dados

O sistema inicia o ciclo de coleta em tempo real e persistência dos dados:

* Coletar Dados de Umidade e Coletar Dados de Temperatura.
* Monitorar Comportamento das Aves.
* Armazenar Dados no Servidor (Plataforma em Nuvem).
* Monitoramento Contínuo.

### 3. Etapa de Processamento, Análise e Ação

Esta é a fase de tomada de decisão e automação dinâmica:

* **Processar Dados Recebidos** e **Analisar Situações Críticas**.
* **Identificar Necessidade de Ação**.
    * **Se SIM:** O sistema **Ativa o Sistema de Climatização** (atuadores como ventiladores, exaustores e nebulizadores).
    * **Paralelamente à ativação,** o sistema **Envia Alertas para o Operador**, **Ajusta Parâmetros de Controle** e **Registra Ações Tomadas**.

### 4. Etapa de Avaliação de Resultados

Esta fase fecha o ciclo, garantindo a avaliação e a melhoria contínua do sistema (Feedback Loop):

* Avaliar Redução de Mortalidade.
* Avaliar Consumo Energético.
* Avaliar Índices Produtivos.
* Ajustar Sistema Conforme Resultados.

## 💻 Tecnologias e Componentes

| Categoria | Componentes/Tecnologias | Finalidade no Projeto |
| :--- | :--- | :--- |
| **Controlador** | ESP32 (Microcontrolador) | Processamento em tempo real e acionamento de atuadores. |
| **Sensores** | Temperatura, Umidade, $CO_2$ | Coleta contínua de variáveis ambientais. |
| **Atuadores** | Ventiladores, Exaustores, Nebulizadores | Controle dinâmico do microclima do aviário. |
| **Plataformas** | Node-RED ou Grafana | Plataformas em nuvem para visualização, análise e alertas. |
