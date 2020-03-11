// Formatting for String
if(!String.prototype.format){
    String.prototype.format = function(){
        var args = arguments;
        return this.replace(/{(\d+)}/g, function (match, number) {
            return typeof args[number] != 'undefined' ? args[number]: match
        })
    }
}

$(document).ready(function(){
    // Handles newsletter signup
    $('#js-newsletterbtn').click((event) => {
        event.preventDefault();
        let email_value = $('.js_id_email');
        let newsletter_link = $('#nwsletterlnk').val();
        if(validateEmail(email_value.val())){
            $.ajax({
                url: newsletter_link,
                type: 'POST',
                data:{
                    'email':email_value.val()
                },
                dataType: 'json',
                success: function(data){
                    if(data.is_saved){
                        displayAlert('center', 'success', 'Done', 'Suscription Added');
                        email_value.val('')
                    }else if(data.email_exists){
                        displayAlert('center', 'warning', 'Hey', 'This email is subscribed already');
                    }else{
                        displayAlert('center', 'error', 'Error', 'An unknown error occurred');
                    }
                },
                error: function(error){
                    displayAlert('center', 'error', 'Error', error.status+': '+error.statusText);
                }
            });

        }else{
            displayAlert('center','warning','Oops!', 'Incorrect email format')
        }

    });
});
