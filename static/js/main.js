
var loc = {
    latitude: 40.388850,
    longitude: -3.628063
};

var $rest = $(".restaurants");

[
    ["italian", "Italiano", "4bf58dd8d48988d110941735"],
    ["tapas", "Tapas", "4bf58dd8d48988d1db931735"],
    ["chinese", "Chino", "4bf58dd8d48988d145941735"],
    ["mexican", "Mexicano", "4bf58dd8d48988d1c1941735"],
    ["burger", "Hamburguesa", "4bf58dd8d48988d16c941735"]
].forEach(function(data){
    $('<p><a class="btn btn-primary btn-lg resttype"><img src="https://ss1.4sqi.net/img/categories_v2/food/' + data[0] + '_64.png"/>' + data[1] + '</a></p>')
        .click(function(){
            alert("pues te jodes");
        })
        .appendTo($rest);
});

function getLocation() {
    navigator.geolocation.getCurrentPosition(function success(res){
        loc = res.coords;
    }, function error(res){
        alert("error");
        console.log(res);
    });
}
getLocation();

