let pedido = [];
let total = 0;

function adicionarProduto(nome, preco) {
  pedido.push({ nome, preco });
  total += preco;
  atualizarTela();
}

function atualizarTela() {
  const lista = document.getElementById('lista-pedido');
  const totalSpan = document.getElementById('total');

  lista.innerHTML = '';

  pedido.forEach((item, index) => {
    const li = document.createElement('li');
    li.textContent = `${item.nome} - R$${item.preco.toFixed(2)}`;
    lista.appendChild(li);
  });

  totalSpan.textContent = total.toFixed(2);
}

function finalizarPedido() {
  if (pedido.length === 0) {
    alert('Nenhum produto no pedido!');
    return;
  }

  let resumo = "Resumo do Pedido:\n";
  pedido.forEach(item => {
    resumo += `- ${item.nome} - R$${item.preco.toFixed(2)}\n`;
  });
  resumo += `\nTotal: R$${total.toFixed(2)}`;
  
  alert(resumo);

  // Resetar pedido
  pedido = [];
  total = 0;
  atualizarTela();
}
