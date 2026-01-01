// Cart Page JavaScript - Product add/remove functionality

// Initialize cart functionality when DOM is loaded
document.addEventListener('DOMContentLoaded', function() {
  // ADD BUTTON CLICK
  document.querySelectorAll('.add-btn').forEach(addBtn => {
    addBtn.addEventListener('click', () => {
      const id = addBtn.dataset.id;
      const name = addBtn.dataset.name;
      const price = parseFloat(addBtn.dataset.price);

      let cart = loadCart();
      let item = cart[id] || { id, name, price, quantity: 0 };

      if (item.quantity < MAX_QTY) {
        item.quantity++;
      }

      cart[id] = item;
      saveCart(cart);

      // Update UI
      addBtn.textContent = item.quantity;
      addBtn.style.background = '#000';
      addBtn.style.color = '#fff';

      // Show remove button when qty > 0
      const removeBtn = addBtn.parentNode.querySelector('.remove-btn');
      if (item.quantity > 0 && removeBtn) {
        removeBtn.style.display = 'inline-block';
      }

      // If quantity reaches max, stop
      if (item.quantity === MAX_QTY) {
        addBtn.textContent = MAX_QTY;
      }
    });
  });

  // REMOVE BUTTON CLICK
  document.querySelectorAll('.remove-btn').forEach(removeBtn => {
    removeBtn.addEventListener('click', () => {
      const id = removeBtn.dataset.id;
      let cart = loadCart();

      if (!cart[id]) return;

      cart[id].quantity--;

      // If quantity becomes 0 → remove item entirely
      if (cart[id].quantity <= 0) {
        delete cart[id];
      }

      saveCart(cart);

      // Update UI
      const addBtn = removeBtn.parentNode.querySelector('.add-btn');

      if (cart[id]) {
        addBtn.textContent = cart[id].quantity;
      } else {
        addBtn.textContent = 'Add';
        addBtn.style.background = '';
        addBtn.style.color = '';
        removeBtn.style.display = 'none';
      }
    });
  });
});

