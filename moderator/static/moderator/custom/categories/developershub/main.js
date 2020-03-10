$(document).ready(function(){
    let addContentTrigger = $('#addContentTrigger');
    let addContentForm = $('#addContentForm');
    addContentTrigger.on('click', () => {
        let validate_status = validateAddContent();
        if(validate_status){
            addContentForm.submit();
        }
    })
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