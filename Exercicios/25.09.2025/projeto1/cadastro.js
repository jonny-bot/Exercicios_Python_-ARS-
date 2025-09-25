let produtos = JSON.parse(localStorage.getItem('produtos')) || [];

const lista = document.getElementById('lista-produtos');
const nomeInput = document.getElementById('nome');
const precoInput = document.getElementById('preco');
const indiceInput = document.getElementById('indice');

function salvarProduto() {
  const nome = nomeInput.value.trim();
  const preco = parseFloat(precoInput.value);

  if (!nome || isNaN(preco)) {
    alert("Preencha todos os campos corretamente.");
    return false;
  }

  const produto = { nome, preco };

  const indice = indiceInput.value;
  if (indice === '') {
    // Novo produto
    produtos.push(produto);
  } else {
    // Editar produto existente
    produtos[indice] = produto;
    indiceInput.value = '';
  }

  localStorage.setItem('produtos', JSON.stringify(produtos));
  nomeInput.value = '';
  precoInput.value = '';
  atualizarLista();
  return false; // evita reload
}

function editarProduto(indice) {
  const produto = produtos[indice];
  nomeInput.value = produto.nome;
  precoInput.value = produto.preco;
  indiceInput.value = indice;
}

function removerProduto(indice) {
  if (confirm("Tem certeza que deseja remover este produto?")) {
    produtos.splice(indice, 1);
    localStorage.setItem('produtos', JSON.stringify(produtos));
    atualizarLista();
  }
}

function atualizarLista() {
  lista.innerHTML = '';
  produtos.forEach((produto, i) => {
    const li = document.createElement('li');
    li.innerHTML = `
      ${produto.nome} - R$${produto.preco.toFixed(2)}
      <button onclick="editarProduto(${i})">✏️</button>
      <button onclick="removerProduto(${i})">🗑️</button>
    `;
    lista.appendChild(li);
  });
}

function voltar() {
  window.location.href = "pdv.html";
}

atualizarLista();
