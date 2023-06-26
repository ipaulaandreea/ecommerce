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

// let cartobject={
  let cartitem=localStorage.getItem('cart')
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
