import type { NextConfig } from "next";

const nextConfig: NextConfig = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx}",
    "./src/components/**/*.{js,ts,jsx,tsx}",
    "./src/app/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: ["class"],
};

export default nextConfig;
