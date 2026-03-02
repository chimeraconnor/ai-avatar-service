import type { Metadata } from "next";

export const metadata: Metadata = {
  title: "Junimo - AI Avatar Platform for VTubers & Influencers",
  description: "Create your AI avatar clone. VTuber model with real voice cloning. Fans pay to chat 24/7. Monetize your influence with AI.",
  keywords: [
    "AI avatar for influencers",
    "VTuber AI service",
    "AI voice cloning",
    "virtual influencer",
    "chat with AI influencer",
    "monetize VTuber",
  ],
  openGraph: {
    title: "Junimo - AI Avatar Platform for VTubers",
    description: "Create your AI avatar clone. VTuber model with real voice cloning. Fans pay to chat 24/7.",
    type: "website",
    url: "https://junimo.dev",
    images: [
      {
        url: "https://junimo.dev/og-image.png",
        width: 1200,
        height: 630,
      },
    ],
  },
  twitter: {
    card: "summary_large_image",
  },
};

export default function Home() {
  return (
    <div className="min-h-screen bg-white dark:bg-black">
      {/* Hero Section */}
      <section className="relative overflow-hidden">
        <div className="absolute inset-0 bg-gradient-to-br from-violet-600 via-purple-600 to-indigo-600 dark:from-violet-900 dark:via-purple-900 dark:to-indigo-900" />
        
        <div className="relative px-4 py-24 sm:px-6 lg:px-8">
          <div className="mx-auto max-w-7xl">
            <div className="grid gap-12 lg:grid-cols-2 lg:gap-16 lg:items-center">
              
              {/* Left: Content */}
              <div className="space-y-8">
                <div className="space-y-4">
                  <div className="inline-flex items-center gap-2 rounded-full bg-white/10 px-4 py-2 text-sm font-medium text-violet-600 dark:text-violet-400 dark:bg-violet-900/20">
                    <span>🎭</span>
                    <span>For VTubers, Streamers & Influencers</span>
                  </div>
                  
                  <h1 className="text-5xl sm:text-6xl font-extrabold tracking-tight text-white dark:text-zinc-50">
                    Transform Your
                    <span className="block bg-gradient-to-r from-yellow-400 via-pink-500 to-red-500 bg-clip-text text-transparent">
                      Influence
                    </span>
                    <br />
                    Into AI
                  </h1>
                  
                  <p className="text-xl text-white/90 dark:text-zinc-300 leading-relaxed">
                    Clone your voice. Train your personality. 
                    <span className="font-semibold text-white dark:text-zinc-50">Earn while you sleep.</span>
                  </p>

                  {/* Stats */}
                  <div className="grid gap-4 pt-8 sm:grid-cols-3">
                    <div className="text-center">
                      <div className="text-3xl font-bold text-white dark:text-zinc-50">$71K</div>
                      <div className="text-sm text-white/80 dark:text-zinc-400">First week revenue (CarynAI)</div>
                    </div>
                    <div className="text-center">
                      <div className="text-3xl font-bold text-white dark:text-zinc-50">70%</div>
                      <div className="text-sm text-white/80 dark:text-zinc-400">Revenue to creators</div>
                    </div>
                    <div className="text-center">
                      <div className="text-3xl font-bold text-white dark:text-zinc-50">24/7</div>
                      <div className="text-sm text-white/80 dark:text-zinc-400">AI chat with fans</div>
                    </div>
                  </div>

                  {/* CTAs */}
                  <div className="flex flex-col gap-3 sm:flex-row pt-8">
                    <button className="flex-1 h-14 items-center justify-center rounded-xl bg-white text-violet-600 font-semibold text-lg transition-all hover:scale-105 hover:shadow-2xl dark:bg-zinc-900 dark:text-violet-400">
                      Start Free Trial
                    </button>
                    <button className="flex-1 h-14 items-center justify-center rounded-xl border-2 border-white/30 bg-white/10 text-white font-semibold text-lg backdrop-blur-sm transition-all hover:bg-white/20 hover:border-white/50 dark:border-zinc-700 dark:bg-zinc-900/50 dark:text-zinc-50">
                      View Pricing
                    </button>
                  </div>
                </div>
              </div>

              {/* Right: Visual */}
              <div className="relative">
                <div className="relative aspect-square max-w-lg mx-auto lg:max-w-full">
                  {/* Glowing effect */}
                  <div className="absolute inset-0 bg-gradient-to-br from-violet-500/30 to-pink-500/30 rounded-3xl blur-3xl" />
                  
                  {/* Main avatar illustration */}
                  <div className="relative flex h-full items-center justify-center">
                    <div className="text-center">
                      <div className="text-9xl mb-4">🎭</div>
                      
                      <div className="space-y-6">
                        <div className="flex items-center justify-center gap-3 text-white dark:text-zinc-50">
                          <div className="h-12 w-12 rounded-xl bg-white/20 backdrop-blur-sm flex items-center justify-center">
                            <span className="text-2xl">🎤</span>
                          </div>
                          <span className="font-semibold text-lg">Voice Cloning</span>
                        </div>
                        
                        <div className="flex items-center justify-center gap-3 text-white dark:text-zinc-50">
                          <div className="h-12 w-12 rounded-xl bg-white/20 backdrop-blur-sm flex items-center justify-center">
                            <span className="text-2xl">🧠</span>
                          </div>
                          <span className="font-semibold text-lg">Personality AI</span>
                        </div>
                        
                        <div className="flex items-center justify-center gap-3 text-white dark:text-zinc-50">
                          <div className="h-12 w-12 rounded-xl bg-white/20 backdrop-blur-sm flex items-center justify-center">
                            <span className="text-2xl">💰</span>
                          </div>
                          <span className="font-semibold text-lg">Earn 24/7</span>
                        </div>
                      </div>

                      {/* Demo badge */}
                      <div className="mt-8 inline-flex items-center gap-2 rounded-full bg-white/20 px-4 py-2 text-sm font-medium text-white dark:text-zinc-300">
                        <span className="w-2 h-2 rounded-full bg-green-400 animate-pulse" />
                        <span>Demo Coming Soon</span>
                      </div>
                    </div>
                  </div>
                </div>

                {/* Floating elements */}
                <div className="absolute -top-4 -right-4 hidden lg:block">
                  <div className="space-y-3 text-right">
                    <div className="rounded-2xl bg-white/10 backdrop-blur-md p-4">
                      <div className="text-2xl mb-2">✨</div>
                      <div className="text-sm text-white dark:text-zinc-300">3-5 day setup</div>
                    </div>
                    <div className="rounded-2xl bg-white/10 backdrop-blur-md p-4">
                      <div className="text-2xl mb-2">🔒</div>
                      <div className="text-sm text-white dark:text-zinc-300">Age verified & legal</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works */}
      <section className="px-4 py-24 sm:px-6 lg:px-8 bg-zinc-50 dark:bg-zinc-950">
        <div className="mx-auto max-w-7xl">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-zinc-900 dark:text-zinc-50 mb-4">
              How It Works
            </h2>
            <p className="text-xl text-zinc-600 dark:text-zinc-400">
              Get your AI avatar live in <span className="font-semibold text-violet-600 dark:text-violet-400">3-5 days</span>
            </p>
          </div>

          <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-4">
            {[
              {
                icon: "🎭",
                step: "01",
                title: "Upload VTuber Avatar",
                description: "Your existing 3D model or custom anime-style design",
              },
              {
                icon: "🎤",
                step: "02",
                title: "Clone Your Voice",
                description: "10-20 audio samples, your real voice not AI",
              },
              {
                icon: "🧠",
                step: "03",
                title: "Train AI Personality",
                description: "Upload Q&A, social content, style preferences",
              },
              {
                icon: "💰",
                step: "04",
                title: "Launch & Earn",
                description: "Fans pay by minute or subscription, you earn 24/7",
              },
            ].map((item) => (
              <div key={item.step} className="relative group">
                <div className="absolute -top-2 -left-2 text-6xl font-bold text-violet-200 dark:text-violet-900/30">
                  {item.icon}
                </div>
                <div className="relative rounded-2xl border border-zinc-200 bg-white p-8 pt-16 shadow-lg transition-all hover:shadow-2xl hover:-translate-y-1 dark:border-zinc-800 dark:bg-zinc-900">
                  <div className="text-violet-600 dark:text-violet-400 font-bold text-sm mb-2">
                    {item.step}
                  </div>
                  <h3 className="mb-3 text-xl font-bold text-zinc-900 dark:text-zinc-50">
                    {item.title}
                  </h3>
                  <p className="text-zinc-600 dark:text-zinc-400">
                    {item.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Features Grid */}
      <section className="px-4 py-24 sm:px-6 lg:px-8 bg-white dark:bg-zinc-900">
        <div className="mx-auto max-w-7xl">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-zinc-900 dark:text-zinc-50 mb-4">
              Why Choose Junimo?
            </h2>
          </div>

          <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
            {[
              {
                title: "VTuber Model",
                description: "Custom 3D anime-style avatar, not face cloning. Your virtual self, on your terms.",
                icon: "🎭",
                highlight: "No Face Cloning",
              },
              {
                title: "Real Voice Cloning",
                description: "Your actual voice, not AI-generated. Fans recognize and connect with you.",
                icon: "🎤",
                highlight: "Authentic Voice",
              },
              {
                title: "Personality AI",
                description: "LLM trained on your speech patterns, tone, vocabulary. Responds like you would.",
                icon: "🧠",
                highlight: "Natural Conversations",
              },
              {
                title: "24/7 Earnings",
                description: "Fans pay by the minute or subscribe monthly. You earn while offline.",
                icon: "💰",
                highlight: "Passive Income",
              },
              {
                title: "70% Revenue Share",
                description: "You keep 70% of earnings. We take 30% platform fee. Transparent pricing.",
                icon: "📊",
                highlight: "Fair Split",
              },
              {
                title: "3-5 Day Setup",
                description: "We handle everything - voice cloning, AI training, avatar integration. No technical skills needed.",
                icon: "⚡",
                highlight: "Fast Launch",
              },
              {
                title: "Age Verified",
                description: "18+ age verification for creators and fans. Compliant with all platforms.",
                icon: "🔒",
                highlight: "Legal & Safe",
              },
              {
                title: "Multi-Platform",
                description: "Works with all major platforms - OnlyFans, Twitch, YouTube, Instagram, Twitter.",
                icon: "🌐",
                highlight: "Everywhere",
              },
            ].map((feature, index) => (
              <div key={index} className="group">
                <div className="mb-3 inline-flex items-center gap-2 rounded-full bg-violet-100 dark:bg-violet-900/30 px-3 py-1 text-sm font-semibold text-violet-700 dark:text-violet-400">
                  {feature.icon}
                  <span>{feature.highlight}</span>
                </div>
                <div className="rounded-2xl border border-zinc-200 bg-zinc-50 p-6 transition-all group-hover:border-violet-300 group-hover:bg-violet-50 dark:border-zinc-800 dark:bg-zinc-800/50">
                  <h3 className="mb-2 text-lg font-bold text-zinc-900 dark:text-zinc-50">
                    {feature.title}
                  </h3>
                  <p className="text-zinc-600 dark:text-zinc-400">
                    {feature.description}
                  </p>
                </div>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* Pricing */}
      <section className="px-4 py-24 sm:px-6 lg:px-8 bg-gradient-to-b from-zinc-50 to-white dark:from-zinc-900 dark:to-zinc-950">
        <div className="mx-auto max-w-6xl">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-zinc-900 dark:text-zinc-50 mb-4">
              Simple, Transparent Pricing
            </h2>
            <p className="text-xl text-zinc-600 dark:text-zinc-400">
              Start earning. Keep 70% of all revenue.
            </p>
          </div>

          <div className="grid gap-6 md:grid-cols-3">
            {[
              {
                name: "Starter",
                price: "$499",
                setup: "Setup Fee",
                features: [
                  "VTuber model included",
                  "Voice cloning",
                  "Personality training",
                  "Basic analytics",
                  "Email support",
                ],
                popular: false,
              },
              {
                name: "Pro",
                price: "$999",
                setup: "Setup Fee",
                features: [
                  "Everything in Starter",
                  "Advanced analytics",
                  "Priority support",
                  "Video avatar generator",
                  "Multi-platform integration",
                  "Custom branding",
                ],
                popular: true,
              },
              {
                name: "Enterprise",
                price: "Custom",
                setup: "Contact Sales",
                features: [
                  "Unlimited avatars",
                  "White-label solution",
                  "Dedicated support",
                  "API access",
                  "Custom integrations",
                  "SLA guarantee",
                ],
                popular: false,
              },
            ].map((plan) => (
              <div
                key={plan.name}
                className={`relative rounded-2xl border-2 p-8 transition-all ${
                  plan.popular
                    ? "border-violet-600 bg-white shadow-2xl scale-105"
                    : "border-zinc-200 bg-zinc-50 hover:border-zinc-300 dark:border-zinc-800 dark:bg-zinc-900 dark:hover:border-zinc-700"
                }`}
              >
                {plan.popular && (
                  <div className="absolute -top-3 -right-3 rounded-full bg-gradient-to-r from-orange-500 to-red-500 px-4 py-1 text-sm font-bold text-white shadow-lg">
                    MOST POPULAR
                  </div>
                )}
                
                <div className="mb-2 text-sm font-semibold text-zinc-500 dark:text-zinc-400 uppercase tracking-wider">
                  {plan.setup}
                </div>
                
                <div className="mb-4">
                  <div className="text-5xl font-bold text-zinc-900 dark:text-zinc-50 mb-2">
                    {plan.price}
                  </div>
                  <div className="text-zinc-600 dark:text-zinc-400">
                    {plan.name}
                  </div>
                </div>

                <ul className="space-y-3 mb-6">
                  {plan.features.map((feature, idx) => (
                    <li key={idx} className="flex items-start gap-3 text-zinc-700 dark:text-zinc-300">
                      <span className="mt-1.5 text-green-500 font-bold">✓</span>
                      <span>{feature}</span>
                    </li>
                  ))}
                </ul>

                <button
                  className={`w-full h-14 rounded-xl font-semibold text-lg transition-all ${
                    plan.popular
                      ? "bg-violet-600 text-white hover:bg-violet-700"
                      : "border-2 border-zinc-300 bg-zinc-50 text-zinc-900 hover:border-violet-600 hover:bg-violet-50 dark:border-zinc-700 dark:bg-zinc-900 dark:text-zinc-50 dark:hover:border-violet-600 dark:hover:bg-violet-900"
                  }`}
                >
                  Get Started
                </button>
              </div>
            ))}
          </div>
        </div>
      </section>

      {/* FAQ */}
      <section className="px-4 py-24 sm:px-6 lg:px-8 bg-white dark:bg-zinc-900">
        <div className="mx-auto max-w-4xl">
          <div className="text-center mb-16">
            <h2 className="text-4xl font-bold text-zinc-900 dark:text-zinc-50 mb-4">
              Frequently Asked Questions
            </h2>
          </div>

          <div className="space-y-4">
            {[
              {
                q: "How long does it take to set up?",
                a: "3-5 days. We handle everything — voice cloning, AI training, and avatar integration. You just upload your VTuber model and voice samples.",
              },
              {
                q: "Do I need technical skills?",
                a: "No. If you have a VTuber avatar and voice samples, we do the rest. Our team sets up everything for you.",
              },
              {
                q: "How much can I earn?",
                a: "Top VTubers earn $500-$50,000/month. Earnings depend on your follower count, engagement, and pricing model. Our top creators earn 6 figures annually.",
              },
              {
                q: "Is this legal?",
                a: "Yes, with your explicit consent. We require age verification (18+) for both creators and fans. All content is compliant with platform terms.",
              },
              {
                q: "What's the revenue split?",
                a: "You keep 70% of all earnings. We take a 30% platform fee to cover AI costs, infrastructure, and support. Stripe handles payouts automatically.",
              },
              {
                q: "Which platforms work?",
                a: "All major platforms — OnlyFans, Twitch, YouTube, Instagram, Twitter/X, Patreon, Fansly. We integrate with your existing audience.",
              },
            ].map((faq, index) => (
              <details key={index} className="group rounded-2xl border border-zinc-200 bg-zinc-50 dark:border-zinc-800 dark:bg-zinc-900">
                <summary className="flex cursor-pointer list-none items-center justify-between p-8 font-semibold text-lg text-zinc-900 dark:text-zinc-50 transition-all hover:text-violet-600 dark:hover:text-violet-400 group-open:text-violet-600 dark:group-open:text-violet-400">
                  <span className="flex items-center gap-3">
                    <span className="text-violet-600 dark:text-violet-400">Q:</span>
                    {faq.q}
                  </span>
                  <span className="transition-transform group-open:rotate-180">▼</span>
                </summary>
                <div className="mt-0 px-8 pb-8 text-zinc-700 dark:text-zinc-300 leading-relaxed">
                  <p className="font-semibold text-zinc-900 dark:text-zinc-50 mb-3">A:</p>
                  {faq.a}
                </div>
              </details>
            ))}
          </div>
        </div>
      </section>

      {/* CTA */}
      <section className="px-4 py-24 text-center sm:px-6 lg:px-8 bg-gradient-to-b from-white to-zinc-50 dark:from-zinc-900 dark:to-zinc-950">
        <div className="mx-auto max-w-4xl">
          <h2 className="mb-6 text-4xl font-bold text-zinc-900 dark:text-zinc-50">
            Ready to Monetize Your VTuber Brand?
          </h2>
          <p className="mb-8 text-xl text-zinc-600 dark:text-zinc-400">
            Join hundreds of VTubers earning with AI avatars. Start your free trial today.
          </p>
          <button className="h-16 px-12 rounded-xl bg-gradient-to-r from-violet-600 to-indigo-600 text-xl font-bold text-white shadow-2xl transition-all hover:scale-105 hover:shadow-3xl dark:from-violet-700 dark:to-indigo-700 dark:hover:from-violet-600 dark:hover:to-indigo-600">
            Start Free Trial
          </button>
        </div>
      </section>

      {/* Footer */}
      <footer className="border-t border-zinc-200 bg-white px-4 py-12 sm:px-6 lg:px-8 dark:border-zinc-800 dark:bg-zinc-900">
        <div className="mx-auto max-w-7xl">
          <div className="grid gap-8 md:grid-cols-2 lg:grid-cols-4">
            <div>
              <h3 className="mb-4 font-bold text-zinc-900 dark:text-zinc-50">Junimo</h3>
              <p className="text-sm text-zinc-600 dark:text-zinc-400">
                AI Avatar Platform for VTubers & Influencers
              </p>
            </div>
            <div>
              <h3 className="mb-4 font-bold text-zinc-900 dark:text-zinc-50">Product</h3>
              <p className="text-sm text-zinc-600 dark:text-zinc-400">
                VTuber Model • Voice Cloning • Personality AI
              </p>
            </div>
            <div>
              <h3 className="mb-4 font-bold text-zinc-900 dark:text-zinc-50">Legal</h3>
              <p className="text-sm text-zinc-600 dark:text-zinc-400">
                Age Verified • Compliant • Transparent
              </p>
            </div>
            <div>
              <h3 className="mb-4 font-bold text-zinc-900 dark:text-zinc-50">Support</h3>
              <p className="text-sm text-zinc-600 dark:text-zinc-400">
                support@junimo.dev
              </p>
            </div>
          </div>
          <div className="mt-12 text-center text-sm text-zinc-500 dark:text-zinc-400">
            © 2026 Junimo. All rights reserved.
          </div>
        </div>
      </footer>
    </div>
  );
}
