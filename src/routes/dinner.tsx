import { createFileRoute, Navigate } from "@tanstack/react-router";

export const Route = createFileRoute("/dinner")({
  component: () => <Navigate to="/" />,
});
