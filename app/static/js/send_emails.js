const containerFilterDepartments = document.querySelector('.container-filter-departments');
const containerFilterCities = document.querySelector('.container-filter-cities');
const filterByDepartment = document.querySelector("#send-departments")
const filterByCity = document.querySelector("#send-cities")
const closeFilterDepartments = document.querySelector('#close-filter-department');
const closeFilterCities = document.querySelector('#close-filter-city');
const sendAll = document.querySelector('#send-all');
const containerLocationsDepartments = containerFilterDepartments.querySelector('.container-locations');
const containerLocationsCities = containerFilterCities.querySelector('.container-locations');
const containerUpDown = document.querySelectorAll('.container-up-down')
const mainsFilter = document.querySelectorAll('.main-filter')
const buttonsApply = [...document.querySelectorAll('.button-apply')]
const containerFilters = document.querySelector('.container-filters')
const containersInput = containerFilters.querySelectorAll('.container-input')
const containerInformation = document.querySelector('.container-information')
const informationLocations = containerInformation.querySelector('.information_container-locations .locations')
const sendEmails = document.querySelector('#send-emails')
const filterSelected = {
    "inputChecked": checkFilterSelected()
}

sendAll.addEventListener('change', () => {
    let dataLocations = {
        "dataName": "all"
    }

    resetAll(containerFilterDepartments, true)
    resetAll(containerFilterCities, true)
    addSendTo(dataLocations)
    containerInformation.setAttribute('show', 'all')
})


filterByDepartment.addEventListener('change', () => {
    setTimeout(() => {
        filterByDepartment.checked && showFilterDepartments()
    }, 200)
})


filterByCity.addEventListener('change', () => {
    setTimeout(() => {
        filterByCity.checked && showFilterCities()
    }, 200)
})



closeFilterCities.addEventListener('click', () => {
    hideFilter(containerFilterCities)
})
closeFilterDepartments.addEventListener('click', () => {
    hideFilter(containerFilterDepartments)
})



function showFilterDepartments() {
    showFilter(containerFilterDepartments)
}

function showFilterCities() {
    showFilter(containerFilterCities)
}





function showFilter(filter) {
    filter?.classList.add('show');
}

function hideFilter(filter) {
    filter.classList.remove('show');
    let checked = checkInputsChecked(filter)

    !checked && resetAll(filter);
}


function checkInputsChecked(container) {
    let checkboxes = container.querySelectorAll('input[type="checkbox"]')
    let checked = false

    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            checked = true
        }
    })

    return checked
}


function resetAll(container, all = false) {
    let checkboxes = container.querySelectorAll('input[type="checkbox"]');
    let header = container.querySelector('header')
    let mainFilter = container.querySelector('.main-filter')
    let filterId = filterSelected.inputChecked.id
    let inputFilter = document.querySelector(`input#${filterId}`)

    checkboxes.forEach(checkbox => {
        checkbox.checked = false;
    })

    inputFilter.checked = true;

    if (all) {
        sendAll.checked = true;
    }

    header.classList.remove('scroll-blur')
    mainFilter.scrollTop = 0;

}




containerUpDown.forEach(upDown => {
    upDown.addEventListener('click', () => {
        let mainFilter = upDown.closest('.main-filter')
        let apply = mainFilter.querySelector('.button-apply')

        apply.scrollIntoView({ behavior: 'smooth' })
    })
})





mainsFilter.forEach(mainFilter => {
    let upDown = mainFilter.querySelector('.container-up-down')
    let header = mainFilter.querySelector('header')


    mainFilter.addEventListener('scroll', () => {
        let scrollLocation = mainFilter.scrollHeight - mainFilter.scrollTop

        mainFilter.scrollTop > 0 ? header.classList.add('scroll-blur') : header.classList.remove('scroll-blur')



        if (scrollLocation === mainFilter.clientHeight) {
            upDown.classList.add('hidden')
        } else if (scrollLocation > mainFilter.clientHeight + 80) {
            upDown.classList.remove('hidden')
        }
    });
})


for (let i in buttonsApply) {
    let buttonApply = buttonsApply[i]

    buttonApply.addEventListener('click', (evt) => {
        let overlayFilter = buttonApply.closest('.overlay-filter')
        let checkedLocations = overlayFilter.querySelectorAll('input[type="checkbox"]:checked')
        let show = "location"


        if (checkedLocations.length === 0) {
            sendAll.checked = true
            show = "all"
        }

        getLocationsFilter(evt)
        updateContainerLocations(overlayFilter)
        containerInformation.setAttribute('show', show)
    })
}



async function addSendTo(data, containerFilter = undefined) {

    let overlayFilter = containerFilter?.closest('.overlay-filter')


    let response = await fetch('/Location/Send-to/', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })

    response = await response.json()


    if (!response.ok) {
        createMessage('An error occurred while processing the request', true)
        resetAll(containerFilter)
        return
    }

    createMessage('filters have been applied correctly', false)
    containerFilter && hideFilter(overlayFilter)

}


function getLocationsFilter({ target }) {
    let containerFilter = target.closest('.main-filter')
    let dataName = target.dataset.name
    let checkboxes = containerFilter.querySelectorAll('input[type="checkbox"]')

    let locations = []

    checkboxes.forEach(checkbox => {
        if (checkbox.checked) {
            let value = parseInt(checkbox.value)
            locations.push(value)
        }
    })


    let dataLocations = {
        "dataName": dataName,
        "locations": locations,
    }

    addSendTo(dataLocations, containerFilter)

}

containersInput.forEach(containerInput => {
    let label = containerInput.querySelector('label')



    label.addEventListener('click', () => {
        let input = containerInput.querySelector('input')
        let inputId = label.getAttribute('for')
        let idEnd = inputId.split('-')[1]
        let container = document.querySelector(`.container-filter-${idEnd}`)

        if (!input.checked) return

        showFilter(container)

    })
})


function checkFilterSelected() {
    let listContainersInput = [...containersInput]

    for (let i in listContainersInput) {
        let container = listContainersInput[i]
        let input = container.querySelector('input')


        if (input.checked) {
            return input
        }
    }
    return sendAll
}


function updateContainerLocations(overlayFilter) {
    informationLocations.innerHTML = ''

    let locationsChecked = overlayFilter.querySelectorAll('input[type="checkbox"]:checked')

    locationsChecked.forEach(location => {
        let containerInput = location.closest('.container-input')
        let label = containerInput.querySelector('label')
        let span = document.createElement('span')

        span.innerText = label.innerText
        span.setAttribute('value', location.id)
        span.classList.add('tag')

        informationLocations.appendChild(span)
    })

}


sendEmails.addEventListener('click', async () => {
    let response = await send_emails()

    if (!response.status) {
        let msg = response.message ? response.message : 'An error occurred while processing the request'
        createMessage(msg, true)
        return
    }

    createMessage('The email has been sent correctly to all companies')
})

async function send_emails() {
    let result = await sendApi({
        "send_to": "user"
    })
    let response = confirm('We have sent you an example email so you can review the final result. Upon confirmation, the emails will be sent to all companies. ')


    if (!response) {
        return
    }

    result = await sendApi({
        "send_to": "all"
    })

    response = await result.json()

    await new Promise(resolve => setTimeout(resolve, 2000))

    return response
}


async function sendApi(data) {
    sendEmails.disabled = true
    showFullLoading("Sending emails")

    let result = await fetch('/User/Send-emails', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify(data)
    })

    sendEmails.disabled = false
    hideFullLoading()
    return result
}