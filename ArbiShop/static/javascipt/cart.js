/**
 * @file This file handles the shopping cart functionality, including adding products to the cart, saving and loading the cart from localStorage, and updating the cart count in the UI.
 */

/**
 * @class Cart
 * @description Manages the shopping cart by handling product additions, cart persistence, and UI updates.
 */
class Cart {
    constructor() {
        this.cart = this.loadCart();
        this.updateCartCount();
        this.initEventListeners();
    }

    /**
     * Loads the cart from localStorage. If no cart exists, returns an empty object.
     * @returns {Object} The cart object.
     */
    loadCart() {
        return localStorage.getItem('cart') ? JSON.parse(localStorage.getItem('cart')) : {};
    }

    /**
     * Saves the current cart to localStorage.
     */
    saveCart() {
        localStorage.setItem('cart', JSON.stringify(this.cart));
    }

    /**
     * Adds a product to the cart. If the product already exists, increments its quantity.
     * @param {Object} product - The product object to add to the cart.
     */
    addToCart(product) {
        if (this.cart[product.id]) {
            this.cart[product.id].quantity += 1;
        } else {
            this.cart[product.id] = product;
        }
        this.saveCart();
        this.updateCartCount();
    }

    /**
     * Updates the displayed cart count based on the total quantity of items in the cart.
     */
    updateCartCount() {
        let totalItems = Object.values(this.cart).reduce((total, item) => total + item.quantity, 0);
        const cartCountElement = document.getElementById('cart-count');
        if (cartCountElement) {
            cartCountElement.textContent = totalItems;
        }
    }

    /**
     * Initializes event listeners for adding products to the cart.
     */
    initEventListeners() {
        const addToCartBtn = document.getElementById('add-to-cart-btn');
        if (addToCartBtn) {
            addToCartBtn.addEventListener('click', () => {
                let product = {
                    id: addToCartBtn.dataset.productId,
                    name: addToCartBtn.dataset.productName,
                    price: parseFloat(addToCartBtn.dataset.productPrice),
                    image: decodeURIComponent(addToCartBtn.dataset.productImageUrl), // Ensure the URL is decoded correctly
                    quantity: 1
                };
                this.addToCart(product);
            });
        }
    }
}

let cart;

/**
 * Initializes or updates the cart by creating a new Cart instance or reloading it.
 */
function updateCart() {
    if (!cart) {
        cart = new Cart();
    } else {
        cart.cart = cart.loadCart();
        cart.updateCartCount();
    }
}

document.addEventListener('DOMContentLoaded', updateCart);

window.addEventListener('pageshow', (event) => {
    if (event.persisted) {
        updateCart();
    }
});
