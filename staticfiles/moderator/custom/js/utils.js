function sendAjaxRequest(toURL, type, data, dtype){
    return $.ajax({
        url: toURL,
        type: type,
        data: data,
        dataType: dtype
    });
}

function displayAlert(position, type, title, text="", timer=3000, delay=0){
    setTimeout(()=>{
        Swal.fire({
            position: position,
            type: type,
            title: title,
            text: text,
            showConfirmButton: false,
            timer: timer
        })
    }, delay)
}

function validateEmail(email) {
    var re = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
    return re.test(String(email).toLowerCase());
}