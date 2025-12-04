import type { Metadata } from "next";
import "./globals.css";
import Navbar from "./components/NavBar"; // keep file name as NavBar.tsx

export const metadata: Metadata = {
  title: "OSC Blue Team",
  description: "Onboarding project",
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="en">
      <body>
        <Navbar />  {/* use the same name as the import */}
        {children}
      </body>
    </html>
  );
}
