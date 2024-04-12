var totalElement = document.querySelector('#order-total');
var total = parseFloat(totalElement.dataset.total);

    var BGNtotal = total * 0.51;
    paypal.Buttons({
        style: {
            color:  'blue',
            shape:  'pill',
            label:  'pay',
            height: 40
        },
        
        createOrder: function(data, actions) {
            return actions.order.create({
                purchase_units: [{
                    amount: {
                        value: BGNtotal.toFixed(2)
                    }
                }]
            });
        },
        onApprove: function(data, actions) {
            return actions.order.capture().then(function(details) {
                window.submitFormData()
            });
        }
    }).render('#paypal-button-container');