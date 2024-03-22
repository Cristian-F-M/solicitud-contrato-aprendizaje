var closesMessage = document.querySelectorAll('span.close')
const containerMessages = document.querySelector('.container-messages')
var messages = containerMessages.querySelectorAll('.message')
const root = document.documentElement;


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
    closeIcon.classList.add('bi', 'bi-x-lg')
    close.appendChild(closeIcon)


    mistake && message.classList.add('mistake')

    message.appendChild(close)
    message.appendChild(p)
    message.appendChild(loader)

    containerMessages.appendChild(message)
    addEventCloseMessage()
    starMessages()
}


document.getElementById('button-createMessage').addEventListener('click', () => {
    let mistake = document.getElementById('input-mistake').checked
    createMessage(document.getElementById('input-createMessage').value, mistake)
})