$(document).ready(function(){
    // Handle Comment Posting
    $('#js_post_comment').click((event) => {
        event.preventDefault();
        validatePostComment();
    });
    // when new notificaton icon is clicked
    $('#js-new-noti-link-click').click((event)=>{
        event.preventDefault();
        scrollToTopOfComment();
    });
    // add scroll event listener to comment box to hide noti
    $('#js-comment-dialog').scroll(function(){
        let position = $(this).scrollTop();
        if(position <= 0){
            $('#js-new-noti-link-click').fadeOut('fast');
        }
    });
    // refresh for new comment
    setInterval(function(){loadNewComments()}, 2000)
});


function loadNewComments(){
    var comment_block = $('#js-comment-dialog');
    let fetch_new_comment_url = $('#js-fetch-new-comment-url').val();
    // let prev_no_of_comment = $('#js-no-fetched-comment');
    let prev_no_of_comment = $('#js-comment-dialog .comment-list:first-child').attr('last-index');
    let blog_id = $('#js_post_id').val();
    let comment_tmp_img = $('#js-comment-img').val();
    let update_no_comment_block = $('.js-toggle-no-comment');

    let new_comment_content = getNewCommentHTMLContent();

    let getStatus = sendAjaxRequest(
        fetch_new_comment_url,
        'GET',
        {'blog_id': blog_id, 'last_comment_index': prev_no_of_comment},
        'json'
    );
    getStatus.done((data) => {
        if(data.new_comments){
            var new_comment_objects = data.new_comments;
            let tmp_no_comment = data.new_no_of_comment;
            for(let i=0; i<new_comment_objects.length;i++){
                let single_comment_obj = new_comment_objects[i];
                let tmp_image = comment_tmp_img;
                let tmp_id = single_comment_obj.id;
                let tmp_user = single_comment_obj.user;
                let tmp_date = single_comment_obj.date_created;
                tmp_date = formatForCommentDate(tmp_date);  // format to date
                let tmp_time = single_comment_obj.date_created;
                tmp_time = formatForCommentTime(tmp_time);
                let tmp_message = single_comment_obj.message;
                let comment_content = new_comment_content.format(
                    tmp_id, tmp_image,tmp_user,tmp_date,tmp_time,tmp_message,tmp_message
                );
                comment_block.prepend(comment_content);
                update_no_comment_block.text(tmp_no_comment);
                if(comment_block.scrollTop() > 0){
                    $('#js-new-noti-link-click').fadeIn('slow');
                }
            }
        }

    });



}

function formatForCommentDate(timestamp){
    try{
        let tmp_date = new Date(timestamp);
        let month = getMonths()[tmp_date.getMonth()];
        let day = tmp_date.getDate();
        let year = tmp_date.getFullYear();
        return month + '&nbsp;' + day + ',&nbsp' + year
    }catch (e) {
        return ''
    }
}

function formatForCommentTime(timestamp){
    try{
        let tmp_date= new Date(timestamp);
        let tmp_time = tmp_date.getUTCHours();
        let tmp_minutes = tmp_date.getUTCMinutes();
        let mid = 'a.m.';
        if(tmp_time >= 12 && tmp_time < 24){
            mid = 'p.m.';
        }
        tmp_time = tmp_time%12;
        if(tmp_time === 0){
            tmp_time = 12;
        }
        return tmp_time + ':' + tmp_minutes + '&nbsp;' + mid;
    }catch (e) {
        return ''
    }
}

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

function scrollToTopOfComment(){
    let comment_box = $('#js-comment-dialog');
    comment_box.animate({
        scrollTop: 0
    }, 1000);
}