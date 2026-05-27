import { useEffect, useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [quote, setQuote] = useState(null);

  const fetchQuote = () => {
    axios
      .get("http://127.0.0.1:8000/api/quotes/random/")
      .then((response) => {
        setQuote(response.data);
      })
      .catch((error) => {
        console.log(error);
      });
  };
  const copyQuote = () => {
    navigator.clipboard.writeText(
      `"${quote.text}" - ${quote.author}`
    );
    alert("Quote copied!");
  };

  useEffect(() => {
    fetchQuote();
  }, []);

  return (
    <div className="container">
      <div className="quote-box">
        
      <h1 className="title">✦ QuoteVerse</h1>

      {quote ? (
        <div>
          <h2 className="quote-text">{quote.text}</h2>
          <p className="author">- {quote.author}</p>

          <button onClick={fetchQuote}>
            Generate New Quote
          </button>
          <button onClick={copyQuote}>
              Copy Quote
            </button>
        </div>
      ) : (
        <p>Loading quote...</p>
      )}
    </div>
    </div>
  );
}

export default App;