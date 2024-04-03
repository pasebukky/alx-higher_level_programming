$(document).ready(function() {
    $('#btn_translate').click(function() {
        var languageCode = $('#language_code').val();
        $.ajax({
            url: 'https://hellosalut.stefanbohacek.dev/?lang=${lang}',
            method: 'GET',
            data: { lang: languageCode },
            dataType: 'json',
            success: function(response) {
                var translation = response.hello;
                console.log("Translation:", translation);
                $('#hello').text(translation);
            }
        });
    });
});

