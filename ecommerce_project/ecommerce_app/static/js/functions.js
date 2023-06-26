$(document).ready(function() {
  console.log( "ready!" );
  displayCart();
});

let displayCart = () => {
  let localSessionCart = localStorage.getItem('cart');
  if (localSessionCart) {
    displayCartContent(JSON.parse(localSessionCart));
  } else {
    displayCartIsEmpty();
  }
}

let displayCartIsEmpty = () => {
  $("#empty-cart").css("display", "block");
}

let displayCartContent = (cartData) => {
  $(".loader").css("display", "block");
  $.ajax({
    url: 'api/products/products_data',
    method: 'GET',
    data: {
      productIds: JSON.stringify(Object.keys(cartData))
    },
    success: function(response) {
      console.log(response);
      let productsData = (JSON.parse(response.response))
      
      // function func(productsData, cartData){
        for (let i=0;i<productsData.length;i++) {
            let obj=productsData[i]
            let productId=Object.keys(cartData)[i]
            if (obj["id"].toString()===productId){
              obj["qty"]=cartData[productId]["qty"]
            }
            
    // return productsData;
                    
  }
  
      generateProductsTable(productsData);
    },
    error: function(xhr, status, error) {
      console.error(error);
    }
  });
}

let generateProductsTable = (productsData) => {
  let rows = [];
  productsData.forEach(data => {
    rows.push(createRow(data))
  });

  rows.map(row => {
    $('#cart-table tbody').append(row);
  });

  $('.loader').css('display', 'none');
  $('.cart-content').css('display', 'block');
}


let createRow = (productData) => {
  return `<tr>
  <th scope="row" class="border-0">
    <div class="p-2">
      <img src="` + productData.imageUrl + `" alt="" width="70" class="img-fluid rounded shadow-sm">
      <div class="ml-3 d-inline-block align-middle">
        <h5 class="mb-0">` + productData.title + `</h5>
      </div>
    </div>
  </th>
  <td class="border-0 align-middle"><strong>` + productData.price + ` $</strong></td>
  <td class="border-10 align-middle" width="120px">
    <div class="cart-product-quantity" width="130px">
      <div class="input-group quantity">
          <div class="input-group-prepend decrement-btn" style="cursor: pointer">
              <span class="input-group-text">-</span>
          </div>
          <input type="text" class="qty-input form-control" maxlength="2" max="10" value="` + productData.qty  + `">
          <div class="input-group-append increment-btn" style="cursor: pointer">
              <span class="input-group-text">+</span>
          </div>
      </div>
    </div>
  
  </td>
  <td id="remove_from_cart">
      <input type="hidden" value="` + productData.id + `" name="cartitem_product">
      <button type="submit" class="trash-btn border-0 align-middle" id="remove-` + productData.id + `" 
      onclick="remove_item(` + productData.id + `)">
        <a href="" class="text-dark"> 
          <i class="fa fa-trash"></i>
        </a>
      </button>                         
  </td>
  </td>
  </tr>`;
}

let generateSummary = (productsData) => {
  let rows = [];
  productsData.forEach(data => {
    rows.push(createRow(data))
  });

  rows.map(row => {
    $('#cart-table tbody').append(row);
  });

  $('.loader').css('display', 'none');
  $('.cart-content').css('display', 'block');
}

let createField = (productData) => {
  return `<div class="col-lg-6">
  <div class="bg-light rounded-pill px-4 py-3 text-uppercase font-weight-bold">Order summary </div>
  <div class="p-4">
    <p class="font-italic mb-4">Shipping and additional costs are calculated based on values you have entered.</p>
    <ul class="list-unstyled mb-4">
      <li class="d-flex justify-content-between py-3 border-bottom"><strong class="text-muted">Order Subtotal </strong><strong>$390.00</strong></li>
      <li class="d-flex justify-content-between py-3 border-bottom"><strong class="text-muted">Shipping and handling</strong><strong>$10.00</strong></li>
      <li class="d-flex justify-content-between py-3 border-bottom"><strong class="text-muted">Tax</strong><strong>$0.00</strong></li>
      <li class="d-flex justify-content-between py-3 border-bottom"><strong class="text-muted">Total</strong>
        <h5 class="font-weight-bold">$ {{cart_amt}}</h5>
      </li>
    </ul><a href="{%url "checkout" %}" class="btn btn-dark rounded-pill py-2 btn-block">Procceed to checkout</a>
    
  </div>`
}