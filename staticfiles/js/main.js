
function getToken(name) {
    let tokenValue = null;
    if (document.cookie && document.cookie !== '') {
        const tokens = document.cookie.split(';');
        for (let i = 0; i < tokens.length; i++) {
            const token = tokens[i].trim();
            if (token.substring(0, name.length + 1) === (name + '=')) {
                tokenValue = decodeURIComponent(token.substring(name.length + 1));
                break;
            }
        }
    }
    return tokenValue;
}
const csrftoken = getToken('csrftoken');

function getCookie(name) {
    var cookieArr = document.cookie.split(";");

    for(var i = 0; i < cookieArr.length; i++) {
        var cookiePair = cookieArr[i].split("=");

        if(name == cookiePair[0].trim()) {
            return decodeURIComponent(cookiePair[1]);
        }
    }

    return null;
}
var cart = JSON.parse(getCookie('cart'))

if (cart == undefined) {
    cart = {}
    console.log('Cart Created!', cart)
    document.cookie = 'cart=' + JSON.stringify(cart) + ";domain=;path=/"
}
console.log('Cart:', cart)