function filterSeeds() {
    const country = document.getElementById('filter-country').value;
    const category = document.getElementById('filter-category').value;
    const cards = document.querySelectorAll('.seed-card');

    cards.forEach(card => {
        const matchCountry = !country || card.dataset.country === country;
        const matchCategory = !category || card.dataset.category === category;
        card.style.display = (matchCountry && matchCategory) ? '' : 'none';
    });
}
