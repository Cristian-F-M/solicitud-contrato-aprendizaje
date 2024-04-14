const $openCloseMenu = document.querySelector('.open-close-left-menu');
const $containerLeftMenu = document.querySelector('.container-left-menu');


$openCloseMenu.addEventListener('click', () => {
    $containerLeftMenu.classList.toggle('open-menu');
});



document.addEventListener('click', ({ target }) => {
    let isNotOpenCloseMenu = !$containerLeftMenu.contains(target);

    if (isNotOpenCloseMenu) $containerLeftMenu.classList.remove('open-menu');
})



