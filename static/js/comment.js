$(document).ready(function () {
    $("#comment_submit").click(function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: "comment_submit/",
            dataType: 'json',
            data: {
                name: $('#name').val(),
                email: $('#email').val(),
                comment: $('#comment').val(),
                email_address: $('#email_address').val(),
                csrfmiddlewaretoken: $("#comment-form").find('input[name=csrfmiddlewaretoken]').val()
            }
        }).done(function (data) {
            data.status ? formSuccess() : errorDisplay();
            document.getElementById('comment-form').reset();

            function formSuccess() {
                $(".comment-container").empty();
                $.each($.parseJSON(data.comments), function (index, comment) {
                    $(".comment-container").append("<div class='comment'>\n" +
                        "<div class='comment-title'><span>" + comment.fields.name + "</span></div>\n" +
                        "<div class='comment-date'><span>" + comment.fields.pub_date + "</span></div>\n" +
                        "<div class='comment-body'><span>" + comment.fields.comment + "</span></div>\n" +
                        "</div>");
                    $('body, html').animate({scrollTop: 0}, 'slow');
                    $('body, html').stop();
                });
            }

            function errorDisplay() {
                console.log("error in comment form");
            }
        }).fail(function (err) {
            console.log(err);
        });
    });
});

/// comment collapse
$('.glyphicon-chevron-up').hide();

$('#comments-collapse').on('shown.bs.collapse', function () {
    $('.glyphicon-chevron-down').hide();
    $('.glyphicon-chevron-up').show();
});

$('#comments-collapse').on('hidden.bs.collapse', function () {
    $('.glyphicon-chevron-down').show();
    $('.glyphicon-chevron-up').hide();
});