
$(".loading").hide();
$(".restaurant").hide();


var loc = {
    latitude: 40.388850,
    longitude: -3.628063
};

var venues = null;

function renderVenue() {
    $(".restaurant").show();
    if(venues.length){
        var venue = venues[0];
        $(".restaurant-name").text(venue.name);
        $(".restaurant-address").text(venue.location.address);
        $(".restaurant-distance").text(venue.location.distance);
        $(".quotes").empty();
        venue.tips.forEach(function(tip){
            $("<blockquote/>").append($("<p/>").text(tip.text)).addClass((tip && tip.anal && tip.anal.result && tip.anal.result.sentiment) || "ERR").appendTo(".quotes");
        });
    }
}

$(".btn-otro").click(function(){
    venues.shift();
    renderVenue();
    if(venues.length == 1){
        $(".btn-otro").hide();
    }
    return false;
});

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
            $(".loading").show();
            $(".selCat").hide();
            var params = {
                "loc": [loc.latitude, loc.longitude].join(","),
                "cat": data[2]
            };
            $.get("/recommend", params, function(res){
                res = JSON.parse(res);
                console.log(res);
                venues = res;
                $(".loading").hide();
                renderVenue();
            });
            return false;
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

