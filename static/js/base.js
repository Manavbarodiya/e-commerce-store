// Base JavaScript - Common cart functionality

const MAX_QTY = 5;

// Load cart from localStorage
function loadCart() {
  return JSON.parse(localStorage.getItem('cart') || '{}');
}

// Save cart to localStorage
function saveCart(cart) {
  localStorage.setItem('cart', JSON.stringify(cart));
}

// Clear cart from localStorage
function clearCart() {
  localStorage.removeItem('cart');
}

