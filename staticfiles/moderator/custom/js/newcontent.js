$(document).ready(function(){
    $('.js-select-stock-image').click(function(event){
        event.preventDefault();
        let image_element = $(this).children('img')[0];
        let image_source = $(image_element).attr('src');
        $('#id_display_image').val(image_source);
        $('#stockImageModal').modal('hide');
    })
});