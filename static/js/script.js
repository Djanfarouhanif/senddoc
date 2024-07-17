$(document).ready(function(){
    $('#sendForm').on('submit', function(event){
        event.preventDefault();

        $.ajax({
            type:'POST',
            url: "{% url 'home' %}",
            data: {
                'faculte': $('input[name=faculte]').val(),
                'departement': $('input[name=departement]').val(),
                'csrfmiddlewaretoken': $('input[name=csrfmiddlewaretoken]').val()
            },
            success: function(response){
                $('.content').append()
            }
        })
    })
})