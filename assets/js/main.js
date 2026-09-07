function filterSeeds() {
    const category = document.getElementById('filter-category').value;
    const cards = document.querySelectorAll('.seed-card');

    cards.forEach(card => {
        const matchCategory = !category || card.dataset.category === category;
        card.style.display = matchCategory ? '' : 'none';
    });
}
