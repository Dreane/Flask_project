title_service = document.querySelectorAll('.title_service');
descr_service = document.querySelectorAll('.descr_service');
menu = document.querySelectorAll('.menu_btn');

function hide_descr(){
    descr_service.forEach(e => {
        e.style = 'display:none;';
    });
}
hide_descr();
title_service.forEach(function(e, i) {
    e.addEventListener("click", function() {
        hide_descr()
        descr_service[i].style = 'display:block;';
    });
});

menu.forEach(e => {
     e.addEventListener('click', function(){
        console.log(e.nextSibling());
        this.classList.toggle('active');
        menu_content = this.nextSibling;
        if (menu_content.style.maxHeight){
            menu_content.style.maxHeight = null;
        }
        else{
            menu_content.style.maxHeight = menu_content.scrollHeight;
        }
    })

});
   