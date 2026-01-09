import axios from "axios";

const API_URL = "http://localhost:8000";

export async function createUser(data) {
  const res = await fetch(`${API_URL}/users`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });

  if (!res.ok) {
    const error = await res.json();
    throw new Error(error.detail || "Failed to create user");
  }

  return res.json();
}

export const login = async (data: any) => {
  console.log("📤 Sending:", { username: data.email, password: data.password });

  try {
    const response = await axios.post(`${API_URL}/auth/login`, {
      email: data.email,
      password: data.password,
    });
    return response.data;
  } catch (error: any) {
    console.error("❌ Error:", error.response?.data);
    throw error;
  }
};

export function authHeaders() {
  const token = localStorage.getItem("token");
  return {
    "Content-Type": "application/json",
    Authorization: `Bearer ${token}`,
  };
}

export async function getBalances() {
  const res = await fetch(`${API_URL}/balances`, {
    headers: authHeaders(),
  });
  return res.json();
}
