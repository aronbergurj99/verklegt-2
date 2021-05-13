
var products;
let searchResults = document.getElementById("search-result");
let searchInput = document.getElementById("search");
let filteredArr = [];
let searchArr;
let input = document.getElementById("search");

//small cart lenght on navbar
let cartLen = 0;

//index
var newHtml;

//listen to the enter key on search bar
input.addEventListener("keyup", function(event) {
  if (event.key === 'Enter') {
    event.preventDefault();
    let product = filteredArr[0].id;
    document.getElementById('search-product-' + product).click();

  }
});

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
  href.href = '/products/' + product.id;
  href.id = 'search-product-' + product.id;
  href.setAttribute("onclick", "addToSearchHistory(" + product.id + ")");

  var container = document.createElement("div");
  container.className = "single-search-result";

  var c = document.createElement("div")
  c.style="display: flex; flex-directino: row; align-items: center;"

  var name = document.createElement("p");
  name.innerHTML = product.name;

  var productPrice = document.createElement("p");
  productPrice.innerHTML = "Price: " + product.price + " Kr";

  var productImage = document.createElement("img");
  productImage.setAttribute("src", product.image)
  productImage.className = "x-small-images"

  c.appendChild(productImage);
  c.appendChild(name);

  container.appendChild(c);
  container.appendChild(productPrice);
  href.appendChild(container);

  searchResults.appendChild(href);
}

function search() {
  if (!products) {
    //json products for live seearch!!
    getProducts()
  }
  if (searchArr.length === 0) {
    getSearchHistory();
  }
  searchResults.innerHTML = ""
  filteredArr = products.filter(info => info['name'].toLowerCase().includes(searchInput.value.toLowerCase()));

  //only show the top 3 most recent searches
  let searchHistorySize = ((searchArr.length <=3) ? searchArr.length : 3);
  //only show the top 4 most likely search results
  let searchSize = ((filteredArr.length <= 4) ? filteredArr.length : 4);
  for (let i = 0; i < searchSize; i++) {
    createSearchResult(filteredArr[i]);
  }
  let searchHistorySeperator = document.createElement('div');
  searchHistorySeperator.innerHTML= `<p>Most recent searches:</p>`;
  searchHistorySeperator.setAttribute('class', "search-bar-history");
  //search history!
  searchResults.appendChild(searchHistorySeperator)
  for (let i = 0; i < searchHistorySize; i++) {
    createSearchResult(searchArr[i]);
  }
}

function addToSearchHistory(product_id) {
  //TODO: implement add search history with post request
  $(document).ready(function() {
    $.ajax({
      type: "POST",
      url: "/accounts/search-history/" + product_id,
      data: {
        csrfmiddlewaretoken: csrfToken
      },
      success: function(resp) {
        console.log(resp)
      },
      error: function (xhr, status, error) {
        console.log(error);
      }
    })
  });

}

function getSearchHistory() {
  $(document).ready(function() {
    $.ajax({
      type: "GET",
      url: "/accounts/search-history",
      data: {
        csrfmiddlewaretoken: csrfToken
      },
      success: function(resp) {
        searchArr = resp.data;
        console.log(searchArr)
      },
      error: function (xhr, status, error) {
        console.log(error);
      }
    })
  });
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
        createIndexHtml(resp)

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
        createIndexHtml(resp)
        $('.products-index').html(newHtml.join(''));
      },
      error: function(xhr, status, error) {
        console.log(error)
      }
    })
  });


});

function createIndexHtml(resp) {
  newHtml = resp.data.map(d => {
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
})};

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

getSearchHistory()
getProducts()
getCartLen()