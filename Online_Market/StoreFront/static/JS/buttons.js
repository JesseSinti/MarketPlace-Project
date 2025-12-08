
document.querySelectorAll('.add').forEach(btn => {
    btn.addEventListener('click', () => {
        const product_id = btn.dataset.id
        $.post({
            url : ADD_TO_CART_URL,
            data : {
                id_number: product_id,
                csrfmiddlewaretoken: CSRF_TOKEN
            },
            success: function(response) {
                console.log("Item successfully added to cart")
            }
        })
        
    })
})
