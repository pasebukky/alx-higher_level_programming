let url = "https://swapi-api.alx-tools.com/api/films/?format=json";

$.get(url, function(data) {
    let films = data.results;
    for (let film in films) {
        $("#list_movies").append("<li>" + films[film].title + "</li>");
    }
});
