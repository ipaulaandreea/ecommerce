const ADD_TO_CART_BUTTON_CLASS = "add-to-cart";

let addToCart = (productId) => {
    console.log(productId);
    let sessionCart = sessionStorage.getItem("cart");
    cart = !sessionCart ? 
    {[productId]: {qty: 1}} : 
        updateQty(sessionCart, productId);
    sessionStorage.setItem("cart", JSON.stringify(cart));
}

let updateQty = (sessionCart, productId) => {
    let cart = JSON.parse(sessionCart);
    let product = cart[productId];
    if (product) {
        product.qty += 1;
    } else {
        product = {qty: 1};
    }

    cart[productId] = product;
    return cart;
}