$(document).ready(function(){
    // Handle Comment Posting
    $('#js_post_comment').click((event) => {
        event.preventDefault();
        validatePostComment();
    })
});

function validatePostComment(){
    let email_value = $('#js_post_email').val();
    let message = $('#js_post_message').val();
    let blog_id = $('#js_post_id').val();

    let email_status = validateEmail(email_value);
    if(!email_status){
        displayAlert('center', 'warning', 'Oops!', "Incorrect email format detected.");
        return
    }
    if(message.length <= 0){
        displayAlert('center', 'warning', 'Oops!', "Type in a valid reply");
        return
    }
    let post_comment_url = $('#js_post_comment_url').val();
    let post_status = sendAjaxRequest(
        post_comment_url,
        'POST',
        {'id': blog_id, 'email': email_value, 'message': message},
        'json'
    );
    post_status.done((data)=>{
        if(data.post_status){
            displayAlert('center', 'success', 'Posted','',1000);
            resetPostCommentValues();
        }else{
            displayAlert('center', 'error', 'Error', 'Unable to post message',1000)
        }
    });
    post_status.fail((jqXHR, textStatus, errorThrown) => {
        let error_message = textStatus + ':' + errorThrown;
        displayAlert('center', 'error', error_message)
    });
}
function resetPostCommentValues(){
    $('#js_post_email').val("");
    $('#js_post_message').val("");
}