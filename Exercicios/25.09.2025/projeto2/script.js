const products = [
  { id: 1, name: "Hambúrguer", price: 12.99 },
  { id: 2, name: "Batata Frita", price: 7.99 },
  { id: 3, name: "Refrigerante", price: 5.49 },
  { id: 4, name: "Milkshake", price: 9.99 },
  { id: 5, name: "Salada", price: 6.5 },
];

const productList = document.getElementById("product-list");
const orderList = document.getElementById("order-list");
const totalPriceEl = document.getElementById("total-price");
const finishOrderBtn = document.getElementById("finish-order");
const paymentForm = document.getElementById("payment-form");

let order = [];

function formatPrice(price) {
  return price.toLocaleString("pt-BR", { style: "currency", currency: "BRL" });
}

function renderProducts() {
  productList.innerHTML = "";
  products.forEach(({ id, name, price }) => {
    const productDiv = document.createElement("div");
    productDiv.classList.add("product");
    productDiv.innerHTML = `
      <div>
        <div class="product-name">${name}</div>
        <div class="product-price">${formatPrice(price)}</div>
      </div>
      <div class="product-actions">
        <input type="number" min="1" value="1" id="qty-${id}" />
        <button data-id="${id}">Adicionar</button>
      </div>
    `;
    productList.appendChild(productDiv);

    const btn = productDiv.querySelector("button");
    btn.addEventListener("click", () => {
      const qtyInput = productDiv.querySelector("input");
      let qty = parseInt(qtyInput.value);
      if (qty < 1 || isNaN(qty)) qty = 1;
      addToOrder(id, qty);
      qtyInput.value = 1; // resetar
    });
  });
}

function addToOrder(productId, quantity) {
  const product = products.find((p) => p.id === productId);
  if (!product) return;

  const existingItem = order.find((item) => item.id === productId);
  if (existingItem) {
    existingItem.quantity += quantity;
  } else {
    order.push({ ...product, quantity });
  }
  renderOrder();
}

function removeFromOrder(productId) {
  order = order.filter((item) => item.id !== productId);
  renderOrder();
}

function renderOrder() {
  orderList.innerHTML = "";
  let total = 0;

  order.forEach(({ id, name, price, quantity }) => {
    total += price * quantity;

    const li = document.createElement("li");
    li.innerHTML = `
      <span class="qty">${quantity}x</span>
      <span class="name">${name}</span>
      <span class="price">${formatPrice(price * quantity)}</span>
      <button class="remove-btn" data-id="${id}">Remover</button>
    `;

    const removeBtn = li.querySelector(".remove-btn");
    removeBtn.addEventListener("click", () => removeFromOrder(id));

    orderList.appendChild(li);
  });

  totalPriceEl.textContent = formatPrice(total);

  finishOrderBtn.disabled = order.length === 0;
}

finishOrderBtn.addEventListener("click", () => {
  if (order.length === 0) {
    alert("Seu pedido está vazio!");
    return;
  }
  const paymentMethod = paymentForm.payment.value;
  alert(
    `Pedido finalizado!\nTotal: ${totalPriceEl.textContent}\nPagamento: ${paymentMethod}`
  );
  order = [];
  renderOrder();
});

renderProducts();
renderOrder();
