const form = document.getElementById('searchBar');

form.addEventListener('submit', async (event) => {
  
event.preventDefault();
//stop page from reloading after html form input :)

const ticker = document.getElementById('IPO').value
fetch ('http://127.0.0.1:8000/stock/' + ticker, {})
    .then (response => response.json())

    .then (data => {
        document.getElementById('testTicker').innerText = 'Current price: $' + data.price
        })

    .catch (error => {
        console.log(error)
    })
})

