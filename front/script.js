document.addEventListener("DOMContentLoaded", function() {
    const bookForm = document.getElementById("bookRoomForm");
    if (bookForm) {
        bookForm.addEventListener("submit", async function(event) {
            event.preventDefault();
            const name = document.getElementById("name").value;
            const phone = document.getElementById("phone").value;
            const aadhaar = document.getElementById("aadhaar").value;
            const checkin = document.getElementById("checkin").value;
            const roomType = document.getElementById("roomType").value;

            const response = await fetch("http://127.0.0.1:5000/book-room", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ name, phone, aadhaar, checkin, roomType })
            });

            const data = await response.json();
            alert(data.message);
        });
    }
});

async function checkRoomAvailability() {
    const response = await fetch("http://127.0.0.1:5000/room-status");
    const data = await response.json();
    document.getElementById("roomStatus").innerHTML = JSON.stringify(data);
}

async function checkCustomerStatus() {
    const response = await fetch("http://127.0.0.1:5000/customer-status");
    const data = await response.json();
    document.getElementById("customerStatus").innerHTML = JSON.stringify(data);
}
