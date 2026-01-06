"use client";

import { useState } from "react";

type Message = {
  role: "user" | "tutor";
  content: string;
};

export default function Home() {
  const [messages, setMessages] = useState<Message[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);


  // Generate or retrieve session ID
  const getSessionId = () => {
    let sessionId = localStorage.getItem("session_id");

    if (!sessionId) {
      sessionId = crypto.randomUUID();
      localStorage.setItem("session_id", sessionId);
    }

    return sessionId;
  };

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage: Message = { role: "user", content: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const res = await fetch("/api/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: input, session_id: getSessionId() }),
      });

      const data = await res.json();

      const tutorMessage: Message = {
        role: "tutor",
        content: data.reply,
      };

      setMessages((prev) => [...prev, tutorMessage]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { role: "tutor", content: "Error connecting to server." },
      ]);
    } finally {
      setLoading(false);
    }
  };

  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-gray-100 p-4">
      <div className="w-full max-w-xl rounded-xl bg-white shadow-lg p-4">
        <h1 className="text-xl font-bold text-center mb-4">
          🧠 NeoChat
        </h1>

        <div className="h-80 overflow-y-auto border rounded p-2 mb-4 space-y-2">
          {messages.map((msg, i) => (
            <div
              key={i}
              className={`p-2 rounded ${
                msg.role === "user"
                  ? "bg-blue-100 text-right"
                  : "bg-green-100 text-left"
              }`}
            >
              <strong>{msg.role === "user" ? "You" : "Neo"}:</strong>{" "}
              {msg.content}
            </div>
          ))}

          {loading && (
            <div className="text-sm text-gray-500">Neo is typing...</div>
          )}
        </div>

        <div className="flex gap-2">
          <input
            value={input}
            onChange={(e) => setInput(e.target.value)}
            onKeyDown={(e) => e.key === "Enter" && sendMessage()}
            placeholder="Type your message..."
            className="flex-1 border rounded px-3 py-2"
          />
          <button
            onClick={sendMessage}
            className="bg-blue-600 text-white px-4 py-2 rounded"
          >
            Send
          </button>
        </div>
      </div>
    </main>
  );
}
