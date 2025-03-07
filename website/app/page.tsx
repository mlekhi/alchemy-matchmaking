"use client";

import Image from "next/image";
import { useState } from "react";
import { motion } from "framer-motion";

export default function Home() {
  const [email, setEmail] = useState("");

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    const response = await fetch("/api/check-email", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ email }),
    });
    const data = await response.json();
    if (data.success) {
      // Redirect to the matches page on success
      window.location.href = `/matches?email=${email}`; // Use window.location.href for redirection
    } else {
      alert("Email not found.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen p-8 bg-gray-50">
      <header className="mb-8 text-center">
        <h1 className="text-3xl font-bold text-gray-800">Welcome to Matchmaking</h1>
        <p className="text-gray-600">Enter your registered email to find your matches.</p>
      </header>
      <motion.div
        className="bg-white shadow-lg rounded-lg p-6 w-full max-w-md"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.5 }}
      >
        <form onSubmit={handleSubmit} className="flex flex-col">
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            placeholder="Enter your registered email"
            className="border p-3 rounded mb-4 w-full focus:outline-none focus:ring-2 focus:ring-blue-500"
            required
          />
          <button type="submit" className="bg-blue-500 text-white p-3 rounded hover:bg-blue-600 transition duration-200">
            Check My Matches
          </button>
        </form>
      </motion.div>
    </div>
  );
}
