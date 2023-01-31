async function makeRequest(url, method, body) {
    let headers = {
        'X-Requested-With': 'XMLHRequest',
        'Content-Type': 'application/json'
    }
    if (method === 'post') {
        const csrf = document.querySelector('[name=csrfmiddlewaretoken]').value
        headers['X-CSRFToken'] = csrf
    }
    let response = await fetch(
        url,
        {
            method: method,
            headers: headers,
            body: body
        })
    return await response.json()
}

form = document.forms[0]

form.addEventListener('submit', runCustomperiod)

async function runCustomperiod(e) {
    e.preventDefault()
    message = {
        start_date: document.forms[0].elements.start_date.value,
        start_time: document.forms[0].elements.start_time.value,
        end_date: document.forms[0].elements.end_date.value,
        end_time: document.forms[0].elements.end_time.value,
    }
    let data = await makeRequest('/', 'post', JSON.stringify(message))
    // один элемент ищется только по id!!!
    document.getElementById('pnl_total').innerText = await data['pnl_total']
    document.getElementById('index_pnl').innerText = await data['index_pnl']
    document.getElementById('profit_in_percent').innerText = await data['profit_in_prcnt']
    document.getElementById('period').innerText = await data['period']

}












// async function getNumber() {
//     let data = await makeRequest('/', 'get')
//     let ul_left = document.getElementById('left')
//     let li = document.createElement('li')
//     li.addEventListener('click', getFloatNumber)
//     li.innerText = await data['number']
//     ul_left.appendChild(li)
// }

// async function getFloatNumber(e) {
//     let number = e.target.innerText
//     let data = await makeRequest('/', 'post', JSON.stringify({ number: number }))
//     let ul_right = document.getElementById('right')
//     let li = document.createElement('li')
//     li.innerText = await data['float']
//     ul_right.appendChild(li)
// }
