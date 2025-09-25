// Produtos disponíveis (carrega do localStorage)
const produtos = JSON.parse(localStorage.getItem('produtos')) || [
  { nome: 'Hambúrguer', preco: 15 },
  { nome: 'Batata Frita', preco: 8 }
];
