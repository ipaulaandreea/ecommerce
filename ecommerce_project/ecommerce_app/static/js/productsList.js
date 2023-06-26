const ADD_TO_CART_BUTTON_CLASS = "add-to-cart";

let addToCart = (productId) => {
    console.log(productId);
    let localSessionCart = localStorage.getItem("cart");
    let cart = 
        !localSessionCart ? 
        {[productId]: {qty: 1}} : 
        updateQty(localSessionCart, productId);
    localStorage.setItem("cart", JSON.stringify(cart));
    window.location.href = '/cart';
}

let updateQty = (localSessionCart, productId) => {
    let cart = JSON.parse(localSessionCart);
    let product = cart[productId];
    if (product) {
        product.qty += 1;
    } else {
        product = {qty: 1};
    }

    cart[productId] = product;
    return cart;
}