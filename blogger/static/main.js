$(function () {
    $(".button#create").click(function() {
        // Submit post to DB
        $.post("/blog/new", {
            subject : "First post",
            body : "Droplet. Lorem ipsum",
            author : 'abekim'
        })
        .done(function(data) {
        })
        .fail(function(data) {
        })
        .always(function(data) {
            console.log(data);
        });
    });
});