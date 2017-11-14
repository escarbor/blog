$(document).ready(function () {
    $("#contact_submit").click(function (event) {
        event.preventDefault();
        $.ajax({
            type: "POST",
            url: "contact_submit/",
            dataType: 'json',
            data: {
                email_body: $('#email_body').val(),
                email_subject: $('#email_subject').val(),
                email_name: $('#email_name').val(),
                email_address: $('#email_address').val(),
                csrfmiddlewaretoken: $("#contact-form").find('input[name=csrfmiddlewaretoken]').val()
            }
        }).done(function (data) {
            console.log(data);
            data.status ? formSuccess() : errorDisplay();

            function formSuccess() {
                $("#alert-danger").css('visibility', 'hidden').hide().fadeOut('fast');
                $("#contact-form").find(':input').css('border-color', '#ccc');
                document.getElementById('contact-form').reset();
                $("#alert").css('visibility', 'visible').hide().fadeIn('fast');
                setTimeout(function () {
                    $("#alert").css('visibility', 'hidden').hide().fadeOut(2000)
                }, 10000);
            }

            function errorDisplay() {
                console.log("in here");
                for (var key in data) {
                    console.log(key);
                    if (data.hasOwnProperty(key)) {
                        var fieldId = "#" + key;
                        $(fieldId).css('border-color', 'red');
                        $("#alert-danger").css('visibility', 'visible').hide().fadeIn('fast');
                    }
                }
            }
        }).fail(function (err) {
            console.log(err);
        });
    });
});