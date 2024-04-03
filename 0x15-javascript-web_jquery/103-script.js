$(document).ready(function() {
    $('#btn_translate').click(fetchTranslation);
    $('#language_code').keypress(function(event) {
        if (event.keyCode === 13) {
            fetchTranslation();
        }
    });

    function fetchTranslation() {
        var languageCode = $('#language_code').val();
        $.ajax({
            url: `https://hellosalut.stefanbohacek.dev/?lang=${languageCode}`,
            method: 'GET',
            dataType: 'json',
            success: function(response) {
                var translation = response.hello;
                $('#hello').text(translation);
            },
            error: function(xhr, status, error) {
                $('#hello').text('Translation not found');
            }
        });
    }
});
