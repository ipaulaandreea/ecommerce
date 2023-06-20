$(document).ready(function () {

// const REMOVE_FROM_CART_BUTTONS = document.getElementById("trash-btn")
// console.log(REMOVE_FROM_CART_BUTTONS)
// function delete_func() { 
//     for (let i=0;i<REMOVE_FROM_CART_BUTTONS.length;i++)
//     button=REMOVE_FROM_CART_BUTTONS[i];
//     buttonClicked=Event.target;
// }
// button.addEventListener('click', delete_func(), buttonClicked.parentElement.remove())






    $(".add-to-cart").click((event) => {
        alert("clicked button");
        event.stopPropagation();
    });

$('.increment-btn').click(function (e) {
    e.preventDefault();
    var incre_value = $(this).parents('.quantity').find('.qty-input').val();
    var value = parseInt(incre_value, 10);
    value = isNaN(value) ? 0 : value;
    if(value<10){
        value++;
        $(this).parents('.quantity').find('.qty-input').val(value);
    }

});

$('.decrement-btn').click(function (e) {
    e.preventDefault();
    var decre_value = $(this).parents('.quantity').find('.qty-input').val();
    var value = parseInt(decre_value, 10);
    value = isNaN(value) ? 0 : value;
    if(value>1){
        value--;
        $(this).parents('.quantity').find('.qty-input').val(value);
    }
});
})