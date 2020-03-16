$(document).ready(function(){
    let addContentTrigger = $('#addContentTrigger');
    let addContentForm = $('#addContentForm');
    addContentTrigger.on('click', () => {
        let validate_status = validateAddContent();
        if(validate_status){
            addContentForm.submit();
        }
    });
    // load next and previous page link for blog template
    loadPrevNextPageLink();
});

function validateAddContent(){
    let title = $('#id_title').val();
    let content = $('#id_content').val();
    let tags = $('#id_tags').val();
    let display_image = $('#id_display_image').val();

    if(title.length <= 0 || content.length <= 0 || display_image.length <= 0){
        displayAlert('center', 'warning', 'Ooops!', 'Fill in required fields');
        return false
    }
    return true
}

function loadPrevNextPageLink(){
    let prevPage = $('#js-prev-page');
    let nxtPage = $('#js-nxt-page');
    let currPage = $('#js-page-num').val();
    let pageLink = $('#js-page-link').val();
    let val = Number.parseInt(currPage);

    if(currPage){
        if(val <= 1){
            prevPage.attr('href', pageLink+1);
            nxtPage.attr('href', '#')
        }else{
            prevPage.attr('href', pageLink+(val-1));
            nxtPage.attr('href', pageLink+(val+1))
        }
    }else{
        nxtPage.attr('href', pageLink+2)
    }
}