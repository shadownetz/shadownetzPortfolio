$(function(){
    // Handles newsletter signup
    $('#js-newsletterbtn').click((event) => {
        event.preventDefault();
        let email_value = $('#id_email');
        let newsletter_link = $('#nwsletterlnk').val();
        if(is_email(email_value.val())){
            $.ajax({
                url: newsletter_link,
                type: 'POST',
                data:{
                    'email':email_value.val()
                },
                dataType: 'json',
                success: function(data){
                    if(data.is_saved){
                        displayAlert('Done', 'Suscription Added', 'success');
                        email_value.val('')
                    }else if(data.email_exists){
                        displayAlert('Hey', 'This email is subscribed', 'warning');
                    }else{
                        displayAlert('Error', 'An unknown error occurred', 'error');
                    }
                },
                error: function(error){
                    displayAlert('Error', error.status+': '+error.statusText, 'error');
                }
            });

        }else{
            displayAlert('Hey', 'Incorrect email format', 'warning')
        }

    });
    // Validates contact sending
    $('#js-contact-btn').click((event) => {
        event.preventDefault();
        let name = $('#id_name').val();
        let email = $('#id_email').val();
        let subject = $('#id_subject').val();
        let message = $('#id_message').val();
        if(!name || !email || !subject || !message){
            displayAlert('Hey', "Fill in all input fields", 'warning');
        }else if(!is_email(email)){
            displayAlert('Hey', 'Incorrect email format', 'warning');
        }else{
            $('#contactForm').submit()
        }
    })
});


function displayAlert(head, message, type){
    Swal.fire({
        position: 'center',
        type: type,
        title: head,
        text: message,
        showConfirmButton: true,
        timer: 2000
    })
}

// Validate Email
function is_email(email){
    var regex = /^([a-zA-Z0-9_.+-])+@(([a-zA-Z0-9-])+\.)+([a-zA-Z0-9]{2,4})+$/;
    return regex.test(email);
}