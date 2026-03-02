import type { Metadata } from "next";
import { Button } from "@/components/ui/button";

export const metadata: Metadata = {
  title: "AI Avatar for Influencers | Create VTuber AI Clone & Monetize",
  description: "Transform your VTuber brand into an AI avatar. Clone your voice, train your personality, and let fans pay to chat with your virtual self. Start earning today.",
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
    title: "AI Avatar for Influencers | Create VTuber AI Clone & Monetize",
    description: "Transform your VTuber brand into an AI avatar. Clone your voice, train your personality, and let fans pay to chat with your virtual self.",
    type: "website",
    url: "https://junimo.dev",
  },
};

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-zinc-50 via-white to-zinc-100 dark:from-black dark:via-zinc-900 dark:to-black">
      {/* Hero Section */}
      <section className="relative px-4 py-20 sm:px-6 lg:px-8">
        <div className="mx-auto max-w-7xl">
          <div className="grid gap-12 lg:grid-cols-2 lg:gap-8 lg:items-center">
            {/* Left: Value Proposition */}
            <div className="space-y-8">
              <div className="space-y-4">
                <div className="inline-flex items-center rounded-full border border-zinc-200 bg-white px-4 py-2 text-sm dark:border-zinc-800 dark:bg-zinc-900">
                  <span className="text-zinc-600 dark:text-zinc-400">🚀 For VTubers, Streamers & Influencers</span>
                </div>
                <h1 className="text-4xl font-bold tracking-tight text-zinc-900 dark:text-zinc-50 sm:text-5xl">
                  Create Your <span className="text-indigo-600 dark:text-indigo-400">AI Avatar</span>.<br />
                  Monetize Your Following.
                </h1>
                <p className="text-lg leading-relaxed text-zinc-600 dark:text-zinc-400">
                  Fans pay to chat with your virtual self. Clone your voice, train your personality,
                  and earn <span className="font-semibold text-zinc-900 dark:text-zinc-50">$500-$50K/month</span> on autopilot.
                </p>
              </div>

              {/* Key Features */}
              <div className="grid gap-4 sm:grid-cols-2">
                <div className="flex items-start gap-3 rounded-lg border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
                  <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-100 text-indigo-600 dark:bg-indigo-900/20 dark:text-indigo-400">
                    🎭
                  </div>
                  <div>
                    <h3 className="font-semibold text-zinc-900 dark:text-zinc-50">VTuber Model</h3>
                    <p className="text-sm text-zinc-600 dark:text-zinc-400">Custom 3D avatar, not face cloning</p>
                  </div>
                </div>

                <div className="flex items-start gap-3 rounded-lg border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
                  <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-100 text-indigo-600 dark:bg-indigo-900/20 dark:text-indigo-400">
                    🎤
                  </div>
                  <div>
                    <h3 className="font-semibold text-zinc-900 dark:text-zinc-50">Voice Cloning</h3>
                    <p className="text-sm text-zinc-600 dark:text-zinc-400">Your real voice, not AI-generated</p>
                  </div>
                </div>

                <div className="flex items-start gap-3 rounded-lg border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
                  <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-100 text-indigo-600 dark:bg-indigo-900/20 dark:text-indigo-400">
                    🧠
                  </div>
                  <div>
                    <h3 className="font-semibold text-zinc-900 dark:text-zinc-50">Personality AI</h3>
                    <p className="text-sm text-zinc-600 dark:text-zinc-400">LLM trained on your speech patterns</p>
                  </div>
                </div>

                <div className="flex items-start gap-3 rounded-lg border border-zinc-200 bg-white p-4 dark:border-zinc-800 dark:bg-zinc-900">
                  <div className="flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-100 text-indigo-600 dark:bg-indigo-900/20 dark:text-indigo-400">
                    💰
                  </div>
                  <div>
                    <h3 className="font-semibold text-zinc-900 dark:text-zinc-50">Earn 24/7</h3>
                    <p className="text-sm text-zinc-600 dark:text-zinc-400">Fans pay while you sleep</p>
                  </div>
                </div>
              </div>

              {/* CTA Buttons */}
              <div className="flex flex-col gap-4 sm:flex-row">
                <Button size="lg" className="w-full bg-indigo-600 text-white hover:bg-indigo-700 dark:bg-indigo-500 dark:hover:bg-indigo-600">
                  Start Free Trial
                </Button>
                <Button size="lg" variant="outline" className="w-full">
                  View Pricing
                </Button>
              </div>
            </div>

            {/* Right: Demo/Social Proof */}
            <div className="relative">
              <div className="aspect-square overflow-hidden rounded-2xl border border-zinc-200 bg-gradient-to-br from-indigo-500 via-purple-500 to-pink-500 dark:border-zinc-800">
                {/* Placeholder for VTuber demo */}
                <div className="flex h-full items-center justify-center bg-zinc-900/20 text-zinc-600 dark:text-zinc-400">
                  <div className="text-center">
                    <div className="text-6xl">🎭</div>
                    <p className="mt-4 text-lg font-semibold">VTuber Demo Coming Soon</p>
                    <p className="text-sm">See how fans chat with your AI avatar</p>
                  </div>
                </div>
              </div>

              {/* Social Proof */}
              <div className="mt-8 space-y-4 rounded-lg bg-white/80 p-6 backdrop-blur-sm dark:bg-zinc-900/80">
                <div className="flex items-center gap-2 text-sm text-zinc-600 dark:text-zinc-400">
                  <span className="text-green-600">✓</span>
                  <span>Proven by CarynAI ($71K first week)</span>
                </div>
                <div className="flex items-center gap-2 text-sm text-zinc-600 dark:text-zinc-400">
                  <span className="text-green-600">✓</span>
                  <span>Age verified & compliant</span>
                </div>
                <div className="flex items-center gap-2 text-sm text-zinc-600 dark:text-zinc-400">
                  <span className="text-green-600">✓</span>
                  <span>70% revenue to creators</span>
                </div>
                <div className="flex items-center gap-2 text-sm text-zinc-600 dark:text-zinc-400">
                  <span className="text-green-600">✓</span>
                  <span>3-5 day setup time</span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="px-4 py-20 sm:px-6 lg:px-8 bg-white dark:bg-zinc-950">
        <div className="mx-auto max-w-7xl">
          <div className="mb-12 text-center">
            <h2 className="text-3xl font-bold text-zinc-900 dark:text-zinc-50">
              How It Works
            </h2>
            <p className="mt-4 text-lg text-zinc-600 dark:text-zinc-400">
              Get your AI avatar live in 3-5 days. No technical skills required.
            </p>
          </div>

          <div className="grid gap-8 md:grid-cols-3">
            {[
              {
                step: "1",
                title: "Upload VTuber Avatar",
                description: "Your existing 3D model or custom design. No face cloning involved.",
              },
              {
                step: "2",
                title: "Clone Your Voice",
                description: "10-20 audio samples (30-60 sec each). Your real voice, not AI-generated.",
              },
              {
                step: "3",
                title: "Train AI Personality",
                description: "Upload Q&A, social content, and style preferences. LLM learns your patterns.",
              },
              {
                step: "4",
                title: "Launch & Earn",
                description: "Fans pay by the minute or monthly subscription. You earn while offline.",
              },
            ].map((item) => (
              <div key={item.step} className="rounded-lg border border-zinc-200 bg-zinc-50 p-8 dark:border-zinc-800 dark:bg-zinc-900">
                <div className="mb-4 flex h-12 w-12 items-center justify-center rounded-full bg-indigo-600 text-2xl font-bold text-white dark:bg-indigo-500">
                  {item.step}
                </div>
                <h3 className="mb-2 text-xl font-bold text-zinc-900 dark:text-zinc-50">{item.title}</h3>
                <p className="text-zinc-600 dark:text-zinc-400">{item.description}</p>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing CTA */}
      <section className="px-4 py-20 text-center sm:px-6 lg:px-8 bg-indigo-50 dark:bg-zinc-900">
        <div className="mx-auto max-w-4xl">
          <h2 className="mb-4 text-3xl font-bold text-zinc-900 dark:text-zinc-50">
            Ready to Monetize Your VTuber Brand?
          </h2>
          <p className="mb-8 text-lg text-zinc-600 dark:text-zinc-400">
            Join hundreds of influencers earning with AI avatars. Start your free trial today.
          </p>
          <div className="flex flex-col gap-4 sm:flex-row sm:justify-center">
            <Button size="lg" className="w-full bg-indigo-600 text-white hover:bg-indigo-700 dark:bg-indigo-500 dark:hover:bg-indigo-600 sm:w-auto">
              Start Free Trial
            </Button>
            <Button size="lg" variant="outline" className="w-full sm:w-auto">
              Contact Sales
            </Button>
          </div>
        </div>
      </section>

      {/* FAQ Preview */}
      <section className="px-4 py-20 sm:px-6 lg:px-8 bg-white dark:bg-zinc-950">
        <div className="mx-auto max-w-3xl">
          <h2 className="mb-12 text-center text-3xl font-bold text-zinc-900 dark:text-zinc-50">
            Frequently Asked Questions
          </h2>

          <div className="space-y-6">
            {[
              {
                q: "How long does it take to set up?",
                a: "3-5 days. We handle everything — voice cloning, AI training, and avatar integration.",
              },
              {
                q: "Do I need technical skills?",
                a: "No. If you have a VTuber avatar and voice samples, we do the rest.",
              },
              {
                q: "How much can I earn?",
                a: "Top creators earn $500-$50,000/month. Earnings depend on your follower count and engagement.",
              },
              {
                q: "Is this legal?",
                a: "Yes, with your explicit consent. We require age verification (18+) for both creators and fans.",
              },
              {
                q: "What's the revenue split?",
                a: "70% to creators, 30% platform fee. Stripe handles payouts automatically.",
              },
            ].map((faq, index) => (
              <details key={index} className="group rounded-lg border border-zinc-200 bg-zinc-50 dark:border-zinc-800 dark:bg-zinc-900">
                <summary className="flex cursor-pointer list-none items-center justify-between p-6 font-semibold text-zinc-900 dark:text-zinc-50">
                  {faq.q}
                  <span className="transition-transform group-open:rotate-180">▼</span>
                </summary>
                <div className="mt-4 px-6 pb-6 text-zinc-600 dark:text-zinc-400">
                  {faq.a}
                </div>
              </details>
            ))}
          </div>
        </div>
      </section>

      {/* Footer CTA */}
      <footer className="border-t border-zinc-200 bg-zinc-50 px-4 py-12 sm:px-6 lg:px-8 dark:border-zinc-800 dark:bg-black">
        <div className="mx-auto max-w-7xl text-center">
          <h2 className="mb-4 text-2xl font-bold text-zinc-900 dark:text-zinc-50">
            Start Your AI Avatar Journey Today
          </h2>
          <p className="mb-6 text-zinc-600 dark:text-zinc-400">
            Create your virtual self. Monetize your following. Earn 24/7.
          </p>
          <Button size="lg" className="bg-indigo-600 text-white hover:bg-indigo-700 dark:bg-indigo-500 dark:hover:bg-indigo-600">
            Get Started Now
          </Button>
        </div>
      </footer>
    </div>
  );
}
