const asNavSettings = document.querySelectorAll('.nav-settings ul li a')
const containers = document.querySelectorAll('.main-settings div')
const mailContent = document.getElementById('mail-content')
const inputs = document.querySelectorAll('input, textarea')
const previewCv = document.getElementById('preview-cv')
const inputCv = document.getElementById('input-cv')
const dropsDown = document.querySelectorAll('.drop-down h3')
const isPassword = document.querySelectorAll('.i-password')
const iMoreOptions = document.querySelectorAll('[data-name="more-options"]')
const SVG_EYES_PASSWORD = {
    "EYE": `<svg width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="icon icon-tabler icons-tabler-outline icon-tabler-eye" viewBox="0 0 24 24"><path stroke="none" d="M0 0h24v24H0z"/><path d="M10 12a2 2 0 1 0 4 0 2 2 0 0 0-4 0"/><path d="M21 12c-2.4 4-5.4 6-9 6-3.6 0-6.6-2-9-6 2.4-4 5.4-6 9-6 3.6 0 6.6 2 9 6"/></svg>`,
    "EYE_OFF": `<svg width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="icon icon-tabler icons-tabler-outline icon-tabler-eye-off" viewBox="0 0 24 24"><path stroke="none" d="M0 0h24v24H0z"/><path d="M10.585 10.587a2 2 0 0 0 2.829 2.828"/><path d="M16.681 16.673A8.717 8.717 0 0 1 12 18c-3.6 0-6.6-2-9-6 1.272-2.12 2.712-3.678 4.32-4.674m2.86-1.146A9.055 9.055 0 0 1 12 6c3.6 0 6.6 2 9 6-.666 1.11-1.379 2.067-2.138 2.87M3 3l18 18"/></svg>`
}


asNavSettings.forEach(a => {
    let container = document.querySelector(`.main-settings div[data-name="${a.dataset.name}"]`)


    a.addEventListener('click', (evt) => {
        evt.preventDefault()

        // Para eliminar el show de todos los containers y asNavSettings
        containers.forEach(container => {
            container.removeAttribute('show')
        })

        // Para eliminar el show de todos los  asNavSettings
        asNavSettings.forEach(a => {
            a.removeAttribute('show')
        })

        // Para agregar el show al container y al asNavSettings seleccionado
        container.setAttribute('show', '')
        a.setAttribute('show', '')


        setTimeout(() => {

            let urlParams = new URLSearchParams(window.location.search);
            urlParams.set('tag', (a.dataset.name).toLowerCase());
            let nuevaURL = `${window.location.origin}${window.location.pathname}?${urlParams.toString()}`;
            history.pushState({}, '', nuevaURL);
        }, 0)


    })
})



inputs.forEach(input => {
    let label = document.querySelector(`label[for="${input.id}"]`)
    if (input.required) {
        label.innerHTML += ' <span class="required">*</span>'
    }
})


inputCv.addEventListener('change', (evt) => {
    let objectPreviewCv = createObjectCv(evt)
    let span = previewCv.querySelector('span')
    let file_user = previewCv.querySelector('#file_user')

    previewCv.classList.add('object')
    previewCv.appendChild(objectPreviewCv)


    if (span) {
        span.remove()
    }
    if (file_user) {
        file_user.remove()
    }
})



function createObjectCv(evt) {
    let url = URL.createObjectURL(evt.target.files[0])
    let objectPreviewCv = document.createElement('object')
    objectPreviewCv.setAttribute('type', 'application/pdf')
    objectPreviewCv.id = 'object-preview-cv'
    objectPreviewCv.setAttribute('data', url)

    return objectPreviewCv
}




dropsDown.forEach(dropdown => {
    let containerDropdown = dropdown.parentNode
    dropdown.addEventListener('click', () => {
        resetDropdownsLocation(containerDropdown)

        if (containerDropdown.classList.contains('departament')) {
            resetAllDropdowns(containerDropdown)
            toggleDropdownDepartament(containerDropdown, dropdown)
        } else if (containerDropdown.classList.contains('city')) {
            toggleDropdownCity(containerDropdown, dropdown)
        }
    })
})


function toggleDropdownDepartament(containerDropdown, dropdown) {
    let content = containerDropdown.querySelector('.container-cities')
    let marginTopContent = getStyleComputed(content, "margin-top")
    let contentHeight = content.offsetHeight
    let dropdownHeight = dropdown.offsetHeight
    let maxHeightContainer = marginTopContent + contentHeight + dropdownHeight

    containerDropdown.classList.toggle('show')
    containerDropdown.style.maxHeight = (!containerDropdown.classList.contains('show')) ? "50px" : `${maxHeightContainer}px`

}

function toggleDropdownCity(containerDropdown, dropdown) {
    let content = containerDropdown.querySelector('.container-emails')
    let containerDepartament = containerDropdown.closest('.departament')
    let dropdownHeight = dropdown.offsetHeight
    let marginTopContent = getStyleComputed(content, "margin-top")
    let contentHeight = content.offsetHeight
    let maxHeightContainer = dropdownHeight + marginTopContent + contentHeight
    let contentCities = containerDepartament.querySelector('.container-cities')
    let marginTopContentCities = getStyleComputed(contentCities, "margin-top")
    let dropdownDepartament = containerDepartament.querySelector('h3')

    containerDropdown.classList.toggle('show')
    containerDropdown.style.maxHeight = (!containerDropdown.classList.contains('show')) ? "50px" : `${maxHeightContainer}px`
    containerDepartament.style.maxHeight = `${maxHeightContainer + contentCities.offsetHeight + marginTopContentCities + dropdownDepartament.offsetHeight}px`
}

function getStyleComputed(element, property) {
    return parseInt(window.getComputedStyle(element, null).getPropertyValue(property))
}

function resetDropdownsLocation(containerDropdown) {
    let containerDepartaments = containerDropdown.parentNode
    let classContainerDropdown = containerDropdown.classList.contains('departament') ? 'departament' : 'city'
    let allDropdowns = containerDepartaments.querySelectorAll(`.drop-down.${classContainerDropdown}`)

    allDropdowns.forEach(dropdown => {
        if (dropdown !== containerDropdown) {
            dropdown.classList.remove('show')
            dropdown.style.maxHeight = "50px"
        }
    })
}

function resetAllDropdowns(containerDropdown2) {
    dropsDown.forEach(dropdown => {
        let containerDropdown = dropdown.parentNode
        if (containerDropdown !== containerDropdown2) {
            containerDropdown.classList.remove('show')
            containerDropdown.style.maxHeight = "50px"
        }
    })
}


function getNextDropdowns(currentElement, element) {
    let dropdowns = [];
    let nextSibling = currentElement.nextElementSibling;

    while (nextSibling) {
        if (nextSibling.classList.contains(element)) {
            dropdowns.push(nextSibling);
        }
        nextSibling = nextSibling.nextElementSibling;
    }

    return dropdowns;
}


isPassword.forEach(i => {
    i.addEventListener('click', () => {
        let input = i.previousElementSibling
        let type = input.getAttribute('type')

        i.innerHTML = type === "password" ? SVG_EYES_PASSWORD.EYE_OFF : SVG_EYES_PASSWORD.EYE
        input.setAttribute('type', (type === 'password') ? 'text' : 'password')
    })
})



iMoreOptions.forEach(i => {
    i.addEventListener('click', () => {
        let containerMoreOptions = i.nextElementSibling
        containerMoreOptions.classList.toggle('show')
    })
})



document.addEventListener('click', (evt) => {
    let element = evt.target
    iMoreOptions.forEach(i => {
        let containerMoreOptions = i.nextElementSibling
        let svg = i.querySelector('svg')
        if (element != i && element != containerMoreOptions && element != svg) {
            containerMoreOptions.classList.remove('show')
        }

    })
})
