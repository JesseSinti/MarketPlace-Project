const popup = document.getElementById('popup')
const filterbtn = document.getElementById('filterbtn')
const formcontainer = document.getElementById('formcontainer')

const minRange = document.getElementById("minRange");
const maxRange = document.getElementById("maxRange");

const minVal = document.getElementById("minVal");
const maxVal = document.getElementById("maxVal");

const hiddenMin = document.getElementById("price_min");
const hiddenMax = document.getElementById("price_max");


filterbtn.addEventListener('click', () => {
    if (formcontainer.style.display === 'none') {
        formcontainer.style.display = 'block'
    }
    else {
        formcontainer.style.display = 'none'
    }
})

function updateValues() {
    // converts the data into int making sure they are numbers 
    let minValue = parseInt(minRange.value);
    let maxValue = parseInt(maxRange.value);

    // if minValue becomes greater then maxValue it swaps their values with each other 
    if (minValue > maxValue) {
        [minValue, maxValue] = [maxValue, minValue];
        minRange.value = minValue;
        maxRange.value = maxValue;
    }

    // passes the values to the hidden inputs for django-filters to read and filter by 
    hiddenMin.value = minValue;
    hiddenMax.value = maxValue;
}

// calls the updatevalue functions whenever the sliders are being changed
minRange.oninput = updateValues;
maxRange.oninput = updateValues;

updateValues();


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
               popup.classList.add("active")
               setTimeout(() => {
                popup.classList.remove("active");    
               }, 2000);
            }
        })
        
    })
})
