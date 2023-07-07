$(document).ready(function() {
    orderId=localStorage.getItem("orderId")
    console.log( "ready! orderId: "+orderId );
    $("#orderid").append(orderId)
    localStorage.clear()
  }
  );
