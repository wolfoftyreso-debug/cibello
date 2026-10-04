import { useEffect, useRef } from "react";
import { useCurrentUserState } from "@/lib/auth/use-current-user";
import { addCookLog, loadKitchen, saveKitchen } from "./api";
import { seedCookLog } from "./data";
import { useKitchen } from "./store";

function unauthorized(err: unknown) {
  return err instanceof Error && err.message === "Unauthorized";
}

/** Pull signed-in kitchen from the server; push local seed on first login. */
export function useKitchenCloud() {
  const { user, isPending } = useCurrentUserState();
  const lastSnap = useRef("");
  const ready = useRef(false);
  const wasUser = useRef(false);

  useEffect(() => {
    if (isPending) return;
    if (!user) {
      if (wasUser.current) {
        useKitchen.getState().reset();
        lastSnap.current = "";
        ready.current = false;
        wasUser.current = false;
      }
      return;
    }
    wasUser.current = true;
    let cancelled = false;
    void (async () => {
      try {
        const remote = await loadKitchen();
        if (cancelled) return;
        const local = useKitchen.getState();
        const pantry = remote.pantry.length ? remote.pantry : local.pantry;
        const list = remote.pantry.length ? remote.list : local.list;
        const week = remote.pantry.length ? remote.week : local.week;
        let cookLog = remote.cookLog;
        const first = remote.pantry.length === 0;
        if (cookLog.length === 0) {
          cookLog = seedCookLog();
          for (const entry of cookLog) {
            void addCookLog({ data: entry }).catch(() => {});
          }
        }
        useKitchen.getState().hydrate({ pantry, list, week, cookLog });
        lastSnap.current = JSON.stringify({ pantry, list, week });
        ready.current = true;
        if (first) {
          void saveKitchen({ data: { pantry, list, week } }).catch(() => {});
        }
      } catch (err) {
        if (!unauthorized(err)) console.error(err);
        ready.current = true;
      }
    })();
    return () => {
      cancelled = true;
    };
  }, [user, isPending]);

  const pantry = useKitchen((s) => s.pantry);
  const list = useKitchen((s) => s.list);
  const week = useKitchen((s) => s.week);

  useEffect(() => {
    if (!user || !ready.current) return;
    const snap = JSON.stringify({ pantry, list, week });
    if (snap === lastSnap.current) return;
    lastSnap.current = snap;
    const timer = window.setTimeout(() => {
      void saveKitchen({ data: { pantry, list, week } }).catch((err) => {
        if (!unauthorized(err)) console.error(err);
      });
    }, 700);
    return () => window.clearTimeout(timer);
  }, [user, pantry, list, week]);
}
