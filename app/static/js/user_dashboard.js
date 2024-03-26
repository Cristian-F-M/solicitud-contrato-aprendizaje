const header = document.querySelector('header')
const main = document.querySelector('.main')
const containersNameIco = document.querySelectorAll('.container-name-ico')
const navWebCaprendizaje = document.getElementById('nav-web-caprendizaje')
const navMin = document.getElementById('nav-min')
const iOpenCloseMenu = document.getElementById('i-open-close-menu')
let leftMenu = document.querySelector('.container-left-menu')
const minMenuLi = document.querySelector('#nav-min li')
const localStorageName = "minMenu"

main.style.setProperty('--height-header', `${header.clientHeight}px`)
leftMenu.style.setProperty('--height-header', `${header.clientHeight}px`)






containersNameIco.forEach(nameIco => {
    nameIco.addEventListener('click', (evt) => {
        evt.preventDefault()
        let li = nameIco.parentNode
        let containerActions = li.querySelector('.container-actions')



        if (li.hasAttribute('show')) {
            li.removeAttribute('show')
        } else {
            li.setAttribute('show', '')
        }


    })
})



iOpenCloseMenu.addEventListener('click', () => {
    if (!leftMenu.hasAttribute('min')) {
        openMinMenu()
    } else {
        openLeftMenu()
    }
})

minMenuLi.addEventListener('click', () => {
    openLeftMenu()
})


function openLeftMenu() {
    leftMenu.removeAttribute('min')
    styleIcoMenu()
}

function openMinMenu() {
    leftMenu.setAttribute('min', '')
    styleIcoMenu()
}


function styleIcoMenu() {
    if (leftMenu.hasAttribute('min')) {
        iOpenCloseMenu.parentNode.removeAttribute('show')
    } else {
        iOpenCloseMenu.parentNode.setAttribute('show', '')
    }
}


function parseBoolean(string) {
    return string === "true";
}


function saveStateMenu() {
    let stateMenu = getStateMenu()
    window.localStorage.setItem(localStorageName, stateMenu)
}


function getStateMenu() {
    leftMenu = document.querySelector('.container-left-menu')
    const stateMenu = leftMenu.hasAttribute('min')

    return stateMenu
}


loadStateMenu()

function loadStateMenu() {
    let stateMenu = window.localStorage.getItem(localStorageName)
    stateMenu && parseBoolean(stateMenu) ? openMinMenu() : openLeftMenu()
}


iOpenCloseMenu.addEventListener('click', saveStateMenu)
minMenuLi.addEventListener('click', saveStateMenu)



function parseBoolean(string) {
    return string === "true";
}