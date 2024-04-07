const buttonSearchEmails = document.getElementById('button-search-emails');
let iMoreOptions = document.querySelectorAll('[data-name="more-options"]')
const aBlacklist = document.querySelectorAll('[data-name="more-options"] + .container-more-options ul li a')
const mainSearchEmails = document.querySelector('.main-search-emails')
const tbodyTableCompanies = document.getElementById('tbody-table-companies')
const containerTableCompanies = document.querySelector('.container-table-companies')
const containerInformationSearch = document.querySelector('.container-information-search')
const containerMessage = document.querySelector('.container-message')
const lastUpdate = document.getElementById('lastUpdate')
const cantCompanies = document.getElementById('cantCompanies')
var searching = false


aBlacklist.forEach(a => {
    a.addEventListener('click', () => {
        sessionStorage.setItem('scrollPosition', mainSearchEmails.scrollTop);
        console.log(mainSearchEmails.scrollTop)
    })
})

// // Restaura la posición del scroll cuando la página se carga
window.onload = function () {
    var scrollPosition = sessionStorage.getItem('scrollPosition');
    if (scrollPosition) {
        setTimeout(function () {
            mainSearchEmails.scrollTo({
                top: scrollPosition,
                behavior: 'smooth'
            });
            sessionStorage.removeItem('scrollPosition');
        }, 100);

    }
};



buttonSearchEmails.addEventListener('click', async () => {


    if (searching) return

    showInformation()
    showFullLoading()

    setTimeout(() => {
        closeInformation()
    }, 5000)

    searching = true
    buttonSearchEmails.disabled = true

    data = await searchEmails();

    const { information, companies } = data


    tbodyTableCompanies.innerHTML = ''


    companies.forEach(company => {


        const tr = createTrTableCompanies(company)

        tbodyTableCompanies.appendChild(tr)

    })


    lastUpdate.innerText = information.lastUpdated
    cantCompanies.innerText = information.cantCompanies

    closeMoreOptions()

    if (!containerTableCompanies.classList.contains('show')) {
        containerTableCompanies.classList.toggle('show')
    }

    if (!containerInformationSearch.classList.contains('show')) {
        containerInformationSearch.classList.toggle('show')
    }

    if (containerMessage.classList.contains('show')) {
        containerMessage.classList.toggle('show')
    }

    buttonSearchEmails.disabled = false
    searching = false
    hideFullLoading()
    showSearchCompleted()
})




async function searchEmails() {
    const response = await fetch('/Company/Search-Emails', {
        method: 'POST',
    })
    const data = await response.json();
    return data;
}



iMoreOptions.forEach(i => {
    i.addEventListener('click', () => {
        let containerMoreOptions = i.nextElementSibling
        containerMoreOptions.classList.toggle('show')
    })
})

closeMoreOptions()

function closeMoreOptions() {

    iMoreOptions = document.querySelectorAll('[data-name="more-options"]')

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
}





function createTrTableCompanies(company) {
    const { company_id, company_name, company_email_address, company_departament, company_city, blacklisted } = company

    let URLS_BLACKLIST = {
        add: `/company/add/${company_id}`,
        remove: `/company/remove/${company_id}`
    }


    let tr = document.createElement('tr')
    let tdName = document.createElement('td')
    let tdEmail = document.createElement('td')
    let tdLocation = document.createElement('td')
    let tdActions = document.createElement('td')
    let i = document.createElement('i')
    let div = document.createElement('div')
    let ul = document.createElement('ul')
    let li = document.createElement('li')
    let a = document.createElement('a')

    i.classList.add('bi', 'bi-list')
    i.setAttribute('title', 'More options')
    i.setAttribute('data-name', 'more-options')

    i.addEventListener('click', () => {
        let containerMoreOptions = i.nextElementSibling
        containerMoreOptions.classList.toggle('show')
    })



    div.classList.add('container-more-options')
    tdEmail.classList.add('text-18')


    a.setAttribute('href', blacklisted ? URLS_BLACKLIST.remove : URLS_BLACKLIST.add)
    a.textContent = blacklisted ? 'Remove to blacklist' : 'Add to blacklist'

    div.appendChild(ul)
    ul.appendChild(li)
    li.appendChild(a)

    tdActions.appendChild(i)
    tdActions.appendChild(div)





    tdName.textContent = company_name
    tdEmail.textContent = company_email_address
    tdLocation.textContent = `${company_departament} / ${company_city}`



    tr.appendChild(tdName)
    tr.appendChild(tdEmail)
    tr.appendChild(tdLocation)
    tr.appendChild(tdActions)

    return tr
}





