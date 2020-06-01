document.addEventListener('DOMContentLoaded', function() {

    var size = '';

    

    //console.log(Subs);
    //console.log(Dinner_Platters);
    //console.log(Subs[0]["name"]);
    //console.log(`Name = ${Subs[0]["name"]}`)

    //Showing subs in menu
    showitem("Subs",Subs);
    showitem("Dinner_Platters",Dinner_Platters);
    showitem("Pasta",Pasta);
    showitem("Salads",Salads);




    var typeofItem = 'Regular_Pizza';
    // toppingSelction(pizzatype,pizzaJson);
    toppingSelction('Regular_Pizza',Regular_Pizza);
    toppingSelction('Sicilian_Pizza',Sicilian_Pizza);


});

function getId(itemname,items,size){
  // input -> Name of the item like meatball
            //  -> Size of the item like small or large
            //  -> and the JSON object of items
  // output -> Id of the item
  //console.log("Inside getID");
  //console.log(items);

  if (!(size == "NOSIZE")){
    console.log("Inside if 1");
    for (var i in items){
        console.log("inside for loop");
        console.log(`name  = ${items[i]["name"]} and type = ${items[i]["type"]}`)
        if(items[i]["name"] == itemname && items[i]["type"]==size){
          console.log(items[i]["id"]);
          return items[i]["id"];
        }

    }
  }

}

function test(add){
  console.log("function test");
  console.log(add);
}
function showitem(itemname,items){
    itemNames = getUniqueName(items);
    //console.log(itemNames);
    // Adding all the subs in a menu

    extra_cheese = document.querySelector('#extra_cheese');
    extra_cheese.onclick = () => {
      document.querySelectorAll('.subsize').forEach(radio => {
        radio.checked = false;
      });

      document.querySelectorAll('[data-disable]').forEach(button => {
          button.disabled = true;
      });

      };

    var td_type = null;
      for(var i in itemNames){
      //create a divison that will display two option  for pizza size small and large
      const div = document.createElement('div');
      div.setAttribute("class","radio");
      // creating componets that will be added to the divison like radio buttons
    //  console.log(itemNames);
      var add = document.createElement('button');
      add.setAttribute('data-name',itemname+itemNames[i]);
      if(itemname == "Subs"){
        add.setAttribute('data-disable','subdis');
      }
      console.log(itemNames[i]);
      add.setAttribute("class","addbuttonstyle subadd btn btn-primary");
      if (itemname == "Pasta" || itemname == "Salads"){
          //Find the id of the item and call add into shopping cart
          for(var eachitem in items){
          // id of the sub
          if (items[eachitem]["name"] == itemNames[i] ){
            add.setAttribute("onclick",`addintoshoppingcart('${items[eachitem]["id"]}','${itemname}')`);
        }
      }
    }
    if(itemname == "Subs" || itemname == "Dinner_Platters"){
          add.disabled = true;




      }

    add.innerHTML = "Add";
    if(itemname == "Subs" || itemname == "Dinner_Platters"){
        var type = 'notselected';
        labelPrice = document.createElement('label');
        labelPrice.setAttribute("class","labelPrice");
        labelPrice.setAttribute('data-name','label'+itemNames[i]);
        labelPrice.innerHTML = '$0';
        div.append(labelPrice);

        var td_type = document.createElement('td');
      }

        if(td_type != null)
          td_type.innerHTML =  div.innerHTML;
      // create the add button

      if(td_type == null){
        // It is the object of pasta, therefore calculate price
        var td_price = document.createElement('td');

        console.log("name of the item is = " + itemNames[i]);
        td_price.innerHTML = calPrice(JSON.stringify(items),itemNames[i],'NOSIZE',itemname);
      }

      // Create the table row for each subs
      const tr = document.createElement('tr');

      // create the coloumn for a row
      const td_name = document.createElement('td');
      const td_add = add;
      td_name.innerHTML = itemNames[i];


      // adding coloumn into a row
      tr.append(td_name);
      if(itemname == "Subs" || itemname == "Dinner_Platters"){
        tr.append(td_type);
      //  tr.append(td_price);
      }
      else{
          tr.append(td_price);
      }
      tr.append(td_add);
      //adding row into a table
      if(itemname == "Subs")
          document.querySelector('#subtable').append(tr);
      if(itemname == "Dinner_Platters")
        document.querySelector('#dinner_platter_table').append(tr);
      //document.querySelector('.Menu_Main_Div').removeChild(document.querySelector('.radio'))
      if(itemname == "Pasta")
        document.querySelector('#Pasta_table').append(tr);
      if(itemname == "Salads")
        document.querySelector('#Salad_table').append(tr);
    }

    if(itemname == "Subs"){
      subitemNames = getUniqueName(Subs);
      document.querySelectorAll('.subsize').forEach(radio => {
        radio.onclick = () => {
          if(radio.value=='Small'){
            type = 'S';
            console.log("Small");
            // call calculate price for evry item name with size = small
            for(var i in subitemNames){
                console.log("Item name= "+ subitemNames[i]);
                calPrice(JSON.stringify(items),subitemNames[i],'S',itemname);
              }
            }

            if(radio.value=='Large'){
              type = 'L';
              console.log("Large");
              for(var i in subitemNames){
                  console.log("Item name= "+ subitemNames[i]);
                  calPrice(JSON.stringify(items),subitemNames[i],'L',itemname);
                }
            }
          };
        });
    }

    if(itemname == "Dinner_Platters"){
      Dinner_Platters_itemNames = getUniqueName(Dinner_Platters);
      document.querySelectorAll('.dinner_platter_size').forEach(radio => {
        radio.onclick = () => {
          if(radio.value=='Small'){
            type = 'S';
            console.log("Small");
            // call calculate price for evry item name with size = small
            for(var i in Dinner_Platters_itemNames){
                console.log("Item name= "+ Dinner_Platters_itemNames[i]);
                calPrice(JSON.stringify(items),Dinner_Platters_itemNames[i],'S',itemname);
              }
            }

            if(radio.value=='Large'){
              type = 'L';
              console.log("Large");
              for(var i in Dinner_Platters_itemNames){
                  console.log("Item name= "+ Dinner_Platters_itemNames[i]);
                  calPrice(JSON.stringify(items),Dinner_Platters_itemNames[i],'L',itemname);
                }
            }
          };
        });
    }


}

function calPrice(items , name , value,itemname){
//  console.log("Function called");
  console.log("Name = "+ name);
  console.log("Value = "+value);
  items = JSON.parse(items);
  console.log('items = '+ items);
  console.log(itemname);

  price = 0;
  if (itemname == "Subs" || itemname == "Dinner_Platters"){
    // call here
  //  enableAdd(add);
    for(var eachSub in items){
      // price of the sub
      if (items[eachSub]["name"] == name && value == items[eachSub]["type"] ){
      //  console.log(name);
    //    console.log(value);
      //  console.log(items[eachSub]["id"]);
          price = items[eachSub]["price"];
          console.log("price found = "+price);
          extra_cheese = document.querySelector('#extra_cheese');
          if (extra_cheese.checked){
            price =  parseFloat(price) + 0.50;
          }
      // adding price along with button
      subAdd = document.querySelector(`[data-name="${itemname + name}"]`);
      labelPrice = document.querySelector(`[data-name="label${name}"]`);
      labelPrice.innerHTML = '$' + price;
      subAdd.disabled = false;

      // adding on click function in the button with all the parameters needed.
      subAdd.setAttribute("onclick",`addintoshoppingcart('${items[eachSub]["id"]}','${itemname}')`);

    }
  }
}
    else if (itemname == "Pasta" || itemname == "Salads"){
      for(var eachSub in items){
        if(items[eachSub]["name"] == name){
          //  console.log(name);
            //console.log(document.querySelector(`[data-name="${name}"]`));
          //addItem = document.querySelector(`[data-name="${itemname + name}"]`);
          //addItem.setAttribute("onclick",`addintoshoppingcart('${items[eachSub]["id"]}','${itemname}')`);
            return items[eachSub]["price"];
          }
        }
      }
  // setting all other button equal to add
  document.querySelectorAll('.subadd').forEach(function(button){
  if(button.getAttribute('data-name') != name)
  {
    //button.innerHTML = "Add";
    //labelPrice = document.querySelector(`[data-name="label${name}"]`);
    //labelPrice.innerHTML = '$0';
  }
});
}

function getUniqueName(item){
  var itemNames = [];
  for(var i in item){
    if(!itemNames.includes(item[i]["name"]))
    itemNames.push(item[i]["name"]);
  }
  return itemNames;
}
function calculatePizzaPrice(pizzatype, pizzasJson, numToppings,type){
//  console.log("pizza type = "+pizzatype);
//  console.log("pizza json = " + JSON.stringify(pizzasJson));
//  console.log("Inside calculatePizzaPrice num of toppings = "+ numToppings);
//  console.log("Inside calculatePizzaPrice type = "+ type);
  for(var i in pizzasJson){
      console.log("num of toppings = "+ numToppings );
      if (pizzasJson[i]["numToppings"] == numToppings && type == pizzasJson[i]["type"] ){
        //console.log(Regular_Pizza[i]["price"]);
        //console.log(Regular_Pizza[i]["id"]);
        price = pizzasJson[i]["price"];
      //  console.log("Price found = "+ price);
        id = pizzasJson[i]["id"];
        if(pizzatype == "Regular_Pizza"){
          document.querySelector('#Regular_Pizza_price').innerHTML = price;
          return id;
        }

        if(pizzatype == "Sicilian_Pizza") {
          document.querySelector('#Sicilian_Pizza_price').innerHTML = price;
          return id;
        }

        }
      }
}
var id = 0;
function  toppingSelction(typeofItem,pizzaJson){
  var numToppings = 0;
  var price = 0;
  var type = 'notselected';
  if(typeofItem == "Regular_Pizza"){
    var pizzaSizeRadio = 'Regular_Pizza_Size';
    var toppingCheckboxClassName = 'Regular_Pizza_Toppings';
  }
  else if(typeofItem == "Sicilian_Pizza"){
    var pizzaSizeRadio = 'Sicilian_Pizza_Size';
    var toppingCheckboxClassName = 'Sicilian_Pizza_Toppings';
  }

  // user can not select the toppings until size is selected
    document.querySelectorAll(`.${pizzaSizeRadio}`).forEach(radio => {
      radio.onclick = () => {

        numToppings = 0;
        if(typeofItem == "Regular_Pizza"){
          document.querySelector('#Regular_Pizza_price').innerHTML = price;

        }

        if(typeofItem == "Sicilian_Pizza") {
          document.querySelector('#Sicilian_Pizza_price').innerHTML = price;

        }
          //if radio is selected enable toppings checkbox
          // if radio is unselected disable toppings checkbox

          //uncheck all toppings toppingsChecsskbox
          document.querySelectorAll(`.${toppingCheckboxClassName}`).forEach(checkbox => {
              checkbox.checked = false;
          });
          if(radio.value=='Small')
            type = 'S';
          if(radio.value=='Large')
            type = 'L';
        };
      });
  document.querySelectorAll(`.${toppingCheckboxClassName}`).forEach(checkbox => {
    checkbox.onclick = () => {
      if(type == "notselected"){
        alert("please select the size");
        checkbox.checked = false;
      }
      else{
        if(checkbox.checked==true && checkbox.value == "Cheese"){
          numToppings = 0;
          // disable and uncheck all other toppings checkboxes except No extra toppings
          document.querySelectorAll(`.${toppingCheckboxClassName}`).forEach(i => {
                if(i.value!="Cheese"){
                  i.disabled = true;
                  i.checked = false;
                }
          });
        }
        if(checkbox.checked==false && checkbox.value == "Cheese"){
          document.querySelectorAll(`.${toppingCheckboxClassName}`).forEach(i => {
            // enable all the toppings checkboxes
              i.disabled = false;
          });
         }

        if(checkbox.checked && checkbox.value == "Special"){
          numToppings = 5;
          // disable all other toppings checkboxes except Special
          document.querySelectorAll(`.${toppingCheckboxClassName}`).forEach(i => {
              if(i.value!='Special'){
                i.disabled = true;
                i.checked = false;
              }
            });
        }
        if(checkbox.checked==false && checkbox.value == "Special"){
          // enable all the toppings checkboxes
          document.querySelectorAll(`.${toppingCheckboxClassName}`).forEach(i => {
              i.disabled = false;
          });
        }
        if(checkbox.checked == false && checkbox.value != "Special" && checkbox.value != "Cheese")
            numToppings = numToppings - 1;
        else if(checkbox.checked == true && checkbox.value != "Special" && checkbox.value != "Cheese") {
          numToppings = numToppings + 1;
        }

        //console.log(Regular_Pizza);
        //console.log(numToppings);
        //console.log(type);

        // calculate price from a dictonary here
        var id = calculatePizzaPrice(typeofItem, pizzaJson, numToppings,type);
        if(numToppings == 3){
          document.querySelectorAll(`.${toppingCheckboxClassName}`).forEach(i => {
            if(i.checked == false)
                i.disabled = true;
          });
            console.log("num of toppings = "+ numToppings );
        }
        else if (numToppings!=3 && checkbox.value!="Cheese" && checkbox.value!="Special") {
          document.querySelectorAll(`.${toppingCheckboxClassName}`).forEach(i => {
                i.disabled = false;
          });
        }
          document.querySelectorAll('.addintoshoppingcart').forEach(button => {
              button.onclick = () => {
              console.log("button clicked");
              console.log("id before adding pizza into shopping cart"+id);
              addintoshoppingcart(id,typeofItem);
              numToppings = 0;
            };
          });
      }
    };



  });
}

var shoppingCartItemCount = 0;
// addintoshoppingcart(id, typeofItem)
function addintoshoppingcart(id,typeofItem){
var Toppingclass;
  if(typeofItem == "Regular_Pizza")
    Toppingclass = 'Regular_Pizza_Toppings';

  else if (typeofItem == "Sicilian_Pizza")
    Toppingclass = 'Sicilian_Pizza_Toppings';

  console.log("Addded into shopping cart");
  console.log("id = "+id);
  console.log("Item ="+typeofItem);

  shoppingCartItemCount = shoppingCartItemCount + 1;
  // addIntoShoppingCart()
  console.log(shoppingCartItemCount);
          // ajax request to call addintoshoppingcart
          const request = new XMLHttpRequest();

        //  get toppings only in case of pizza otherwise set topping = noToppingItem
              var toppings  = [];

                var checkboxes =  document.querySelectorAll(`input[class=${Toppingclass}]:checked`);
                if(typeofItem == "Sicilian_Pizza" || typeofItem == "Regular_Pizza"){
                var i;
                for(i=0;i<checkboxes.length;i++){
                  toppings.push(checkboxes[i].value)
                }
              }
              else {
                toppings.push("noToppingItem");
              }


          extra_cheese = document.querySelector('#extra_cheese');
          if(extra_cheese.checked && typeofItem == "Subs"){
            toppings.push('extra_cheese_sub');
          }
           //console.log(toppings);
           request.open('GET', `/addintoshoppingcart/${id}/${typeofItem}/${toppings}`);
        // Callback function for when request completes
          request.onload = () => {
          // Extract JSON data from request
          const data = request.responseText;
          console.log(data)
          // Update the cart number
          document.querySelector('#numofitems').innerHTML = data;
          document.querySelector('#numofitems').style.color = '#ffffff';
          // 2.  set number of topping to "0" in case of pizzas
          numToppings = 0;
          // 3. uncheck and enable all topping checkbox in case of pizzas
          if(typeofItem == "Sicilian_Pizza" || typeofItem == "Regular_Pizza"){
            document.querySelectorAll(`.${Toppingclass}`).forEach(checkbox => {
              checkbox.checked = false;
              checkbox.disabled = false;
            });
          }

          // set price to "0"
          if (typeofItem == "Regular_Pizza")
            document.querySelector('#Regular_Pizza_price').innerHTML = 0;
          if (typeofItem == "Sicilian_Pizza")
            document.querySelector('#Sicilian_Pizza_price').innerHTML = 0;
        }
          request.send();
}
