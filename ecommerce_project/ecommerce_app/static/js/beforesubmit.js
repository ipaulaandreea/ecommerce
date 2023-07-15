
$(document).ready(function() {
    console.log( "ready!" );
    beforesubmit();
  });

let beforesubmit = () => {
    let productsData = JSON.parse(localStorage.getItem("cart"));
    let cartResults = generateCartResult(productsData);
    let ordertotal=0;
    let productTotalsList=[]
    let ids=Object.keys(productsData)
    for (let i=0;i<ids.length;i++) {
        let product=productsData[ids[i]]
        producttotal=product["price"]*product["qty"]
        ordertotal+=producttotal
        }
    

    cartResults.map(row => {
        $('#beforesubmit').append(row);
    });

    showtotal(ordertotal);
    
}

  
let generateCartResult= (productsData) => {
    let rows = [];
    let productIds=Object.keys(productsData)
    productIds.forEach(productId => {
        rows.push(createFinalTable(productsData[productId]))
    });
    return rows;
}

let createFinalTable = (productData) => {
    return `<li class="list-group-item d-flex justify-content-between lh-condensed">
        <div>
        <h6 class="my-0">` + productData?.title + ` x ` + productData?.qty + ` </h6>
        </div>
        <span class="text-muted">$ ` + (productData?.price*productData?.qty) + `</span>
        </li>`;
}


let showtotal=(total)=> {
    $('#ordertotal').append(createtotalline(total));
}

createtotalline=(total) => {
    return `<span>Total (USD)</span>
     <strong>$ ` + total + `</strong>`
 }