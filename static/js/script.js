document.addEventListener("DOMContentLoaded", function () {

    /** ---------------------------
     * 🎯 Fetch Books by Category using form POST submission
     * --------------------------- */
   function getRecommendations() {
    const genre = document.getElementById("genre").value;
    if (!genre) {
        alert("⚠️ Please select a genre.");
        return;
    }

    const formData = new FormData();
    formData.append("category", genre);

    fetch("/find_books", {
        method: "POST",
        headers: { "X-Requested-With": "XMLHttpRequest" },
        body: formData
    })
    .then(response => response.json())
    .then(books => {
        displayBooks(books);
    })
    .catch(error => console.error("❌ Error fetching books:", error));
}



    /** ---------------------------
     * 🤖 Fetch AI-Based Recommendations using Google Books API (Front-end only)
     * --------------------------- */
    function getAIRecommendations() {
        const genre = document.getElementById("genre").value;
        if (!genre) {
            alert("⚠️ Please select a genre first.");
            return;
        }

        const randomStartIndex = Math.floor(Math.random() * 20);
        const googleBooksAPI = `https://www.googleapis.com/books/v1/volumes?q=subject:${encodeURIComponent(genre)}&startIndex=${randomStartIndex}&maxResults=20`;

        fetch(googleBooksAPI)
            .then(response => response.json())
            .then(data => {
                if (data.items) {
                    const books = data.items.map(item => ({
                        title: item.volumeInfo.title || "Unknown Title",
                        author: item.volumeInfo.authors ? item.volumeInfo.authors.join(", ") : "Unknown Author",
                        rating: item.volumeInfo.averageRating || "N/A",
                        published_date: item.volumeInfo.publishedDate || "Unknown",
                        description: item.volumeInfo.description
                            ? item.volumeInfo.description.slice(0, 150) + "..."
                            : "No description available."
                    }));
                    displayBooks(books);
                } else {
                    alert("❌ No AI recommendations found for this genre.");
                }
            })
            .catch(error => console.error("❌ Error fetching AI recommendations:", error));
    }

    function getAIRecommendations() {
    const genreSelect = document.getElementById("genre");
    if (!genreSelect) {
        alert("⚠️ Genre dropdown not found in DOM.");
        return;
    }
    const genre = genreSelect.value;
    if (!genre) {
        alert("⚠️ Please select a genre first.");
        return;
    }

    const randomStartIndex = Math.floor(Math.random() * 20);
    const googleBooksAPI = `https://www.googleapis.com/books/v1/volumes?q=subject:${encodeURIComponent(genre)}&startIndex=${randomStartIndex}&maxResults=20`;

    fetch(googleBooksAPI)
        .then(response => response.json())
        .then(data => {
            if (data.items) {
                const books = data.items.map(item => ({
                    title: item.volumeInfo.title || "Unknown Title",
                    author: item.volumeInfo.authors ? item.volumeInfo.authors.join(", ") : "Unknown Author",
                    rating: item.volumeInfo.averageRating || "N/A",
                    published_date: item.volumeInfo.publishedDate || "Unknown",
                    description: item.volumeInfo.description
                        ? item.volumeInfo.description.slice(0, 150) + "..."
                        : "No description available."
                }));
                displayBooks(books);
            } else {
                alert("❌ No AI recommendations found for this genre.");
            }
        })
        .catch(error => console.error("❌ Error fetching AI recommendations:", error));
}



    /** ---------------------------
     * 📚 Display Books in a Professional Grid Layout
     * --------------------------- */
    function displayBooks(books) {
        const bookList = document.getElementById("book-list");
        bookList.innerHTML = ""; // Clear previous results

        if (books.length === 0) {
            bookList.innerHTML = "<p>No books found.</p>";
            return;
        }

        books.forEach(book => {
            const encodedTitle = encodeURIComponent(book.title);
            const bookCoverUrl = `https://covers.openlibrary.org/b/title/${encodedTitle}-L.jpg`;

            const bookDiv = document.createElement("div");
            bookDiv.classList.add("book");

            bookDiv.innerHTML = `
                <img src="${bookCoverUrl}" alt="${book.title}" class="book-image" onerror="this.src='fallback.jpg'">
                <h3>${book.title}</h3>
                <p><strong>Author:</strong> ${book.author}</p>
                <p><strong>Rating:</strong> ${book.rating} ⭐</p>
                <p><strong>Published:</strong> ${book.published_date}</p>
                <p><strong>Description:</strong> ${book.description}</p>
                <button class="buy-btn" data-title="${book.title}">Buy</button>
            `;

            bookList.appendChild(bookDiv);
        });

        // Attach buy button listeners
        document.querySelectorAll(".buy-btn").forEach(button => {
            button.addEventListener("click", function () {
                const title = this.getAttribute("data-title");
                openBuyModal(title);
            });
        });
    }


    /** ---------------------------
     * 🛒 Modal functions (same as your JS)
     * --------------------------- */
    function openBuyModal(title) {
        const modal = document.getElementById("buyModal");
        const modalContent = document.getElementById("buyModalContent");
        const overlay = document.getElementById("buyModalOverlay");

        if (!modal || !modalContent || !overlay) {
            console.error("❌ Modal elements are missing in HTML.");
            return;
        }

        modalContent.innerHTML = `
            <h2>Buy "${title}"</h2>
            <p>Select where you want to buy this book:</p>
            <button class="buy-btn amazon-btn" onclick="buyBook('${encodeURIComponent(title)}', 'amazon')">Amazon</button>
            <button class="buy-btn flipkart-btn" onclick="buyBook('${encodeURIComponent(title)}', 'flipkart')">Flipkart</button>
            <button class="buy-btn cancel-btn" onclick="closeBuyModal()">Cancel</button>
        `;

        modal.style.display = "block";
        overlay.style.display = "block";
    }

    function closeBuyModal() {
        const modal = document.getElementById("buyModal");
        const overlay = document.getElementById("buyModalOverlay");

        if (!modal || !overlay) {
            console.error("❌ Modal elements are missing in HTML.");
            return;
        }

        modal.style.display = "none";
        overlay.style.display = "none";
    }

    function buyBook(title, platform) {
        title = decodeURIComponent(title);
        const amazonUrl = `https://www.amazon.in/s?k=${encodeURIComponent(title)}`;
        const flipkartUrl = `https://www.flipkart.com/search?q=${encodeURIComponent(title)}`;

        if (platform === "amazon") {
            window.open(amazonUrl, "_blank");
        } else if (platform === "flipkart") {
            window.open(flipkartUrl, "_blank");
        }

        closeBuyModal();
    }


    /** ---------------------------
     * 📝 Submit Book Recommendation (submit form normally to /add route)
     * --------------------------- */
    function submitBookRecommendation() {
        // Instead of fetch JSON, submit form normally or convert this to form submission
        alert("Please use the 'Add Book' form to submit books.");
    }

    /** ---------------------------
     * 🔗 Ensure all functions are globally accessible
     * --------------------------- */
    window.getRecommendations = getRecommendations;
    window.getAIRecommendations = getAIRecommendations;
    window.openBuyModal = openBuyModal;
    window.closeBuyModal = closeBuyModal;
    window.buyBook = buyBook;

});
