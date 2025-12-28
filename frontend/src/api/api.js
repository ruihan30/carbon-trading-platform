const API_URL = "http://localhost:8000";

export async function login(data) {
  const res = await fetch(`${API_URL}/auth/login`, {
    method: "POST",
    headers: { "Content-Type": "application/json",},
    body: JSON.stringify(data),
  });
  return res.json();
}

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