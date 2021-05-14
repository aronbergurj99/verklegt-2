
var products;
let searchResults = document.getElementById("search-result");
let searchInput = document.getElementById("search");
let filteredArr = []

//small cart lenght on navbar
let cartLen = 0;


//function to retrieve all products when searching
function getProducts() {

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      products = JSON.parse(this.response).data
      search()
    }
  };
  xhttp.open("GET", '/search', true);
  xhttp.send();
}



function createSearchResult(product) {
  var href = document.createElement("a");
  href.href = '/products/' + product.id

  var container = document.createElement("div");
  container.className = "single-search-result";

  var name = document.createElement("p");
  name.innerHTML = product.name;

  var productPrice = document.createElement("p");
  productPrice.innerHTML = "Price: " + product.price;

  var productImage = document.createElement("img");
  productImage.setAttribute("src", product.image)
  productImage.className = "x-small-images"
  container.appendChild(name);
  container.appendChild(productPrice);
  container.appendChild(productImage);
  href.appendChild(container);

  searchResults.appendChild(href);
}

function search() {
  if (!products) {
    getProducts()
  }
  searchResults.innerHTML = ""
  filteredArr = products.filter(info => info['name'].toLowerCase().includes(searchInput.value.toLowerCase()));

  for (let i = 0; i < filteredArr.length; i++) {
    createSearchResult(filteredArr[i]);
  }
}

function updateCartNavIcon() {

}
function getCartLen() {

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      cartLen = JSON.parse(this.response)['cart-items'];
      changeCartIconLen()
    }
  };
  xhttp.open("GET", '/cart/get-cart-len', true);
  xhttp.send();
}

function changeCartIconLen() {
  let lenValue = document.getElementById('cart-len-display');
  console.log(lenValue.innerText)
  if (Number(lenValue.innerText) !== cartLen) {
    lenValue.innerText = cartLen;
  }
};

var order = 'name';
var type = '';

$(document).ready(function() {

  $('#filter').on('change', function (e){
    e.preventDefault();
    type = $('#filter').val();
    order = $('#order').val();
    $.ajax( {
      url: '/?type_filter=' + type + '&order=' + order,
      success: function(resp) {
        var newHtml = resp.data.map(d => {
          return `
<div class="small-product">
    <a href="/products/${d.id}">
        <img class="small-image" src="${d.image}"/>
    </a>
    <div class="small-product-text">
        <h1>${d.name}</h1>
        <p><b>Price: ${d.price}</b></p>
    </div>

    <button type="submit" class="btn btn-primary btn-sm add-to-cart-btn" onclick="addToCart(${d.id}, true, false)">add to cart<i class="fas fa-cart-plus"></i></button>

</div>
`

        });
        $('.products-index').html(newHtml.join(''));
      },
      error: function(xhr, status, error) {
        console.log(error)
      }
    })
  });

    $('#order').on('change', function (e){
    e.preventDefault();
    type = $('#filter').val();
    order = $('#order').val();
    $.ajax( {
      url: '/?type_filter=' + type + '&order=' + order,
      success: function(resp) {
        var newHtml = resp.data.map(d => {
          return `
<div class="small-product">
    <a href="/products/${d.id}">
        <img class="small-image" src="${d.image}"/>
    </a>
    <div class="small-product-text">
        <h1>${d.name}</h1>
        <p><b>Price: ${d.price}</b></p>
    </div>
    <button type="submit" class="btn btn-primary btn-sm add-to-cart-btn" onclick="addToCart(${d.id}, true, false)">add to cart<i class="fas fa-cart-plus"></i></button>
   
</div>
`

        });
        $('.products-index').html(newHtml.join(''));
      },
      error: function(xhr, status, error) {
        console.log(error)
      }
    })
  });


});

function addToCart(id, add, incart) {
  var url;
  var increase;
  if (add == true) {
    url = "/cart/add-to-cart/" + id
    increase = 1;
  } else {
    url = "/cart/remove-from-cart/" + id
    increase = -1;
  }

  $(document).ready(function () {
    $.ajax( {
      type: "POST",
      url: url,
      data: {
        csrfmiddlewaretoken: csrfToken
      },
      success: function(resp) {
        cartLen = resp.data['len']
        changeCartIconLen()
        if (incart) {
          // if the add to cart button is the in cart html then we need to update a few things.
          let cartInput = document.getElementById("cart-input-" + id);
          let cartItem = document.getElementById("cart-item-" + id);
          let totalPrice = document.getElementById("total-price");
          totalPrice.innerText = resp.data['total-price']
          console.log()
          cartInput.value = Number(cartInput.value) + increase;

          if (cartInput.value ==0) {
            cartItem.remove();
          }
        }
      },
      error: function (xhr, status, error) {
        console.log(error)
      }
    });
  });
};

getCartLen()

function getHamburger() {
  var x = document.getElementById("myLinks");
  if (x.style.display === "block") {
    x.style.display = "none";
  } else {
    x.style.display = "block";
  }
}