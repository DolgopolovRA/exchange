'use strict';

let fitlerPopup = document.querySelector('.filterPopup');
let fitlerLabel = document.querySelector('.filterLabel');
let filterIcon = document.querySelector('.filterIcon');

fitlerLabel.addEventListener('click', function () {
    fitlerPopup.classList.toggle('hidden');
    fitlerLabel.classList.toggle('filterLabelPink');
    filterIcon.classList.toggle('filterIconPink');

    if (filterIcon.getAttribute('src') === 'images/filter.svg') {
        filterIcon.setAttribute('src', 'images/filterHover.svg')
    } else {
        filterIcon.setAttribute('src', 'images/filter.svg')
    }
});

let filterHeaders = document.querySelectorAll('.filterCategoryHeader');
filterHeaders.forEach(function (header) {
    header.addEventListener('click', function (event) {
        event.target.nextElementSibling.classList.toggle('hidden');
    })
});

let filterSizes = document.querySelector('.filterSizes');
let filterSizeWrap = document.querySelector('.filterSizeWrap');
filterSizeWrap.addEventListener('click', function () {
    filterSizes.classList.toggle('hidden');
});


class ProdAtr {
    constructor(prodName, price) {
        this.prodName = prodName;
        this.nums = 1;
        this.price = price;
    }
}

let allBasket = [];
let numProd = document.querySelector('.num_basket');

document.querySelector('.featuredItems').addEventListener('click', function (event) {
    if (event.target.tagName !== "BUTTON") {
        return;
    }
    const dataEl = event.target.parentNode.parentNode.nextElementSibling;
    const prodName = dataEl.querySelector('.featuredName').innerText;
    const price = Number(dataEl.querySelector('.featuredPrice').innerText.slice(1));

    let findEl = allBasket.find(item => item.prodName === prodName);

    if (findEl) {
        findEl.nums += 1;
        numProd.innerText = Number(numProd.innerText) + 1;
    } else {
        let prod = new ProdAtr(prodName, price);
        allBasket.push(prod);
        numProd.innerText = Number(numProd.innerText) + 1;
        document.querySelector('.basket_row').insertAdjacentHTML("afterend", `<ul class="basket_row">
            <li class="line">${prod.prodName}</li>
            <li class="line">${prod.nums}</li>
            <li class="line">${prod.price}</li>
        <li class="line">${prod.nums * prod.price}</li>
    </ul>`);
    }

    console.log(allBasket);
    //console.log(dataEl.querySelector('.featuredPrice').innerText);
});