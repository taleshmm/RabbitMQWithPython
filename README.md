# 🐇 RabbitMQ com Python - Bot Telegram

Projeto didático que demonstra como integrar o **RabbitMQ** com **Python** usando um **bot no Telegram**. O objetivo é entender e aplicar os conceitos de mensageria com RabbitMQ de forma prática.

## 📌 Sobre o Projeto

Este projeto simula uma aplicação real de mensageria, onde as mensagens enviadas por usuários no Telegram são processadas usando uma **fila (queue)** do RabbitMQ. Ele é voltado para estudo e prática dos conceitos básicos de:

- Exchange
- Queue
- Bind
- Publicação e consumo de mensagens

A aplicação foi desenvolvida com fins **educacionais** para explorar o funcionamento de mensageria assíncrona com **RabbitMQ**.

## 📦 Funcionalidades

- Receber mensagens via Telegram
- Publicar mensagens no RabbitMQ
- Consumir mensagens da fila e processar (responder) no bot
- Separação clara entre **produtor** (bot) e **consumidor** (processador)

## 🚀 Como Executar

### 1. Pré-requisitos

- Python 3.8+
- Conta e bot criados no Telegram (obtenha um token com o [@BotFather](https://t.me/BotFather))
- RabbitMQ instalado e rodando localmente (`localhost:5672`) ou em nuvem

### 2. Instale as dependências

```bash
pip install -r requirements.txt
````

### 3. Configure as variáveis de ambiente

Crie um arquivo `.env` ou configure no próprio código:

```env
TOKEN=seu_token_do_bot
CHAT_ID=seu_chat_id
```

### 4. Execute os scripts

#### Produtor (envia mensagens para a fila a partir do Telegram)

```bash
python publisher.py
```

#### Consumidor (lê e processa mensagens da fila)

```bash
python consumer.py
```

> Obs.: Eles devem rodar **simultaneamente**, em terminais diferentes.

## 📚 Tecnologias Utilizadas

* Python
* RabbitMQ (via [pika](https://pika.readthedocs.io/))
* Telegram Bot API (via [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot))

## 🎯 Objetivos Didáticos

* Aprender os conceitos fundamentais de mensageria com RabbitMQ
* Aplicar a arquitetura produtor-consumidor em Python
* Usar filas para desacoplar serviços
* Praticar integração de APIs (Telegram)
