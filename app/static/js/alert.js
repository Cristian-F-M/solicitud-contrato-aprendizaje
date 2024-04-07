var closesMessage = document.querySelectorAll('span.close')
const containerMessages = document.querySelector('.container-messages')
var messages = containerMessages.querySelectorAll('.message')
const root = document.documentElement;
const SVG_X = `<svg width="24" height="24" fill="none" stroke="currentColor" stroke-linecap="round" stroke-linejoin="round" stroke-width="2" class="icon icon-tabler icons-tabler-outline icon-tabler-x" viewBox="0 0 24 24"><path stroke="none" d="M0 0h24v24H0z"/><path d="M18 6 6 18M6 6l12 12"/></svg>`


function addEventCloseMessage() {
    var closesMessage = document.querySelectorAll('span.close')

    closesMessage.forEach(close => {
        close.addEventListener('click', () => {
            let message = close.closest('.message')
            closeMessage(message)
            message.style.animationDelay = ""
        })
    })
}




function getVariableRoot(variable) {
    let variableRoot = getComputedStyle(root).getPropertyValue(variable);
    variableRoot = variableRoot.trim().toLowerCase();

    let milliseconds = variableRoot.endsWith('ms') ? parseFloat(variableRoot) : parseFloat(variableRoot) * 1000;
    return milliseconds;
}




function starMessages() {
    messages = containerMessages.querySelectorAll('.message')

    let i = 1

    messages.forEach(message => {
        message.classList.add('show')
        message.style.animationDelay = `${i * 0.3}s`
        i++


        message.addEventListener('animationend', () => {
            let close = message.querySelector('span.loader')
            close.classList.add('show')

            let timeMessage = getVariableRoot('--time-message');
            let durationMessage = getVariableRoot('--duration-message');


            let timeClose = (timeMessage + durationMessage)


            setTimeout(() => {
                closeMessage(message)
            }, timeClose)


            if (!containerMessages.hasChildNodes(message))
                if (containerMessages.hasChildNodes(message))
                    containerMessages.removeChild(message)
        })
    })

}





function closeMessage(message) {
    message.classList.remove('show')
    message.classList.add('close')

    message.addEventListener('animationend', () => {
        message.remove()
    })
}

addEventCloseMessage()
starMessages()


function createMessage(text, mistake = false) {
    let message = document.createElement('div')
    let close = document.createElement('span')
    let p = document.createElement('p')
    let loader = document.createElement('span')
    let closeIcon = document.createElement('i')

    message.classList.add('message')
    close.classList.add('close')
    p.innerText = text
    loader.classList.add('loader')
    closeIcon.innerHTML = SVG_X
    close.appendChild(closeIcon)


    mistake && message.classList.add('mistake')

    message.appendChild(close)
    message.appendChild(p)
    message.appendChild(loader)

    containerMessages.appendChild(message)
    addEventCloseMessage()
    starMessages()
}
