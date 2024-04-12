var orderInfoElement = document.querySelector('#order-info');
var shipping = orderInfoElement.getAttribute('data-shipping');
var storeUrl = orderInfoElement.getAttribute('data-store-url');

if(user != 'AnonymousUser'){
    document.getElementById('user-info').innerHTML = ''
}

var form = document.getElementById('form')
form.addEventListener('submit', function(e){
    e.preventDefault()
    console.log('Form Submitted...')
    document.getElementById('form-button').classList.add("hidden")
    document.getElementById('payment-info').classList.remove("hidden")
    document.getElementById('shipping-info').classList.add("hidden")
    document.getElementById('user-info').classList.add("hidden");
    
})

function submitFormData(){
    console.log('Payment button clicked')

    var userFormData = {
        'name':null,
        'email':null,
        'total':total,
    }

    var shippingInfo = {
        'address':null,
        'city':null,
        'zipcode':null,
        'country':null,
    }

    shippingInfo.address = form.address.value
    shippingInfo.city = form.city.value
    shippingInfo.zipcode = form.zipcode.value
    shippingInfo.country = form.country.value

    if (user == 'AnonymousUser'){
        userFormData.name = form.name.value
        userFormData.email = form.email.value
    }

    console.log('Shipping Info:', shippingInfo)
    console.log('User Info:', userFormData)

    var currentLanguage = getLang('django_language') || 'en';
    var url = '/' + currentLanguage + '/process_order/'
    fetch(url, {
        method:'POST',
        headers:{
            'Content-Type':'application/json',
            'X-CSRFToken':csrftoken,
        }, 
        body:JSON.stringify({'form':userFormData, 'shipping':shippingInfo}),
        
    })
    
    .then((response) => response.json())
    .then((data) => {
          console.log('Success:', data)
          alert('Transaction completed')
          cart = {}
          document.cookie ='cart=' + JSON.stringify(cart) + ";domain=;path=/"
          window.location.href = storeUrl
        })
}

function getLang(name) {
    var cookieArr = document.cookie.split(";");
    
    for(var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");
        
        if(name == cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }
    
    return null;
}
    