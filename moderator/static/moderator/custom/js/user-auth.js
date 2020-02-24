$(document).ready(function(){
    $('#loginsubmit').click(function(event){
        event.preventDefault();
        validateLogin();
    })
});

function validateLogin(){
    let emailOriginLink = $('#emailoriginlink').val();
    let emailAddress = $('#id_email').val();
    let passcode = $('#id_password').val();
    let loginFormBox = $('#loginform');

    if(emailAddress.length <= 0 || passcode.length <= 0){
        displayAlert('center', 'warning', 'Fill in your login details');
        return
    }else if(!validateEmail(emailAddress)){
        displayAlert('center', 'error', 'Wrong email format detected');
        return
    }
    let emailStatus = sendAjaxRequest(
        emailOriginLink,
        'GET',
        {'email': emailAddress},
        'json'
    );
    emailStatus.done((data) => {
        if(data.exist){
            loginFormBox.submit()
        }else{
            displayAlert('center', 'warning', 'The email address does not exist')
        }
    });
    emailStatus.fail((jqXHR, textStatus, errorThrown) => {
        let error_message = textStatus + ':' + errorThrown;
        displayAlert('center', 'error', error_message)
    });
}

function sendAjaxRequest(toURL, type, data, dtype){
    return $.ajax({
        url: toURL,
        type: type,
        data: data,
        dataType: dtype
    });
}

function displayAlert(position, type, title, timer=3000){
    Swal.fire({
        position: position,
        type: type,
        title: title,
        showConfirmButton: false,
        timer: timer
    })
}

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}