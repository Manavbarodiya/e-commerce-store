// Checkout Page JavaScript

function renderCartItems() {
  const cart = loadCart();
  const tbody = document.getElementById('checkoutBody');
  const totalAmountEl = document.getElementById('totalAmount');
  const cartDataInput = document.getElementById('cartDataInput');
  const placeOrderBtn = document.getElementById('placeOrderBtn');

  // Clear existing rows
  tbody.innerHTML = '';

  // Populate cart data in hidden input
  cartDataInput.value = JSON.stringify(cart);

  const items = Object.values(cart);
  let total = 0;

  if (items.length === 0) {
    const row = document.createElement('tr');
    row.innerHTML = `<td colspan="5" style="text-align:center; color: #ff5252;">No items in cart. <a href="/cart/" style="color: #00ffc3;">Go to cart</a></td>`;
    tbody.appendChild(row);
    placeOrderBtn.disabled = true;
  } else {
    items.forEach(item => {
      const subtotal = item.price * item.quantity;
      total += subtotal;

      const row = document.createElement('tr');
      row.setAttribute('data-item-id', item.id);
      row.innerHTML = `
        <td>${item.name}</td>
        <td>
          <div class="quantity-control">
            <button type="button" class="quantity-btn minus-btn" data-item-id="${item.id}">-</button>
            <span class="quantity-value">${item.quantity}</span>
            <button type="button" class="quantity-btn plus-btn" data-item-id="${item.id}" ${item.quantity >= 5 ? 'disabled' : ''}>+</button>
          </div>
        </td>
        <td>₹${parseFloat(item.price).toFixed(2)}</td>
        <td>₹${subtotal.toFixed(2)}</td>
        <td>
          <button type="button" class="remove-item-btn" data-item-id="${item.id}">
            Remove
          </button>
        </td>
      `;
      tbody.appendChild(row);
    });

    // Add event listeners to quantity buttons
    tbody.querySelectorAll('.minus-btn').forEach(btn => {
      btn.addEventListener('click', function() {
        const itemId = this.getAttribute('data-item-id');
        decreaseQuantity(itemId);
      });
    });

    tbody.querySelectorAll('.plus-btn').forEach(btn => {
      btn.addEventListener('click', function() {
        const itemId = this.getAttribute('data-item-id');
        increaseQuantity(itemId);
      });
    });

    // Add event listeners to remove buttons
    tbody.querySelectorAll('.remove-item-btn').forEach(btn => {
      btn.addEventListener('click', function() {
        const itemId = this.getAttribute('data-item-id');
        removeItem(itemId);
      });
    });

    placeOrderBtn.disabled = false;
  }

  totalAmountEl.textContent = total.toFixed(2);
}

function decreaseQuantity(itemId) {
  let cart = loadCart();
  
  if (cart[itemId] && cart[itemId].quantity > 1) {
    cart[itemId].quantity--;
    saveCart(cart);
    renderCartItems(); // Re-render the cart items
  }
}

function increaseQuantity(itemId) {
  let cart = loadCart();
  
  if (cart[itemId] && cart[itemId].quantity < MAX_QTY) {
    cart[itemId].quantity++;
    saveCart(cart);
    renderCartItems(); // Re-render the cart items
  }
}

function removeItem(itemId) {
  let cart = loadCart();
  
  if (cart[itemId]) {
    // Remove the item entirely
    delete cart[itemId];
    saveCart(cart);
    renderCartItems(); // Re-render the cart items
  }
}

// Initialize checkout page when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  // Initial render
  renderCartItems();

  // Form submission handler
  const checkoutForm = document.getElementById('checkoutForm');
  if (checkoutForm) {
    checkoutForm.addEventListener('submit', function(e) {
      const cart = loadCart();
      const items = Object.values(cart);
      
      if (items.length === 0) {
        e.preventDefault();
        alert('Your cart is empty. Please add items before placing an order.');
        return false;
      }

      // Validate form fields
      const shippingAddress = document.getElementById('shipping_address').value.trim();
      const contactNumber = document.getElementById('contact_number').value.trim();

      if (!shippingAddress) {
        e.preventDefault();
        alert('Please enter a shipping address.');
        return false;
      }

      if (!contactNumber) {
        e.preventDefault();
        alert('Please enter a contact number.');
        return false;
      }

      // Disable button to prevent double submission
      const placeOrderBtn = document.getElementById('placeOrderBtn');
      if (placeOrderBtn) {
        placeOrderBtn.disabled = true;
        placeOrderBtn.textContent = 'Processing...';
      }
    });
  }
});

