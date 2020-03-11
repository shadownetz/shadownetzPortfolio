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

function getNewCommentHTMLContent(){
    return `
    <div class='comment-list' last-index="{0}">
        <div class="single-comment justify-content-between d-flex">
             <div class="user justify-content-between d-flex">
                <div class="thumb">
                   <div style="background-image: url('{1}')" class="comment-img"></div>
                </div>
                <div class="desc">
                    <h5><a href="#">{2}</a></h5>
                    <p class="date">{3} at {4}</p>
                    <p class="comment">
                        {5}
                    </p>
                </div>
             </div>
        </div>
    </div>
    `;
}

function getMonths(){
    return ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ];
}