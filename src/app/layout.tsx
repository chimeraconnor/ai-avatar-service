import type { Metadata, Viewport } from "next";
import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const viewport: Viewport = {
  width: "device-width",
  initialScale: 1,
};

export const metadata: Metadata = {
  metadataBase: new URL("https://junimo.dev"),
  title: {
    default: "AI Avatar for Influencers | Create VTuber AI Clone & Monetize",
    template: "%s | Junimo - AI Avatar Service",
  },
  description: {
    default: "Transform your VTuber brand into an AI avatar. Clone your voice, train your personality, and let fans pay to chat with your virtual self. VTuber model with real voice cloning.",
    template: "%s | Junimo - AI Avatar Service",
  },
  keywords: [
    "AI avatar for influencers",
    "VTuber AI service",
    "AI voice cloning for creators",
    "chat with AI influencer",
    "virtual influencer platform",
    "how to create VTuber AI avatar",
    "monetize your VTuber with AI",
  ],
  openGraph: {
    title: "Junimo - AI Avatar Service for Influencers",
    description: "Create your AI avatar with VTuber model and voice cloning. Monetize your following with 24/7 AI chat.",
    type: "website",
    url: "https://junimo.dev",
    siteName: "Junimo",
  },
  twitter: {
    card: "summary_large_image",
    title: "Junimo - AI Avatar Service for Influencers",
    description: "Create your AI avatar with VTuber model and voice cloning.",
  },
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.ico" />
      </head>
      <body className={`${inter.className} antialiased`}>
        {children}
      </body>
    </html>
  );
}
