function updatePrice() {
    fetch('/get_price')
        .then(response => response.json())
        .then(data => {
            document.getElementById('btc-price').textContent = data.valor;
            document.getElementById('last-update').textContent = new Date().toLocaleString();
        })
        .catch(error => console.error('Erro:', error));
}

// Atualiza o preço a cada 15 segundos
setInterval(updatePrice, 15000);
