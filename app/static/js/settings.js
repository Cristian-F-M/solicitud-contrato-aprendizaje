const asNavSettings = document.querySelectorAll('.nav-settings ul li a')
const containers = document.querySelectorAll('.main-settings div')
const mailContent = document.getElementById('mail-content')
const inputs = document.querySelectorAll('input, textarea')
const previewCv = document.getElementById('preview-cv')
const inputCv = document.getElementById('input-cv')
const dropsDown = document.querySelectorAll('.drop-down h3')


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
    previewCv.classList.add('object')
    previewCv.removeChild(previewCv.querySelector('span'))
    previewCv.appendChild(objectPreviewCv)
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