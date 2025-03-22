// src/App.js
import React, { useState, useEffect } from "react";

function App() {
  const [menu, setMenu] = useState([]);
  const [order, setOrder] = useState([]);

  useEffect(() => {
    fetch("https://your-backend-url.com/menu")
      .then((res) => res.json())
      .then((data) => setMenu(data));
  }, []);

  const placeOrder = () => {
    fetch("https://your-backend-url.com/order", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ items: order }),
    })
      .then((res) => res.json())
      .then((data) => alert("Order placed successfully!"));
  };

  return (
    <div>
      <h1>Smart Menu</h1>
      <ul>
        {menu.map((item) => (
          <li key={item.id}>
            {item.name} - ₹{item.price} 
            <button onClick={() => setOrder([...order, item])}>Add</button>
          </li>
        ))}
      </ul>
      <button onClick={placeOrder}>Place Order</button>
    </div>
  );
}

export default App;
