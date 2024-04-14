const $iconsMoreMenu = document.querySelectorAll('.icon-more-options');
const $containerActions = document.querySelector('.container-actions');
const $linksActions = $containerActions.querySelectorAll('a')
const $closesOverlay = document.querySelectorAll('.close i')
const $overlays = document.querySelectorAll('.overlay')

$iconsMoreMenu.forEach(icon => {
    icon.addEventListener('click', () => {
        const $containerMoreOptions = icon.nextElementSibling;
        $containerMoreOptions.classList.toggle('show');
    });
})



document.addEventListener('click', ({ target }) => {
    $iconsMoreMenu.forEach(icon => {
        let $containerMoreOptions = icon.nextElementSibling;
        let isNotOpenCloseMenu = !$containerMoreOptions.contains(target) && !icon.contains(target);

        if (isNotOpenCloseMenu) $containerMoreOptions.classList.remove('show');
    })


})


$containerActions.addEventListener('wheel', (event) => {
    if (event.deltaY !== 0) {
        event.preventDefault();
        $containerActions.scrollLeft += (event.deltaY * 2);
    }
});


function handleKeyDown(event) {
    if (event.key === 'ArrowRight') {
        $containerActions.scrollLeft += 100;
    } else if (event.key === 'ArrowLeft') {
        $containerActions.scrollLeft -= 100;
    }
}

$containerActions.addEventListener('mouseenter', () => {
    document.addEventListener('keydown', () => {
        document.addEventListener('keydown', handleKeyDown);
    });
});


$containerActions.addEventListener('mouseleave', () => {
    $containerActions.addEventListener('mouseleave', () => {
        document.removeEventListener('keydown', handleKeyDown);
    });
});


$linksActions.forEach(link => {
    link.addEventListener('click', evt => {
        evt.preventDefault()

        let $overlay = document.querySelector(`div[data-id='${link.id}']`)
        $overlay?.classList.add('show')

    })
})


$closesOverlay.forEach(close => {
    close.addEventListener('click', () => {
        let $overlay = document.querySelector(`div[data-id='${close.dataset.id}']`)
        $overlay?.classList.remove('show')
    })
})



document.addEventListener('keyup', ({ key }) => {
    if (key == "Escape") {
        $overlays.forEach(overlay => {
            if (overlay.classList.contains('show')) return overlay.classList.remove('show')
        })
    }
})


$overlays.forEach(overlay => {
    overlay.addEventListener('click', ({ target }) => {
        if (overlay === target) return overlay.classList.remove('show')
    })
})