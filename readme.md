# Bitcoin Price Monitor 🪙

Uma aplicação web moderna para monitoramento em tempo real do preço do Bitcoin, com armazenamento de histórico e interface amigável.

## Funcionalidades ✨

- 📊 Monitoramento em tempo real do preço do Bitcoin
- 💽 Armazenamento em PostgreSQL para histórico de preços
- 🌐 Interface web responsiva e moderna
- 🔄 Atualização automática a cada 15 segundos
- 📱 Design adaptativo para dispositivos móveis
- 🎯 API REST para integração com outros sistemas

## Tecnologias Utilizadas 🛠️

- **Backend:**
  - Python 3.12+
  - Flask (Framework Web)
  - SQLAlchemy (ORM)
  - PostgreSQL (Banco de Dados)
  - Requests (API Client)

- **Frontend:**
  - HTML5
  - CSS3
  - JavaScript
  - Bootstrap 5
  
- **APIs:**
  - Coinbase API (Dados do Bitcoin)

## Configuração do Ambiente 🚀

### Pré-requisitos

- Python 3.12+
- pip (Gerenciador de pacotes Python)
- PostgreSQL

### Instalação

1. Clone o repositório:
```bash
git clone https://github.com/seu-usuario/bitcoin-price-monitor.git
cd bitcoin-price-monitor
```

2. Instale as dependências:
```bash
pip install -r requirements.txt
```

3. Configure as variáveis de ambiente:
```bash
cp .env.example .env
# Edite o arquivo .env com suas configurações
```

4. Execute a aplicação:
```bash
python main.py
```

5. Acesse a aplicação:
- Frontend: http://localhost:5000
- API: http://localhost:5000/get_price

## Estrutura do Projeto 📁

```
bitcoin-price-monitor/
├── main.py              # Aplicação principal
├── static/             # Arquivos estáticos
│   ├── css/           # Estilos
│   └── js/            # JavaScript
├── templates/         # Templates HTML
│   └── index.html    # Página principal
└── requirements.txt   # Dependências
```

## API Endpoints 📚

### GET /
- Retorna a interface web do monitor de preços

### GET /get_price
- Retorna o preço atual do Bitcoin em formato JSON
- Exemplo de resposta:
```json
{
    "valor": "45000.00",
    "cripto": "BTC",
    "moedas": "USD",
    "timestamp": "2025-05-15T10:30:00"
}
```

## Contribuindo 🤝

1. Faça um Fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Licença 📝

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## Contato 📧

Paulo - [@seutwitter](https://twitter.com/seutwitter)

Link do Projeto: [https://github.com/seu-usuario/bitcoin-price-monitor](https://github.com/seu-usuario/bitcoin-price-monitor)

