export function PhoneMock() {
  return (
    <div
      className="relative mx-auto h-[560px] w-[270px] rounded-[48px] bg-gradient-to-br from-[#2b2b2e] to-[#131315] p-[10px] shadow-[0_50px_90px_-45px_rgb(20_30_24_/_0.55)] sm:h-[620px] sm:w-[300px] sm:rounded-[54px] sm:p-[11px]"
      aria-hidden
    >
      <span className="absolute left-1/2 top-5 z-10 h-[18px] w-[70px] -translate-x-1/2 rounded-full bg-black" />
      <div className="flex h-full flex-col overflow-hidden rounded-[40px] bg-bg sm:rounded-[44px]">
        <div className="flex items-center justify-between px-5 pt-8 text-[11px] font-semibold text-ink">
          <span>9:41</span>
          <span className="opacity-60">Cibello</span>
        </div>
        <div className="px-4 pt-3">
          <div className="mb-1 flex items-center gap-1.5 text-[11px] font-semibold uppercase tracking-[0.14em] text-green-d">
            <span className="grid size-5 place-items-center rounded-md bg-green text-white">
              <svg width="11" height="11" viewBox="0 0 32 32">
                <path d="M16 6c4.4 0 8 3.4 8 8 0 5.6-8 12-8 12S8 19.6 8 14c0-4.6 3.6-8 8-8z" fill="currentColor" />
              </svg>
            </span>
            Cibello
          </div>
          <h3 className="font-display text-[1.35rem] font-semibold leading-tight">Vad ska vi äta?</h3>
          <p className="mt-1 text-[0.78rem] text-muted">Utifrån vad ni har hemma, vad som bör användas och vad ni gillar.</p>
          <div className="mt-3 flex items-center gap-2 rounded-[12px] border border-line bg-surface px-3 py-2 text-[0.78rem] text-muted">
            Sök recept, t.ex. pannkaka…
          </div>
          <div className="mt-2.5 flex gap-1.5 overflow-hidden">
            {["Rekommenderat", "Frukost", "Lunch", "Middag"].map((c, i) => (
              <span
                key={c}
                className={
                  i === 0
                    ? "shrink-0 rounded-full bg-green px-2.5 py-1 text-[0.7rem] font-semibold text-white"
                    : "shrink-0 rounded-full bg-green-l px-2.5 py-1 text-[0.7rem] font-semibold text-green-d"
                }
              >
                {c}
              </span>
            ))}
          </div>
        </div>
        <div className="mt-3 flex flex-col gap-2.5 px-4">
          <div className="rounded-[14px] border border-line bg-surface p-3.5 shadow-[var(--shadow-soft)]">
            <div className="flex items-start justify-between gap-2">
              <h4 className="font-display text-[0.98rem] font-semibold leading-snug">Krämig kycklinggryta med svamp</h4>
              <span className="shrink-0 rounded-md bg-amber-l px-2 py-0.5 text-[0.65rem] font-semibold text-amber">Toppval</span>
            </div>
            <div className="mt-2 flex gap-1.5">
              <span className="rounded-md bg-amber-l px-2 py-0.5 text-[0.68rem] font-semibold text-amber">4.8 · 132</span>
              <span className="rounded-md bg-green-l px-2 py-0.5 text-[0.68rem] font-semibold text-green-d">82 % hemma</span>
            </div>
            <p className="mt-2 text-[0.75rem] text-muted">
              För att du har kyckling och grädde som snart går ut — och du brukar gilla krämigt.
            </p>
          </div>
          <div className="rounded-[14px] border border-line bg-surface/80 p-3.5 opacity-80">
            <div className="flex items-start justify-between gap-2">
              <h4 className="font-display text-[0.98rem] font-semibold">Snabb gurkraita</h4>
              <span className="rounded-md bg-green-l px-2 py-0.5 text-[0.65rem] font-semibold text-green-d">Passar er</span>
            </div>
            <div className="mt-2 flex gap-1.5">
              <span className="rounded-md bg-amber-l px-2 py-0.5 text-[0.68rem] font-semibold text-amber">4.6 · 89</span>
              <span className="rounded-md bg-green-l px-2 py-0.5 text-[0.68rem] font-semibold text-green-d">Lunch</span>
            </div>
          </div>
        </div>
        <div className="mt-auto mb-2 flex justify-center">
          <span className="h-1 w-24 rounded-full bg-ink/20" />
        </div>
      </div>
    </div>
  );
}
