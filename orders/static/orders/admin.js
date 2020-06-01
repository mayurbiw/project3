document.addEventListener('DOMContentLoaded', () => {

document.querySelectorAll('.completeOrder').forEach(button => {
  button.onclick = () => {
    const request = new XMLHttpRequest();
    orderId = button.getAttribute('data-orderid');

    request.open('GET', `/markcompleted/${orderId}`);


    request.onload = () => {
    // Extract JSON data from request
    const data = JSON.parse(request.responseText);
    if(data["success"]){
      location.reload();
    }
    else{
      alert("something went wrong");
    }


  };

  request.send();

  }


});
});
