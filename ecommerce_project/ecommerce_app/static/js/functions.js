let orderTotal=0;
let products={"data":{},"total":0};
let productsData={};



function getSessionID() {
  return $.ajax({
    url: '/access_session/',
    method: 'GET',
    dataType: 'json'
  });

  getSessionID().done(function(response) {
    let session_id = response.session_id;
    console.log("Session ID:", session_id);

  }).fail(function() {
    console.log("Failed to retrieve session ID.");
  });
  return session_id;
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + '=') {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}
const csrfToken = getCookie('csrftoken');



$(document).ready(function() {
  console.log( "ready!" );
  displayCart();
});


let displayCart = () => {
  $(".loader").css("display", "block");
  let localSessionCart = localStorage.getItem('cart');
  if (localSessionCart!="{}") {
    displayCartContent(JSON.parse(localSessionCart));
  } else if (localSessionCart="{}") {
    displayCartIsEmpty();
  
  }
}

let hideCart=()=> {
  $("#delivery").css("display","none");
  $(".cartheader").css("display","none");
  $("#cart-table").css("display","none");


}

let displayCartIsEmpty = () => {
  $(".loader").css("display", "none");
  $("#delivery").css("display","none");
  $("#empty-cart").css("display", "block");

}

let displayCartContent = (cartData) => {
  $(".loader").css("display", "block");
  $.ajax({
    url: 'api/products/products_data',
    method: 'GET',
    data: {
      productIds: JSON.stringify(Object.keys(cartData)),
      csrfmiddlewaretoken: csrfToken
    },
    success: function(response) {
      console.log(response);
      let productsData = (JSON.parse(response.response))
      console.log(productsData)
      let productTotalsList=[]
      products["data"]=productsData;
      for (let i=0;i<productsData.length;i++) {
          let obj=productsData[i]
          
          let productId=Object.keys(cartData)[i]
          if (obj["id"].toString()===productId){
            obj["qty"]=cartData[productId]["qty"]
            let productTotal=obj["qty"]*obj["price"]
            obj["total"]=productTotal;
            productTotalsList.push(productTotal);
            orderTotal+=productTotal;
            products["total"]=orderTotal;
          } 
          cartData[productId].title = obj.title
          cartData[productId].price=obj.price
          localStorage.setItem("cart", JSON.stringify(cartData));

      } 
      generateProductsTable(productsData);
      generateSummary(orderTotal);
      // numberrows(productsData);
      // generateCartResult(productsData);
      
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
  $("#cart-icon").text(rows.length);
 

  } 

// // let cartIcon = () => {
//     let localSessionCart = localStorage.getItem('cart');
//     let numberitems=Object.keys(localSessionCart);
// //   $('#cart-icon').val(numberitems.length);
// // }


let createRow = (productData) => {
  return `<tr id="product-row-` + productData.id + `">
  <th scope="row" class="border-2">
    <div class="p-2">
      <img src="` + productData.imageUrl + `" alt="" width="70" class="img-fluid rounded shadow-sm">
      <div class="ml-3 d-inline-block align-middle">
        <h5 class="mb-0">` + productData.title + `</h5>
      </div>
    </div>
  </th>
  <td class="border-2 align-middle subtotals"><strong>` + productData.price + ` $</strong></td>
  <td class="border-2 align-middle" width="120px">
    <div class="cart-product-quantity" width="130px">
      <div class="input-group quantity">
          <div button class="decrement-btn input-group-prepend" style="cursor: pointer" onclick="decrementQuantity(` + productData.id + `)">
              <span class="input-group-text">-</span>
          </div>
          <input id="qty-` + productData.id + `" type="text" class="qty-input form-control qty" maxlength="2" max="10" value="` + productData.qty  + `">
          <div button id="incr" class="increment-btn input-group-append" style="cursor: pointer" onclick="incrementQuantity(` + productData.id + `)">
              <span class="input-group-text">+</span>
          </div>
      </div>
    </div>
  
  </td>
  <td class="border-2 align-middle" id="remove_from_cart">
      <button class="trash-btn border-0 align-middle" id="remove-` + productData.id + `" 
      onclick="deleteCartItem(` + productData.id + `)">
          <i class="fa fa-trash"></i>
      </button>                         
  </td>
  </td>
  </tr>`;
}

let generateSummary = (orderTotal) => {
  $('#list').append(createLi(orderTotal));
  $('.cart-summary').css('display', 'block');
};

let createLi = (orderTotal) => {
  return `<li class="d-flex justify-content-between py-3" id="total-price">
  <strong class="text-muted">Order Subtotal </strong><strong>$ ` + orderTotal + `.00</strong></li>`  
}          

let updateCartTotal = (orderTotal) => {
  $('#total-price').remove();
  $('#list').append(createLi(orderTotal));
  $('.cart-summary').css('display', 'block');
};

// let numberrows = (productsData) => {
//   let localSessionCart = localStorage.getItem('cart');
//   $("#cart-icon").text((Object.keys(localSessionCart).length));
 
// }



function findObjectByValue(data, key, value) {
  for (let i = 0; i < data.length; i++) {
    if (data[i][key] === value) {
      return data[i];
    }
  }
}

let deleteCartItem = (id) => {
  let localSessionCart = localStorage.getItem("cart");
  let cart = JSON.parse(localSessionCart);
  let cartid = id.toString();
  let data=products["data"];
  let product = findObjectByValue(data, "id", id);
  let deletedProductTotal = product["qty"] * product["price"];
  delete cart[cartid];
  localStorage.setItem("cart", JSON.stringify(cart));
  let numberofitems=((Object.keys(cart)).length);
  $('#product-row-' + id).remove();
  $("#cart-icon").text(numberofitems);
  // $('#cart-icon').append(numberofitems);
  orderTotal -= deletedProductTotal;
  updateCartTotal(orderTotal);
  console.log(JSON.stringify(cart));
  if (JSON.stringify(cart) =='{}'){
    displayCartIsEmpty();
    hideCart();
  }
  }

let incrementQuantity=(id)=>{
  let localSessionCart = localStorage.getItem("cart");
  let cart = JSON.parse(localSessionCart);
  let cartid = id.toString();
  let data=products["data"];
  let product = findObjectByValue(data, "id", id);
  product["qty"]+=1;
  orderTotal+=parseInt(product["price"], 10);
  updateCartTotal(orderTotal);
  cart[cartid]["qty"]+=1;
  console.log(cart[cartid]);
  localStorage.setItem("cart", JSON.stringify(cart));
  let updatedQty=product["qty"]
  updateQty(id,updatedQty);
}


let decrementQuantity=(id)=>{
  let localSessionCart = localStorage.getItem("cart");
  let cart = JSON.parse(localSessionCart);
  let cartid = id.toString();
  let data=products["data"];
  let product = findObjectByValue(data, "id", id);
  if (product["qty"]>0){
    product["qty"]-=1;
    orderTotal-=parseInt(product["price"], 10);
    updateCartTotal(orderTotal);
  } else {
    deleteCartItem(id);
  }
  localStorage.setItem("cart", JSON.stringify(cart));
  let updatedQty=product["qty"]
  updateQty(id,updatedQty);
}


let updateQty=(prod,qty)=>{
  $('#qty-' + prod).val(qty);
}


let submitOrder = async (cart) =>{
  cart=localStorage.getItem("cart")
  console.log(cart)
  // $(".loader").css("display", "block");
  let input=JSON.parse(cart)
  // cart={"1":{"qty":5},"2":{"qty":4}}

  // const result = {
  //   "products": [{
  //     "product_id": "",
  //     "qty":""
  // },]
  // };
  
  
  let bigList=[];
  let finallist={};
  let productIds=Object.keys(input);
  productIds.forEach(productId => {
    bigList.push({"product_id": productId, "qty": input[productId]["qty"]})
  });
      console.log("li: "+JSON.stringify(bigList));
      finallist={"products":bigList};
      console.log("finalist: " + JSON.stringify(finallist))    
    

  let session_id=await getSessionID();
  
  $.ajax({
    url: 'api/orders/create',
    method: 'POST',
    data: {
      orderitems: JSON.stringify(finallist),
      sessionID: JSON.stringify(session_id['session_id']),
      csrfmiddlewaretoken: csrfToken
    },
    
    success: function(response) {
      console.log(response.response);
      let order = (JSON.parse(response.orderId))
      localStorage.setItem("orderId", response.orderId)
      
      window.location.href = 'cart/ordersubmitted';
      
        
      // let createstr = (e) => {
      //   return `<div class="container text-white py-2 text-center">
      //   <h1 id="submitted" class="display-4">"Your order(#` + e + ` ) has been submitted!" </h1>
      // </div>` 
      // }
      // $('#output').append(createstr(response.orderId));
      // window.location.href = 'cart/ordersubmitted';
      // console.log("Page loaded");
  
    }
  })
}


