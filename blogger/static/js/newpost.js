/*
 * Javascript for new post creation page
 */
$(function () {
    $(".button#create").click(function() {
        // Submit post to DB
        $.post("/blog/new", {
            subject : "First post",
            body : "Droplet. Lorem ipsum",
            author : 'abekim'
        })
        .done(function(data) {
            window.location.href = "/?" + encodeURIComponent("new_post_success") + "=" + encodeURIComponent("1");
        })
        .fail(function(data) {
        })
        .always(function(data) {
            console.log(data);
        });
    });
});