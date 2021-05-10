
var products;
var images;
var searchResults = document.getElementById("search-result");
var searchInput = document.getElementById("search");
let filteredArr = []
//function to retrieve all products when searching

function getProducts() {

  var xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      var data = JSON.parse(this.response)
      products = data['products']
      images = data['images']
      search()
    }
  };
  xhttp.open("GET", '/search', true);
  xhttp.send();
}



function createSearchResult(product, image) {
  var href = document.createElement("a");
  href.href = product.id

  var container = document.createElement("div");
  container.className = "single-search-result";

  var name = document.createElement("b");
  name.innerHTML = product.name;

  var productPrice = document.createElement("b");
  productPrice.innerHTML = "Price: " + product.price;

  var productImage = document.createElement("img");
  productImage.setAttribute("src", "/media/" + image.image.toString())
  productImage.className = "x-small-images"
  container.appendChild(name);
  container.appendChild(productPrice);
  container.appendChild(productImage);
  href.appendChild(container);

  searchResults.appendChild(href);
}

function search() {
  searchResults.innerHTML = ""

  filteredArr = products.filter(info => info['name'].toLowerCase().includes(searchInput.value.toLowerCase()));
  console.log(products);
  console.log(images)
  for (var i = 0; i < filteredArr.length; i++) {
    for (var j=0; j < images.length; j++) {
      if (images[j].product == filteredArr[i].id) {
        createSearchResult(filteredArr[i], images[j]);
      }
    }

  }
}



