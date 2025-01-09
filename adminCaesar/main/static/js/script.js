//   Функция поиска
   function filterCards() {
        const input = document.getElementById("search-input").value.toLowerCase();
        const cards = document.querySelectorAll(".card");

        cards.forEach(card => {
            const title = card.querySelector("h3").textContent.toLowerCase();
            card.style.display = title.includes(input) ? "block" : "none";
        });
    }