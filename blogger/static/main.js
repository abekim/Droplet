$(function () {
    $('#new_task').keypress(function (e) {
        if (e.which == 13) {
            console.log('enter key registered');
            descr = $(this).val();
            $(this).val('');
            $.post('/new', { description: descr }).done(function (resp) {
                $('#tasks tbody').append('<tr><td><input class="toggle" type="checkbox"></td><td>' + resp.data.description + '</td></tr>');
            });
        };
    });
});