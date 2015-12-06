/**
 * Created by Job on 12/6/2015.
 */
$(function () {
    $(document).foundation();
    $('.text_area').ckeditor(
        {
            skin:'flat',
            removePlugins : 'elementspath'
        }
    );
});