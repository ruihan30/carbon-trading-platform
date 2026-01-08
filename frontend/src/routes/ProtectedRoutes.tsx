import { useAuthStore } from "@/store/useAuthStore";
import { Navigate, Outlet, useLocation } from "react-router-dom";

export const ProtectedRoutes = () => {
  const token = useAuthStore((state) => state.token);
  const location = useLocation();

  // If there is no token, redirect to login
  // We save the 'from' location so we can redirect them back after they log in
  if (!token) {
    return <Navigate to="/" state={{ from: location }} replace />;
  }

  return (
    <div>
      <Outlet />
    </div>
  );
};
