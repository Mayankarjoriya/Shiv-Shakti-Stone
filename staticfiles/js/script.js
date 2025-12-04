document.addEventListener('DOMContentLoaded', function() {
    // Filter sidebar toggle for mobile
    const filterToggle = document.querySelector('.filter-toggle');
    const sidebar = document.querySelector('.filter-sidebar');

    if (filterToggle && sidebar) {
        filterToggle.addEventListener('click', function() {
            sidebar.classList.toggle('open');
        });
    }

    // Price range slider value display
    const priceRange = document.getElementById('price-range');
    const priceValue = document.getElementById('price-value');

    if (priceRange && priceValue) {
        priceRange.addEventListener('input', function() {
            priceValue.textContent = `$${this.value}`;
        });
    }
});
